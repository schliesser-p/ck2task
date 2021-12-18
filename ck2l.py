import requests as req
from bs4 import BeautifulSoup
import re

def get_recepy_list(url):
    page = req.get(url)
    soup_page = BeautifulSoup(page.content, "html.parser")
    result = soup_page.find(
        "table",{"class":"ingredients table-header"}
    )
    table_list = []
    # every pair is one ingredient
    for row in result.findAll("tr"):
        ingredients = row.findAll("span")
        table_list.extend(ingredients)
    
    ingredient_list = []
    for ii in range(len(table_list)):
        ingredient_list.append(str(table_list[ii].contents))

    clean = []
    for ingredient in ingredient_list:
        remove_link = re.sub(r"<(?:\b[^>]*>|/a>)", "", ingredient)
        clean.append(remove_link.replace(" ", "").replace("\\n", "").replace("\n", ""))

    return clean

    
