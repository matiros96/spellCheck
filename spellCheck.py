#!/usr/bin/env python3
# spellCheck.py - A simple spellchecker
# Grabs word from clipboard and checks speeling.
__author__ = "Soren Matiros"
__version__ = "0.1.0"
__license__ = "MIT"

import pyperclip
import requests
import json

#TODO Implemnt costant checking.

def main():
# """ Main entry point of the app """
    text = pyperclip.paste()
    apiKey = "INSERTYOUAPIKEYHERE"
    dork = f"https://www.googleapis.com/customsearch/v1?key={apiKey}&cx=017576662512468239146:omuauf_lfve&q="
    query = dork+text

    payload = requests.get(query).content
    payload = json.loads(payload)
    if "spelling" in payload:
        output = (payload["spelling"]["correctedQuery"])
        pyperclip.copy(output)
    else:
        exit()
if __name__ == "__main__":
    # """ This is executed when run from the command line """
    main()