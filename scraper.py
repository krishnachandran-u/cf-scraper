import requests
import html5lib
import sys
import subprocess
import os
from bs4 import BeautifulSoup

submission_id = (sys.argv[1]).strip()
contestId = (sys.argv[2]).strip()
index = (sys.argv[3]).strip()
problem_name = ' '.join(sys.argv[4:])
problem_name = problem_name.strip()

URL = "https://codeforces.com/contest/" + contestId + "/submission/" + submission_id

r = requests.get(URL)

soup = BeautifulSoup(r.content, "html5lib")

pre_tag = soup.find('pre', id = "program-source-text")

if pre_tag:
    content_between_pre_tags = pre_tag.get_text(separator = "\n")

    #print(content_between_pre_tags)

else:

    print("not_found")

PATH = "/home/krishnachandran/myfiles/python/codeforces"

PATH = PATH + "/submissions"

full_path = os.path.join(PATH, contestId, index, problem_name + ".cpp")
directory = os.path.dirname(full_path)
if not os.path.exists(directory):
    os.makedirs(directory)

file_name = problem_name + ".cpp"

with open(full_path, "w") as file:
    file.write(content_between_pre_tags)



