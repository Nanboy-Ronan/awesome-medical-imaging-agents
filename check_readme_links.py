# README Link Checker
#
# This script checks the online status of links in a README.md file. It extracts all URLs from the README file
# and sends a HEAD request to each URL to determine if the link is online or not.
#
#     python check_readme_links.py path/to/README.md
#
# Author: Brandon Himpfen
# Website: himpfen.xyz

import argparse
import re
import requests
from pathlib import Path

# Some publishers block plain scripted requests (no browser session / JS challenge)
# and reliably return a non-200 status to every automated client, even a real
# browser's User-Agent from a datacenter IP. Treat these as reachable rather than
# broken when the known bot-protection status code shows up, so CI doesn't flag a
# link that a human can open fine in a browser.
KNOWN_BOT_PROTECTED = {
    "mdpi.com": {403},       # Cloudflare challenge in front of all MDPI journals
    "doi.org/10.3390": {403},  # MDPI's DOI prefix, redirects to mdpi.com
    "jmir.org": {202},       # JMIR serves a 202 "please wait" page to non-browser clients
}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    )
}


def _known_bot_protection(url, status_code):
    """Return True if `status_code` matches a known bot-protection response for `url`."""
    for domain, codes in KNOWN_BOT_PROTECTED.items():
        if domain in url and status_code in codes:
            return True
    return False


def check_links(file_path):
    contents = Path(file_path).read_text()

    # Extract all URLs from the README file
    urls = re.findall(r'\[.*\]\((http[s]?://.*?)\)', contents)

    for url in urls:
        try:
            response = requests.head(url, allow_redirects=True, timeout=10, headers=HEADERS)
            # Some servers don't support HEAD; fall back to GET before judging it broken.
            if response.status_code >= 400:
                response = requests.get(url, allow_redirects=True, timeout=10, headers=HEADERS, stream=True)
            final_url = response.url

            if response.status_code == 200:
                print(f"Link {url} is online.")
            elif _known_bot_protection(final_url, response.status_code):
                print(f"Link {url} is behind known bot-protection (got {response.status_code}); treating as online.")
            else:
                print(f"Link {url} returned status code {response.status_code}.")
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while checking link {url}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Check links in a README file.")
    parser.add_argument("readme", nargs="?", default="README.md", help="Path to README.md")
    args = parser.parse_args()
    check_links(args.readme)


if __name__ == "__main__":
    main()
