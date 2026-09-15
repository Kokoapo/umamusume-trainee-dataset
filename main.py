from bs4 import BeautifulSoup
import requests

URL = "https://umamusu.wiki/Game:List_of_Trainees"

def parse_html(url):
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, "html.parser")
        return soup
    return None

if __name__ == "__main__":
    soup = parse_html(URL)
    if not soup:
        print("Failed to retrieve the webpage.")
        exit(1)
    print(soup.prettify())