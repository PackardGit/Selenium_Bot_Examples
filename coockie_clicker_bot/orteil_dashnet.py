from selenium.webdriver.common.by import By
from general_driver.driver import Driver


class CookieDriver(Driver):
    """Wrapper for orteil.dashnet.org/cookieclicker website - bot which clicks cookies."""

    def __init__(self, url, path_to_driver="H:\ChromeDriver\chromedriver.exe", implicitly_wait=10):
        super().__init__(url, path_to_driver, implicitly_wait)
        self.cookies_counter = 0

    def __select_language(self):
        """Select language at initial opening"""
        try:
            lang_selection = self.driver.find_element(By.ID, "langSelect-PL")
            lang_selection.click()
        except Exception as e:
            print(e)
            pass

    def open_website(self):
        """Initialize website"""
        self.driver.get(self.url)
        self.__select_language()

    @property
    def cookies_number(self):
        """Number of collected cookies and cookies per second
        :return self.cookies counter: nr of cookies and cookies/sec"""
        self.cookies_counter = self.driver.find_element(By.ID, "cookies").text
        return self.cookies_counter

    def start_clicking_v1(self):
        """Simple game scenario to click cookies and buy upgrades"""
        cookie = self.driver.find_element(By.ID, "bigCookie")
        items = [self.driver.find_element(By.ID, "product" + str(i)) for i in range(18, -1, -1)]
        # current_item = items[18]
        i = 0
        while True:
            i += 1
            cookie.click()

            if i % 200 == 0:
                print("\n", self.cookies_number)
                for item in items:
                    if str(item.get_attribute("class")) in ["product unlocked enabled", "product unlocked disabled"]:
                        current_id = str(item.get_attribute("id"))
                        current_upgrade = self.driver.find_element(By.ID, current_id)
                        if item.get_attribute("class") == "product unlocked enabled":
                            current_upgrade.click()
                        break
