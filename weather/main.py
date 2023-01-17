from settings import MyDriver
from website import WebSettings
from selenium.webdriver.common.by import By


class City:

    def __init__(self, city_name, temperature):
        self.city_name = city_name
        self.temperature = temperature

    def __str__(self):
        return "In {} Temperature: {}".format(self.city_name, self.temperature)

    def __add__(self, other):
        avg_temp = (int(self.temperature.split("°")[0]) + int(other.temperature.split("°")[0]))/2
        return "Average temperature in {} and {} is {}°C".format(self.city_name, other.city_name, avg_temp)


my_website = WebSettings(url="https://pogoda.interia.pl", search_bar=(By.ID, "weather-currently-input-text-1"))
my_driver = MyDriver(url=my_website.url)

my_driver.title()
my_driver.use_searchbar("Katowice", my_website.search_bar)
temp = my_driver.get_text_value_from_element((By.CLASS_NAME, "weather-currently-temp-strict"))
Katowice = City("Katowice", temp)
temp2 = int(temp.split("°")[0])

my_driver.use_searchbar("Kielce", my_website.search_bar)
temp = my_driver.get_text_value_from_element((By.CLASS_NAME, "weather-currently-temp-strict"))
Kielce = City("Kielce", temp)

print(Katowice)
print(Kielce)
print(Katowice + Kielce)



