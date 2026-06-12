import requests
import os
import json
import random as rd

def getDadosApi():
    page = rd.randint(0, 43)
    response = requests.get(f'https://rickandmortyapi.com/api/character?page={page}')

    path = r'H:\Python\test\data'
    path_archive = path + "/data.json"

        

    if response.status_code == 200:
        if response != None:
            data = response.json()


    else:
        print(response.status_code)
        raise(f'requisition error ')


    if not os.path.isdir(path):
        os.makedirs('data')

    with open(path_archive, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii= False)
        print("data saved")        

    return data['results']



