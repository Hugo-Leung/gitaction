#/usr/bin/python3
import sys
import subprocess

if __name__== "__main__":
    current_tag = ""

    if len(sys.argv)>1:
        ref = sys.argv[1]
        if ref.startswith("refs/tags/")
            current_tag=ref.replace("refs/tags/","")
    result = subprocess.run(['git', 'tag' ,'-l', '--sort=committerdate'], stdout=subprocess.PIPE) 
    tags_list = (result.stdout).decode("utf-8").split('\n')[:-1]
    previous_tag="empty"
    flag=False
    for i in reversed(tags_list):
        if flag or current_tag!=i:
            previous_tag=i
            break
        if current_tag!=i:
            flag=True
    print(previous_tag)
