import argparse
import json
import logging
import os
import time
from datetime import datetime

import requests

VERSION = "1.0.0"

def parse_arguments():

    parser = argparse.ArgumentParser(
        description="API Troubleshooting Toolkit"
    )

    parser.add_argument(
        "--url",
        help="API endpoint to test"
    )

    parser.add_argument(
        "--timeout",
        type=int,
        default=10,
        help="Request timeout in seconds"
    )

    return parser.parse_args()

def print_title(title):
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)


def print_section(title):
    print("\n" + "-" * 50)
    print(title)
    print("-" * 50)


def configure_logging():
    os.makedirs("logs", exist_ok=True)

    filename = f"logs/api_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    logging.basicConfig(
        filename=filename,
        level=logging.INFO,
        format="%(asctime)s - %(message)s"
    )

    return filename


def send_request(url, timeout):

    try:
        start = time.time()

        response = requests.get(url, timeout=timeout)

        end = time.time()

        response_time = (end - start) * 1000

        return response, response_time

    except requests.exceptions.Timeout:
        print("\nRequest timed out.")
        return None, None

    except requests.exceptions.ConnectionError:
        print("\nUnable to connect to the server.")
        return None, None

    except requests.exceptions.InvalidURL:
        print("\nInvalid URL.")
        return None, None

    except requests.exceptions.RequestException as e:
        print(f"\nRequest failed: {e}")
        return None, None


def display_summary(response, response_time):

    print_section("Request Summary")

    print(f"{'Status Code':<18}: {response.status_code} {response.reason}")
    print(f"{'Response Time':<18}: {response_time:.2f} ms")
    print(f"{'Content Type':<18}: {response.headers.get('Content-Type')}")
    print(f"{'Response Size':<18}: {len(response.content)} bytes")


def display_headers(response):

    print_section("Response Headers")

    for key, value in response.headers.items():
        print(f"{key:<20}: {value}")


def display_body(response):

    print_section("Response Body")

    try:

        formatted = json.dumps(response.json(), indent=4)

        if len(formatted) > 1500:
            print(formatted[:1500])
            print("\n... Output truncated ...")

        else:
            print(formatted)

    except ValueError:
        print("Response is not valid JSON.")


def save_log(logfile, url, response, response_time):

    logging.info(f"URL: {url}")
    logging.info(f"Status Code: {response.status_code}")
    logging.info(f"Reason: {response.reason}")
    logging.info(f"Response Time: {response_time:.2f} ms")
    logging.info(f"Content Type: {response.headers.get('Content-Type')}")
    logging.info(f"Response Size: {len(response.content)} bytes")

    print(f"\nLog saved to: {logfile}")


def main():

    logfile = configure_logging()

    print_title(f"API Troubleshooting Toolkit v{VERSION}")

    args = parse_arguments()
    if args.url:
        url = args.url
    else:
        url = input("Enter an API URL: ").strip()

    timeout = args.timeout

    print_section("Target URL")
    print(url)

    print("\nSending request...")

    response, response_time = send_request(url, timeout)

    if response is None:
        return

    print("\nRequest completed successfully.")

    display_summary(response, response_time)

    display_headers(response)

    display_body(response)

    save_log(logfile, url, response, response_time)

    print_title("Analysis Complete")


if __name__ == "__main__":
    main()
