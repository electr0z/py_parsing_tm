from bs4 import BeautifulSoup
import undetected_chromedriver


def parcing(site):
    try:
        driver = undetected_chromedriver.Chrome()
        driver.get(site)

        html_main = driver.page_source
        soup = BeautifulSoup(html_main, 'lxml')
        massiv_content_container = soup.find(class_='main-content').find_all(class_='region')
        for element in massiv_content_container:
            # find_unerline = soup.find(class_="text-underline")
            # soup_element = BeautifulSoup(element.text, 'lxml')
            oblast_menu = element.find(class_='region-main').find(class_='region-cities').find_all(class_='text-underline')
            for menu in oblast_menu:
                str_menu = site[:-1] + menu.attrs['href']
                driver.get(str_menu)
                html_menu = driver.page_source
                soup_ = BeautifulSoup(html_menu, 'lxml')
                massiv_href_content = soup_.find(id_="navbar-nav mx-auto nav-submenu scroll_tabs_theme_tomato")
                test = 1
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    parcing("https://www.tomato-pizza.ru/")





