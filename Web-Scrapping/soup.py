# from bs4 import BeautifulSoup
# import requests

# url = 'https://realpython.github.io/fake-jobs/'

# page = requests.get(url)

# soup = BeautifulSoup(page.text, 'html')

# print(soup)

# import requests
# from bs4 import BeautifulSoup

# url = "https://realpython.github.io/fake-jobs/"
# response = requests.get(url)

# soup = BeautifulSoup(response.text, "html.parser")

# job_cards = soup.find_all("div", class_="card-content")

# for job in job_cards:
#     title = job.find("h2", class_="title").text.strip()
#     company = job.find("h3", class_="company").text.strip()
#     location = job.find("p", class_="location").text.strip()

#     # Find the parent card and the Apply link
#     card = job.parent
#     apply_link = card.find("a", string="Apply")

#     job_url = apply_link["href"] if apply_link else "N/A"

#     print(f"Job Title: {title}")
#     print(f"Company: {company}")
#     print(f"Location: {location}")
#     print(f"URL: {job_url}")
#     print("-" * 50)

import requests
from bs4 import BeautifulSoup
import csv

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

job_cards = soup.find_all("div", class_="card-content")

with open("jobs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Header row
    writer.writerow(["Job Title", "Company Name", "Location", "Job URL"])

    for job in job_cards:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()

        card = job.parent
        apply_link = card.find("a", string="Apply")
        job_url = apply_link["href"] if apply_link else ""

        writer.writerow([title, company, location, job_url])

print("Jobs saved to jobs.csv")