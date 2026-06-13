import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

response = requests.get(
    "https://hh.ru/search/vacancy?text=Python&area=1",
    headers=headers,
    verify=False
)

soup = BeautifulSoup(response.text, "html.parser")
cards = soup.find_all("div", {"data-qa": "vacancy-serp__vacancy"})

for card in cards[:10]:
    title = card.find("a", {"data-qa": "serp-item__title"})
    company = card.find("a", {"data-qa": "vacancy-serp__vacancy-employer"})
    salary = card.find("span", {"data-qa": "vacancy-salary-compensation-type-net"})
    link = card.find("a", {"data-qa": "serp-item__title"})
    link = link["href"]
    print("Название:", title.text if title else "—")
    print("Компания:", company.text if company else "—")
    vacancy_response = requests.get(link, headers=headers)
    vacancy_soup = BeautifulSoup(vacancy_response.text, "html.parser")
    salary_block = vacancy_soup.find("div", {"data-qa": "vacancy-salary"})
    salary = salary_block.text.strip() if salary_block else "—"
    skills_block = vacancy_soup.find("ul", class_=lambda c: c and "vacancy-skill-list" in c)
    print("Зарплата:", salary)
    if skills_block:
        skills = skills_block.find_all("li")
        print('Навыки:', ', '.join([skill.text.strip() for skill in skills]))
    print('Ссылка:', link)
    print('\n-----\n')