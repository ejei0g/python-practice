import sys
from requests import get

base_url = "https://weworkremotely.com/remote-jobs/search?term="
job = "python"

response = get(f"{base_url}{job}")
if response.status_code != 200:
    print("Fali requests")
else:
    print(response.text)
