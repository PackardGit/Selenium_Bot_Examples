from selenium import webdriver


class Driver:
    """ General Driver class"""
    def __init__(self, url, path_to_driver, implicitly_wait):
        self.path_to_driver = path_to_driver
        self.driver = webdriver.Chrome(self.path_to_driver)
        self.url = url
        self.driver.implicitly_wait(implicitly_wait)
