from bs4 import BeautifulSoup
import requests


def parcing(site):
    request_site = requests.get(site)
    content_tomato = request_site.content
    soup = BeautifulSoup(content_tomato, 'lxml')
    massiv_content_container = soup.find(class_='main-content').find_all(class_='region')
    for element in massiv_content_container:
        # find_unerline = soup.find(class_="text-underline")
        # soup_element = BeautifulSoup(element.text, 'lxml')
        oblast_menu = element.find(class_='region-main').find(class_='region-name').find(class_='region-details')
        print(oblast_menu.text.strip())


if __name__ == "__main__":
    parcing("https://www.tomato-pizza.ru/")
