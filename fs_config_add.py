#!/data/data/com.nightmare/files/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import re
import os
p=os.popen(f"cd tmp&&find ./system")
allpath=p.read().split("\n")
p.close()
#print(allpath)

with open(f"{str(sys.argv[1])}", 'r') as file:
    fs_config = file.read().strip()
    os.system("echo 查找手动添加的文件中...")
    for node_path in allpath:
        node_path=node_path.replace("./system/","").strip()
        node_path=node_path.replace("./system","").strip()
        alreadyHas=False
        #print(fs_config.split("\n"))
        for fs_config_line in fs_config.split("\n"):
            fs_node=fs_config_line.split(" ")
            #print(fs_node[0])
            if fs_node[0]==node_path:
                #print(node_path.replace("./","").strip())
                #print(fs_node)
                alreadyHas=True
                break
        #print(alreadyHas)
        if not alreadyHas:
            os.system(f"echo {node_path}")
            if node_path.endswith(".apk"):
                fs_config=f"{fs_config}\n{node_path} 0000 0000 00644"
            elif "bin" in node_path:
                fs_config=f"{fs_config}\n{node_path} 0000 2000 00755"
            else:
                fs_config=f"{fs_config}\n{node_path} 0000 0000 00755"
            #data = input("please enter the data: ")
            #a=oct(os.stat(f'tmp/system/{node_path}').st_mode)[-3:]
            #print(a)
            #p=os.popen(f"ls -ldn tmp/system/{node_path}")
            #ls_info=re.split(r"\s{1,}",p.read())
            #print(ls_info)
            #fs_config=f"{fs_config}\n{node_path} {ls_info[2]}  {ls_info[3]} {a}"
            #print()
    os.system("echo 已将以上文件整合进img配置文件")
with open(f"{str(sys.argv[1])}", 'w') as new:
    new.write(fs_config)