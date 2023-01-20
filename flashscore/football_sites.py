from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from typing import Union, Literal
from logger import logger
import pandas as pd


class FlashscoreNavigator:
    """FlashscoreNavigator supports getting information from flashscore.pl site"""

    def __init__(self, path_to_driver="H:\ChromeDriver\chromedriver.exe", url="https://www.flashscore.pl"):
        self.path_to_driver = path_to_driver
        self.url = url
        self.driver = webdriver.Chrome(self.path_to_driver)
        # self.driver.get(self.url)
        self.chosen_league = False
        self.league_name = None
        self.table = []
        self.df = pd.DataFrame()

    def __del__(self):
        self.driver.quit()

    @logger
    def choose_league(self, league_name: Union[Literal["Premier League", "Ligue 1", "LaLiga", "Bundesliga", "Serie A",],
                                               None], locator=(By.CLASS_NAME, "leftMenu__item")):
        """Select league

        :param league_name: [str] values: "Premier League", "Ligue 1", "LaLiga", "Bundesliga", "Serie A"
        :param locator: identification of the menu with leagues
        """
        sleep(1)
        element = None
        self.league_name = league_name
        allowed_values = ["Premier League", "Ligue 1", "LaLiga", "Bundesliga", "Serie A"]
        self.driver.get(self.url)
        if self.league_name in allowed_values:
            elements = self.driver.find_elements(*locator)
            element = [el for el in elements if el.text == self.league_name][0]
            try:
                element.click()
                sleep(1)
                log_info = ["League : {} was successfully searched".format(self.league_name)]
                self.chosen_league = True
            except Exception as e:
                log_info = e
        else:
            log_info = ["This league: {} can not be searched".format(self.league_name)]

        return log_info, element

    @logger
    def select_table(self, locator=(By.ID, "li3")):
        """ Show table of selected league. Note: You must choose_league first

        :param locator: identification of the menu with leagues
        """
        sleep(1)
        element = None
        if self.chosen_league:
            try:
                element = self.driver.find_element(*locator)
                element.click()
                log_info = ["Table league for: {} was searched successfully".format(self.league_name)]
            except Exception as e:
                log_info = ["Invalid Locator"]
                print(e)
        else:
            log_info = ["Choose league first"]
        return log_info, element

    @logger
    def get_table(self, locator=(By.CLASS_NAME, "ui-table__row")):
        """ Show table of selected league. Note: You must choose_league first

        :param locator: identification of the menu with leagues
        """
        sleep(1)
        try:
            elements = self.driver.find_elements(*locator)
            for el in elements:
                self.table.append(el.text)
            log_info = ["Elements: {} was found successfully".format(elements)]
        except Exception as e:
            log_info = ["Invalid Locator"]
            print(e)
        return log_info, self.table

    @logger
    def port_table_to_pandas(self):
        """Transform Table to Pandas dictionary"""
        position = []
        team_name = []
        games = []
        wins = []
        drafts = []
        looses = []
        goals = []
        points = []
        last_match_1 = []
        last_match_2 = []
        last_match_3 = []
        last_match_4 = []
        last_match_5 = []
        table_2 = []
        for count, el in enumerate(self.table):
            a = el.split("\n")
            table_2.append(a)
            position.append(a[0])
            team_name.append(a[1])
            games.append(a[2])
            wins.append(a[3])
            drafts.append(a[4])
            looses.append(a[5])
            goals.append(a[6])
            points.append(a[7])
            last_match_1.append(a[9])
            last_match_2.append(a[10])
            last_match_3.append(a[11])
            last_match_4.append(a[12])
            last_match_5.append(a[13])

        self.df["Position"] = position
        self.df["Team"] = team_name
        self.df["Games"] = games
        self.df["Wins"] = wins
        self.df["Drafts"] = drafts
        self.df["Looses"] = looses
        self.df["Goals"] = goals
        self.df["Points"] = points
        self.df["Last_match_1"] = last_match_1
        self.df["Last_match_2"] = last_match_2
        self.df["Last_match_3"] = last_match_3
        self.df["Last_match_4"] = last_match_4
        self.df["Last_match_5"] = last_match_5

        log_info = ["Data frame was created"]

        return log_info, self.df
