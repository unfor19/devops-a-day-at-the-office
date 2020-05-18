#!/bin/python
import os
import json
import requests


def main():
    API_URL = os.environ.get("API_URL") or "https://catfact.ninja/fact"
    API_PATH_TO_RESULT = os.environ.get("API_PATH_TO_RESULT") or "fact"
    API_RESULT_PRE_TEXT = os.environ.get(
        "API_RESULT_PRE_TEXT") or "Today's fact about cats:"
    response = requests.get(API_URL)
    if 200 <= response.status_code < 400:
        msg = f"{API_RESULT_PRE_TEXT} {response.json()[API_PATH_TO_RESULT]}"
    else:
        msg = response.text
    print(msg)


if __name__ == "__main__":
    main()
