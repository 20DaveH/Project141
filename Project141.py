from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"


# Convert to CSV
planet_df_1.to_csv('scrape_data.csv', index = True, index_label = "id") 


stars_data = []
headers = ["Name", "Distance", "Mass", "Radius"]