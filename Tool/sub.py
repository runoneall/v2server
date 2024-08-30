import requests


def get_list() -> list:
    with open('./subs.txt', 'r', encoding='utf-8') as SubFile:
        SubFileContent = SubFile.read()
    sub_list = SubFileContent.split('\n')
    sub_list = [item for item in sub_list if item]
    return sub_list

def download(url:str) -> str:
    while True:
        try:
            rep_content = requests.get(url=url)
            break
        except:
            print('Error, Retry')
    rep_content = rep_content.text
    return rep_content