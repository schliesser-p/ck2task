import requests as req
from bs4 import BeautifulSoup
import re

def get_recepy_dict(url):
    """
    Function to extract all recepies from page.
    :param url: webpage (chefkoch)
    :return recepy: Dictionary of the recepy
    """
    page = req.get(url)
    soup_page = BeautifulSoup(page.content, "html.parser")

    recepy = {}  # dict contain all ingredients and amounts
    tables = soup_page.find_all("table")  # find all tables in page
    for table in tables:
        for row in table.find_all("tr"):
            col = row.find_all("td")
            if col != []:
                amn = col[0].text.strip()  # amount
                ingr = col[1].text.strip() # ingredient
                recepy[ingr] = amn.replace(" ", "")  # add to dict
    return recepy

    
