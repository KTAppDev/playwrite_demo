from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
url = "https://store.epicgames.com/en-US/free-games"

def main():
    games = []
    games_dict = {}  # This list dict thing isn't the best way, I know
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()
        page.goto(url)
        page_source = page.inner_html('div.css-1myhtyb')
        print(page_source)

    #
    soup = BeautifulSoup(page_source, 'lxml')
    games_names = soup.find_all("div", class_="css-1h2ruwl")

    for x in games_names:
        games.append(x.text)

    for i in range(0, len(games), 2):
        games_dict[games[i]] = games[i + 1]

    for key in games_dict:
        print(key, '-', games_dict[key])

if __name__ == '__main__':
    main()
