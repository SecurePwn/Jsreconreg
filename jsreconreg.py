#!/usr/bin/env python3

import sys
import re
import requests

if len(sys.argv) != 2:
    print("Author: github.com/syedalizain033")
    print(f"Usage: {sys.argv[0]} <js.txt_input_file>")
    sys.exit(1)

input_file = sys.argv[1]
regex_pattern = r"(?i)apikey=.{32,}|(?i)secret=.{32,}|(?i)token=.{32,}|(?i)password=.{8,}|(?i)access_key=.{16,}|(?i)auth=.{16,}|(?i)private_key=.{32,}|(?i)db_pass=.{8,}|(?i)api_secret=.{32,}|(?i)auth_token=.{32,}|(?i)client_secret=.{32,}|(?i)api_key=.{32,}|(?i)session_token=.{32,}|(?i)passwd=.{8,}|(?i)credentials=.{16,}|(?i)apikey|(?i)secret|(?i)password|(?i)access_key|(?i)auth|(?i)private_key|(?i)db_pass|(?i)api_secret|(?i)auth_token|(?i)client_secret|(?i)api_key|(?i)session_token|(?i)passwd|(?i)credentials"

with open(input_file, 'r') as file:
    js_links = file.read().splitlines()

for link in js_links:
    content = requests.get(link).text
    if re.search(regex_pattern, content):
        print("Found sensitive information in:", link)
        print("\nPattern matched:", regex_pattern)
        print("--------------------------------------------")


'''
TIP: I personally paste the regex above in https://regex101.com/ and then all the listed urls, I open one by one in browser, copy the whole JS code
and paste it in regex101 website and see whats getting highligted. It may show several false positive but I really dont want to miss anything. 
'''   