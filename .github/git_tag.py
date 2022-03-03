#/usr/bin/python3
import sys
import subprocess

if __name__== "__main__":
    current_tag = ""

    if len(sys.argv)>1:
        current_tag = sys.argv[1]
    result = subprocess.run(['git', 'tag' ,'-l', '--sort=committerdate'], stdout=subprocess.PIPE) 
    tags_list = (result.stdout).decode("utf-8")#.split('\n')
    print(tags_list)
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
