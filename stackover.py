import requests
from bs4 import BeautifulSoup

SEARCH = 'python'
URL = f'https://stackoverflow.com/jobs?q={SEARCH}'


def get_last_page():
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, "html.parser")
    pages = soup.find('div', {'class': 's-pagination'}).find_all('a')
    last_page = pages[-2].get_text(strip=True)
    # print(type(last_page))
    # print(last_page)
    return int(last_page)


def extract_job(html):
    jobid = html['data-jobid']
    title = html.find('a', {'class': 's-link'})['title']

    # # recursive False를 사용할 경우 모든 span이 아닌 해당 레벨에 있는 span만 가지고 온다.
    # spans = html.find('h3', {'class': 'fc-black-700'}).find_all('span', recursive=False)
    #
    # for span in spans:
    #     print(span.get_text())

    # 만약 index가 2개만 존재 한다는 것을 알 경우 다음과 같이 사용가능하다.
    copmany, location = html.find('h3', {'class': 'fc-black-700'}).find_all('span', recursive=False)
    copmany = copmany.get_text(strip=True)
    location = location.get_text(strip=True)

    return {'title': title, 'company': copmany, 'location': location,
            'apply_link': f'https://stackoverflow.com/jobs/{jobid}'}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f'Scrapping : stackoverflow, page: {page}')
        r = requests.get(f'{URL}&pg={page + 1}')
        soup = BeautifulSoup(r.text, "html.parser")
        results = soup.find_all('div', {'class': '-job'})
        for result in results:
            job = extract_job(result)
            # print(result['data-jobid'])
            jobs.append(job)
    print(jobs)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
