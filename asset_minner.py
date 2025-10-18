#!/usr/bin/env python3

import requests
import re
import argparse
import os  # NEW: To interact with the operating system (create directories)
from pathlib import Path  # NEW: For modern path manipulation
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# A dictionary of regex patterns for different secrets
SECRET_PATTERNS = {
    'Google API Key': r'AIza[0-9A-Za-z-_]{35}',
    'AWS Access Key': r'AKIA[0-9A-Z]{16}',
    'GitHub Token': r'(ghp|gho|ghu|ghs|ghr)_[0-9a-zA-Z]{36}',
    'Firebase URL': r'https://[a-z0-9-]+\.firebaseio\.com',
    'Vue AWS AppSync Key': r'VUE_APP_AWS_APPSYNC_API_KEY["\']?\s*[:=]\s*["\'][a-zA-Z0-9-]{20,}',
}
def display_banner():
    """Displays an aesthetic banner for the tool."""
    yellow = "\033[93m"
    cyan = "\033[96m"
    end_color = "\033[0m"

    banner = f"""
{yellow}
>>=========================================================================<<
||  _  _    _    ___  _  _  ___  ___  ___        ___  ___   ___   ___  ___ ||
|| | \| |  /_\  / __|| || || __||   \|_ _|__ __ / __|/ _ \ |   \ | __|| _ \||
|| | .` | / _ \ \__ \| __ || _| | |) || | \ \ /| (__| (_) || |) || _| |   /||
|| |_|\_|/_/ \_\|___/|_||_||___||___/|___|/_\_\ \___|\___/ |___/ |___||_|_\||
||                                                                         ||
>>=========================================================================<<

{cyan}
          Created by: nashedi_x_coder
{end_color}
    """
    print(banner)


def find_js_links(url):
    """Finds all JavaScript file links on a given webpage."""
    # ... (This function remains the same)
    print(f"[*] Scraping {url} for JavaScript files...")
    js_links = []
    try:
        response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        for tag in soup.find_all('script', {'src': True}):
            js_url = tag['src']
            js_url = urljoin(url, js_url)
            js_links.append(js_url)

    except requests.RequestException as e:
        print(f"[!] Error fetching URL {url}: {e}")

    return js_links


# NEW: The function now takes an 'output_dir' to know where to save files
def scan_js_file(js_url, output_dir):
    """Downloads a JS file, saves it, and scans it for secrets."""
    print(f"[*] Scanning file: {js_url}")
    try:
        response = requests.get(js_url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        content = response.text

        # NEW: Save the content to a file
        try:
            # Create a safe filename from the URL
            filename = Path(urlparse(js_url).path).name
            if not filename:  # Handle cases where URL ends in /
                filename = "index.js"

            save_path = output_dir / filename
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"    [+] Saved file to: {save_path}")
        except Exception as e:
            print(f"    [!] Could not save file {js_url}: {e}")

        # --- Scanning logic (same as before) ---
        for secret_type, pattern in SECRET_PATTERNS.items():
            matches = re.findall(pattern, content)
            for match in matches:
                print(f"[!] FOUND: {secret_type} -> '{match}' in {js_url}")

    except requests.RequestException as e:
        print(f"[!] Error scanning file {js_url}: {e}")


def main():
    """Main function to parse arguments and orchestrate the scanning process."""
    display_banner()
    parser = argparse.ArgumentParser(description="A simple secret scanner for JavaScript files found on a webpage.")
    parser.add_argument("-u", "--url", required=True, help="The target URL to scan.")
    args = parser.parse_args()

    target_url = args.url

    # NEW: Create a directory for the output
    domain_name = urlparse(target_url).netloc
    output_dir = Path(domain_name)
    output_dir.mkdir(exist_ok=True)
    print(f"[*] Saving files to directory: {output_dir}")

    js_links = find_js_links(target_url)

    if not js_links:
        print("[!] No JavaScript files found.")
        return

    for link in set(js_links):
        # NEW: Pass the output directory to the scan function
        scan_js_file(link, output_dir)


if __name__ == "__main__":
    main()