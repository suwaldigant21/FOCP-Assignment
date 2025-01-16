"""4. Write a program that takes a URL as a command-line argument and reports
whether or not there is a working website at that address.
Hint: You need to get the HTTP response code.
Another Hint: StackOverflow is your friend."""

import sys
import requests

if len(sys.argv) > 1:
    url = sys.argv[1]
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"The website at {url} is working.")
        else:
            print(f"The website at {url} returned status code {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
else:
    print("Error: No URL provided.")