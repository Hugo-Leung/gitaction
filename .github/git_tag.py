#/usr/bin/python3
import sys
import subprocess

if __name__== "__main__":
    current_tag = ""

    if len(sys.argv)>1:
        current_tag = sys.argv[1]
    result = subprocess.run(['git', 'ls-remote', '--tags' ,'-q', '--sort=committerdate'], stdout=subprocess.PIPE) #git 'ls-remote' --tags -q --sort=committerdate
    tags_list = (result.stdout).decode("utf-8").split('\n')[:-1]
    print(tags_list[0].split())
    """
    previous_tag="empty"
    flag=False
    for i in reversed(tags_list):
        t=i.split()[1]
        if flag or current_tag!=i:
            previous_tag=i
            break
        if current_tag!=i:
            flag=True
    print(previous_tag)
    """
