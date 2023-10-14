import requests
import html5lib
import sys
import json
import subprocess
import time
from bs4 import BeautifulSoup
import random

HANDLE = sys.argv[1].strip()

URL = "https://codeforces.com/api/user.status?handle=" + HANDLE + "&from=1&count=1000000"

r = requests.get(URL)

soup = BeautifulSoup(r.content, "html5lib")

body_tag = soup.find("body")

if body_tag:

    content_between_body_tags = body_tag.get_text(separator="\n")
else:

    print("<pre> tag not found on the page.")

#print(type(content_between_body_tags))

json_dict = json.loads(content_between_body_tags)

#print(json_dict)

script_name = "python3 scraper.py"

for item in json_dict["result"]:
    random_integer = random.randint(3000000, 6000000)
    time.sleep(random_integer / 100000)
    if item["verdict"] != "OK":
        continue
    submission_id = str(item["id"]).strip()
    contestId = str(item["contestId"]).strip()
    index = str(item["problem"]["index"]).strip()
    problem_name = str(item["problem"]["name"]).strip()
    bash_command = script_name + " " + submission_id + " " + contestId + " " + index + " " + problem_name
    subprocess.run(bash_command, shell = True)
    print("[SUCCESSFUL] id: " + submission_id + " | contestId: " + contestId + " | index: " + index + " | problem_name: " + problem_name)
   
