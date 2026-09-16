from bs4 import BeautifulSoup
import pandas as pd
import requests

URL = "https://umamusu.wiki/Game:List_of_Trainees"

def parse_html(url):
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, "html.parser")
        return soup
    return None

def extract_table_data(soup):
    # Table Tag
    table_tag = soup.find("table")
    if not table_tag:
        return None

    # tr (Table Row) Tags
    tr_table_tags = table_tag.find_all("tr")
    th_table_tags = tr_table_tags[0]
    table_headers = []
    th_tags = th_table_tags.find_all("th")
    th_tags = th_tags[1:]   # Remove Icon
    for th_tag in th_tags:
        table_headers.append(th_tag.text)

    tr_table_tags = tr_table_tags[1:]   # Remove Header Row
    table_data = []
    for tr_tag in tr_table_tags:
        td_tags = tr_tag.find_all("td")
        table_data.append(extract_table_row_data(td_tags))
    return table_headers, table_data

def extract_table_row_data(td_tags):
    name_tag = td_tags[1]
    character_tag = td_tags[2]
    release_tags = td_tags[3:5]
    rarity_tag = td_tags[5]
    stats_tags = td_tags[6:11]
    tds_tags = td_tags[11:]

    data = []

    # Scrap Name
    data.append(name_tag.b.a.text)

    # Scrap Character
    data.append(character_tag.text)

    # Scrap Releases
    for release_tag in release_tags:
        data.append(release_tag.text if release_tag.text != "N/A" else None)

    # Scrap Rarity
    data.append(len(rarity_tag.text))   # Number of Stars

    # Scrap Stats
    for stats_tag in stats_tags:
        data.append(int(stats_tag.text))

    # Scrap Track / Distance / Style
    for tds_tag in tds_tags:
        data.append(tds_tag.span.a.attrs['href'][11])    # Find Image Ref, Get X from "/File:Rank_X.png"

    return data

if __name__ == "__main__":
    soup = parse_html(URL)
    if not soup:
        print("Failed to retrieve the webpage.")
        exit(1)

    table_headers, table_data = extract_table_data(soup)
    if not table_headers or not table_data:
        print("No table headers or data found.")
        exit(1)

    df = pd.DataFrame(table_data)
    df.columns = table_headers

    df.to_csv("data.csv")