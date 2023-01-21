from football_sites import FlashscoreNavigator

league = "Serie A"

navi = FlashscoreNavigator()
navi.choose_league(league_name=league)
navi.select_table()

table = navi.get_table()

df = navi.port_table_to_pandas()
print(df)
df.to_excel("table.xlsx")
