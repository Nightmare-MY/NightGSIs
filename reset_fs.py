import sys
import re
import os

with open(f"{str(sys.argv[1])}", 'r') as file:
    fs_config = file.read().strip()
    for fs_config_line in fs_config.split("\n"):
        fs_node=fs_config_line.split(" ")
        #print(fs_node);
        a=oct(os.stat(f'system/{fs_node[0]}').st_mode)[-3:]
        p=os.popen(f"ls -ldn system/{fs_node[0]}")
        ls_info=re.split(r"\s{1,}",p.read())
        print(f"{fs_node[0]} {ls_info[2]}  {ls_info[3]} {a}")
        #print(fs_config_line)
        #print(re.split(r"\s{1,}",p.read()))
        input("please enter the data: ")
        #os.system(f"chown {fs_node[1]}:{fs_node[2]} system/{fs_node[0]}")
        #os.system(f"chmod {fs_node[3]} system/{fs_node[0]}")