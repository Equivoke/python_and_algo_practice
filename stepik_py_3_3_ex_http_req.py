"""
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с
дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и
из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.
"""
import requests
import bs4

# Считываем адрес А
res_1 = requests.get(input())
# Получаем содержимое страницы и находим все URL
html_1 = res_1.content
soup_1 = bs4.BeautifulSoup(html_1, 'html.parser')
links = [a['href'] for a in soup_1.find_all('a', href=True)]
# Пробегаемся по URL и собираем лежащие в них URL
links_in = []
for a in links:
    res_a = requests.get(a)
    html_a = res_a.content
    soup_a = bs4.BeautifulSoup(html_a, 'html.parser')
    links_a = [a['href'] for a in soup_a.find_all('a', href=True)]
    links_in.extend(links_a)
# Считываем адрес B
string_b = str(input())

print('Yes' if string_b in links_in else 'No')
