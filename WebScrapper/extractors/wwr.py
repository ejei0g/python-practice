from bs4 import BeautifulSoup
from requests import get

def extract_jobs(keyword):

    main_url = "https://weworkremotely.com"
    base_url = f"{main_url}/remote-jobs/search?term="
    job = keyword

    response = get(f"{base_url}{job}")
    if response.status_code != 200:
        print("Fali requests")
    else:
        result = []

        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("section", class_="jobs")
        for job_section in jobs:
            job_posts = job_section.find_all("li") # list like python
            job_posts.pop()
            for post in job_posts:
                anchors = post.find_all('a')
                anchor = anchors[1]
                link = anchor['href']
                a = anchor.find_all('span', class_="company")
                company, kind, region = a
                #print(company.string)
                #print(kind.string)
                #print(region.string)
                title = anchor.find('span', class_="title")
                #print(title.string)
                #print("------")
                # Save
                job_data = {
                    'link': f"{main_url}{link}",
                    'Company': company.string,
                    'Resion': region.string,
                    'Position': title.string
                }
                result.append(job_data)

        #print(f'"{result}"')
        for res in result:
            print(res)
        return result
    # positional parameters

    #def say_hello(name, age):
    #    print(f"Hello {name} you r {age} years old")

    #say_hello("jyl", 11);

    # get "a href", company, date

    # object, list, length , object

    list_of_numbers = [1,2,3]
    first, second, third = list_of_numbers

    # span 에서 텍스트 추출 element.string
