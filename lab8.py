"""
Сколько глав в книге “Две крепости” и сколько всего персонажей в целом. Ответ вывести через запятую без пробелов.
"""

import requests

url = "https://the-one-api.dev/v2"
token = "Jce-HqLdgzwmILm-ocBn"
books = requests.get(url+'/book', headers={"Authorization":f"Bearer {token}"}).json()
for book in books["docs"]:
    if book['name'] == 'The Two Towers':
        bookid = book['_id']
chapters = requests.get(url+'/book/'+bookid+'/chapter', headers={"Authorization":f"Bearer {token}"}).json()
chapterResult = chapters['total']
characters = requests.get(url+'/character', headers={"Authorization":f"Bearer {token}"}).json()
charactersResult = characters['total']
print("Глав в книге “Две крепости”,Персонажей")
print(f'{chapterResult},{charactersResult}')