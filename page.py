import requests

from bs4 import BeautifulSoup

def extract(page):
    url = f'https://www.onlinejobs.ph/jobseekers/jobsearch/{page}'
    r=requests.get(url)
    soap = BeautifulSoup