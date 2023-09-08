import os
import requests
import concurrent.futures
from datetime import datetime
import sys
import threading
import uuid

lock = threading.Lock()
urls_checked = 0
endpoints_checked = 0
last_checked_base_url = ""
current_tasks = set()
processed_base_urls = set()  # Set to store processed base URLs

def check_url(args):
    global urls_checked, lines_printed, endpoints_checked, current_tasks, last_checked_base_url, processed_base_urls
    base_url, endpoint = args
    full_url = base_url.strip() + "/" + endpoint.strip()
    status_code = None

    with lock:
        current_tasks.add(full_url)

        if base_url not in processed_base_urls:
            processed_base_urls.add(base_url)
            urls_checked += 1
            last_checked_base_url = base_url
            endpoints_checked = 0

        lines_printed += 1
        if lines_printed >= 10:
            os.system('cls' if os.name == 'nt' else 'clear')
            print_header(full_url)

    try:
        response = requests.get(full_url, timeout=5)
        status_code = response.status_code
    except requests.RequestException:
        pass
    finally:
        with lock:
            current_tasks.remove(full_url)
            endpoints_checked += 1

    return full_url, status_code

def base_url_generator(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

def combinations_generator(base_urls_file, endpoints_file):
    for base_url in base_url_generator(base_urls_file):
        with open(endpoints_file, 'r') as f:
            for endpoint in f:
                yield (base_url, endpoint.strip())

def print_header(current_url=""):
    # DIRB-like output format
    print("-----------------")
    print("Directory Brute force")
    print("By Shravan")
    print("-----------------")
    print(f"START_TIME: {datetime.now().strftime('%a %b %d %H:%M:%S %Y')}")
    print(f"URL_BASE: {base_urls_file}")
    print(f"WORDLIST_FILES: {endpoints_file}")
    print(f"URLS CHECKED: {urls_checked}")
    print(f"ENDPOINTS CHECKED FOR CURRENT URL: {endpoints_checked}")
    print("CURRENTLY CHECKING:")
    for task in current_tasks:
        print(f"  {task}")
    print()

base_urls_file = sys.argv[1]
endpoints_file = sys.argv[2]
max_threads = 40

# Initialize the lines_printed counter and print the header
lines_printed = 0
print_header()

log_filename = f"log_{uuid.uuid4().hex}.txt"

# Use ThreadPoolExecutor to check URLs concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
    for result in executor.map(check_url, combinations_generator(base_urls_file, endpoints_file)):
        url, status_code = result
        output_line = f"CHECKED: {url} ==> {status_code}"
        print(output_line)
        # Append the result to the file
        with open(log_filename, 'a') as log_file:
            log_file.write(output_line + "\n")

print(f"Log saved to: {log_filename}")
