from bs4 import BeautifulSoup
from requests import get
from extractors.wwr import extract_jobs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
#options.add_argument("--no-sandbox")
#options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)
main_url = "https://kr.indeed.com/jobs"
browser.get(main_url)
# How to get html?
source = browser.page_source
print(source)


#jobs = extract_jobs("iOS")
target = "iOS"

#response = get(f"{main_url}{target}")
#response = get("https://kr.indeed.com")
"""
if response.status_code != 200:
    print("fail")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup)
    job_list = soup.find_all('li')
    print(job_list.count)
"""

    # Selenium 브라우저 자동화
    # 왜 봇으로 막혔나? -> http get 리퀘스트를 보냈기 때문
    # 크롬 브라우저를 실행 -> 해당 브라우저를 방문하는로직을실행
    # How?
    # - Scrapping instagram ..etc

    # pkgs.chromium
    # pkgs.chromedriver
