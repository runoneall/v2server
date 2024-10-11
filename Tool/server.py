import os
import shutil


def CleanDir(path:str):
    if not os.path.exists(path=path):
        os.mkdir(path=path)
    else:
        shutil.rmtree(path=path)
        CleanDir(path=path)

def ListItem() -> list[str]:
    items = os.listdir('./resource')
    return items

def Read(name:str) -> str:
    with open(f'./resource/{name}', 'r', encoding='utf-8') as File:
        content = File.read()
    return content

def Write(name:str, content:str):
    with open(f'./resource/{name}', 'w', encoding='utf-8') as File:
        File.write(content)

def ReadOne() -> str:
    content = Read('../one.txt')
    return content

def Unite():
    unite_str = str()
    for Item in ListItem():
        content = Read(Item)
        unite_str += content+'\n\n\n'
    unite_str += ReadOne()
    Write('unite', unite_str)