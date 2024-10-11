import requests
import RandomUA


def get_list() -> list:
    with open('./subs.txt', 'r', encoding='utf-8') as SubFile:
        SubFileContent = SubFile.read()
    sub_list = SubFileContent.split('\n')
    sub_list = [item for item in sub_list if item]
    return sub_list

def download(url:str) -> str:
    while True:
        try:
            ua = RandomUA.Get()
            headers = {
                'User-Agent': ua
            }
            print(f'UA Plus: {ua}')
            rep_content = requests.get(url=url, headers=headers, timeout=(5, 7))
            print(f'Status Code: {rep_content.status_code}')
            break
        except requests.exceptions.Timeout:
            print("Time Out")
        except KeyboardInterrupt:
            exit()
        except:
            print('Error, Retry')
    rep_content = rep_content.text
    return rep_content