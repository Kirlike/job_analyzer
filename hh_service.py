import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()

def parse_vacancies(query:str) -> list[dict]:
    vacancies = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    response = requests.get(
        f"https://hh.ru/search/vacancy?text={query}&area=1",
        headers=headers,
        verify=False
    )

    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.find_all("div", {"data-qa": "vacancy-serp__vacancy"})

    for card in cards:
        vacancy = {}
        title = card.find("a", {"data-qa": "serp-item__title"})
        company = card.find("a", {"data-qa": "vacancy-serp__vacancy-employer"})
        link = card.find("a", {"data-qa": "serp-item__title"})
        link = link["href"]
        vacancy['title'] = title.text
        vacancy['company'] = company.text
        vacancy_response = requests.get(link, headers=headers, verify=False)
        vacancy_soup = BeautifulSoup(vacancy_response.text, "html.parser")
        salary_block = vacancy_soup.find("div", {"data-qa": "vacancy-salary"})
        salary = salary_block.text.strip() if salary_block else "—"
        skills_block = vacancy_soup.find("ul", class_=lambda c: c and "vacancy-skill-list" in c)
        vacancy['salary'] = salary
        vacancy['skills'] = ', '.join([skill.text.strip() for skill in skills_block.find_all("li")]) if skills_block else ' '
        vacancy['link'] = link
        vacancies.append(vacancy)
    return vacancies
