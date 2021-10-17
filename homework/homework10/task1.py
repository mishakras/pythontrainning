"""
Homework
Ваша задача спарсить информацию о компаниях, находящихся в
индексе S&P 500 с данного сайта:
https://markets.businessinsider.com/index/components/s&p_500

Для каждой компании собрать следующую информацию:

Текущая стоимость в рублях (конвертацию производить по текущему курсу,
взятому с сайта центробанка РФ)
Код компании (справа от названия компании на странице компании)
P/E компании (информация находится справа от графика на странице компании)
Годовой рост/падение компании в процентах (основная таблица)
Высчитать какую прибыль принесли бы акции компании (в процентах), если
бы они были куплены на уровне 52 Week Low и проданы на уровне
52 Week High (справа от графика на странице компании)
Сохранить итоговую информацию в 4 JSON файла:

Топ 10 компаний с самими дорогими акциями в рублях.
Топ 10 компаний с самым низким показателем P/E.
Топ 10 компаний, которые показали самый высокий рост за последний год
Топ 10 комппаний, которые принесли бы наибольшую прибыль, если бы были
 куплены на самом минимуме и проданы на самом максимуме за последний год.
Пример формата:
[
{
    "code": "MMM",
    "name": "3M CO.",
    "price" | "P/E" | "growth" | "potential profit" : value,
},
...
]
For scrapping you cans use beautifulsoup4
For requesting aiohttp
"""
import asyncio
import aiohttp
from bs4 import BeautifulSoup


def make_string(tasks):
    str1 = ""
    for index, i in enumerate(tasks):
        if index > 10:
            break
        str1 += '{\n'
        str1 += '\t"code": "' + i[1] + '"\n'
        str1 += '\t"name": "' + i[0] + '"\n'
        str1 += '\t"' + str(i[2]) + '" |'
        str1 += ' "' + str(i[3]) + '" |'
        str1 += ' "potential profit" : ' + str(i[4]) + ',\n'
        str1 += '},\n'
    str1 = '[\n' + str1[:len(str1) - 2] + '\n]'
    return str1


async def start():
    tasks = [asyncio.create_task(main(i)) for i in range(0, 11)]
    await asyncio.gather(*tasks)
    companies = []
    for i in tasks:
        for j in i.result():
            companies.append(j.result())
    tasks = []
    for i in companies:
        if i not in tasks:
            tasks.append(i)
    tasks.sort(key=lambda x: x[2], reverse=True)
    str1 = make_string(tasks)
    with open('../../price.json', 'w') as fi:
        fi.write(str1)
    tasks.sort(key=lambda x: x[3], reverse=True)
    str1 = make_string(tasks)
    with open('p/e.json', 'w') as fi:
        fi.write(str1)
    tasks.sort(key=lambda x: x[4], reverse=True)
    str1 = make_string(tasks)
    with open('dif.json', 'w') as fi:
        fi.write(str1)


async def main(i):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://markets.businessinsider.com/'
                               'index/components/s&p_500?p='
                               + str(i)) as response:
            html = await response.text()
    soup = BeautifulSoup(html, 'html.parser')
    companies = []
    for index, link in enumerate(soup.find_all('a')):
        if "stocks" in link.get('href'):
            if 50 <= index <= 200:
                companies.append(link.get('href'))
    tasks = [asyncio.create_task(company(url)) for url in companies]
    await asyncio.gather(*tasks)
    return tasks


def cost(temp):
    while temp[0] == '\n' or temp[0] == '\t' or temp[0] == '\r':
        temp = temp[1:]
    while temp[len(temp) - 1] == '\n' or temp[len(temp) - 1] == '\t'\
            or temp[len(temp) - 1] == '\r':
        temp = temp[:len(temp) - 1]
    if ',' in temp:
        index = temp.find(',')
        temp = temp[:index] + temp[index + 1:]
    index = temp.find('.')
    temp = temp[:index] + temp[index + 1:]
    temp = int(temp) / 100
    return temp


def div(soup):
    p_e = 0
    for j in soup.find_all('div'):
        if 'class' in j.attrs:
            if ['snapshot__highlow-container'] == j['class']:
                try:
                    temp = j.contents[3].contents[1].contents[0]
                    week_low = cost(temp)
                    temp = j.contents[3].contents[3].contents[0]
                    week_high = cost(temp)
                    temp = (week_high-week_low)/week_low
                except IndexError:
                    temp = 0
            elif ['snapshot__data-item'] == j['class']:
                if 'Ratio' in str(j.contents[1].string):
                    p_e = cost(str(j.contents[0].string))
    return [p_e, temp]


def span(soup):
    for j in soup.find_all('span'):
        if 'class' in j.attrs:
            if ['price-section__label'] == j['class']:
                name = str(j.string)[:len(str(j.string))-1]
            elif ['price-section__category'] == j['class']:
                company_type = str(j.span.string)[2:]
            elif['price-section__current-value'] == j['class']:
                price = cost(str(j.string))
    return [name, company_type, price]


async def company(href):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://markets.businessinsider"
                               ".com/"+href) as response:
            html = await response.text()
    soup = BeautifulSoup(html, 'html.parser')
    name, company_type, price = span(soup)
    week_diff, p_e = div(soup)
    return [name, company_type, price, p_e, week_diff]


loop = asyncio.get_event_loop()
loop.run_until_complete(start())
