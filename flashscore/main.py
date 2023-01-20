from football_sites import FlashscoreNavigator

league = "LaLiga"

navi = FlashscoreNavigator()
navi.choose_league(league)
navi.select_table()

table = navi.get_table()

df = navi.port_table_to_pandas()
df.to_excel("table.xlsx")
