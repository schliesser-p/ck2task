import requests as req
from bs4 import BeautifulSoup


def get_recepy_list(url):
    page = req.get(url)
    soup_page = BeautifulSoup(page.content, "html.parser")
    result = soup_page.find(
        "table",{"class":"ingredients table-header"}
    )
    return result
