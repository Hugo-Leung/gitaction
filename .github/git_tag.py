import sys
import subprocess

current_tag = ""

if len(sys.argv)>1:
    current_tag = sys.argv[1]

result = subprocess.run(['git', 'tag', '-l', '--sort=committerdate'], stdout=subprocess.PIPE)
tags_list = (result.stdout).decode("utf-8").split('\n')[:-1]

previous_tag=""
flag=False
for i in reversed(tags_list):
    if flag or current_tag!=i:
        previous_tag=i
        break
    if current_tag!=i:
        flag=True
print(previous_tag)
