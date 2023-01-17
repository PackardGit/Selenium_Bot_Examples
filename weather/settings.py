from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys


class MyDriver:
    """WEB Driver initialization"""

    def __init__(self, url, path_to_driver="H:\ChromeDriver\chromedriver.exe"):
        self.path_to_driver = path_to_driver
        self.url = url
        self.driver = webdriver.Chrome(self.path_to_driver)
        self.driver.get(self.url)

    def __find_element(self, element_id):
        try:
            sleep(0.5)
            element = self.driver.find_element(*element_id)
            print("---> Element {} has been found\n".format(element_id))
            sleep(2)
            return element
        except Exception as e:
            print("[Error] Could not find {}\n".format(element_id))
            # print(e)
            return None

    def title(self):
        print("---> Site Title: {}\n".format(self.driver.title))

    def use_searchbar(self, search_word, element_id):
        search_bar = self.__find_element(element_id)
        if search_bar:
            try:
                search_bar.send_keys(search_word)
                sleep(2)
                search_bar.send_keys(Keys.RETURN)
                print("---> Word '{}' was successfully searched using {}\n".format(search_word, element_id))
            except Exception as e:
                print("[Error] Could not use searchbar\n")
                # print(e)
        else:
            print("Something went wrong. Word was not searched\n")

    def get_text_value_from_element(self, element_id):
        element = self.__find_element(element_id)
        print("---> Searched text value: {}".format(element.text))
        return element.text



