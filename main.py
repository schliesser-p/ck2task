from ck2l import get_recepy_list

def main():
    url = "https://www.chefkoch.de/rezepte/772011180069862/Die-echte-Sauce-Bolognese.html"
    recepy = get_recepy_list(url)
    print(recepy)
if __name__ == "__main__":
    main()