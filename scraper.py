from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scraped_data = []


# Define Exoplanet Data Scrapping Method
def scrape():
    bright_star_table = soup.find("table",attrs={"class","wikitable"})
    table_body=bright_star_table.find('tbody')
    table_rows=table_body.find_all('tr')

    for row in table_rows:
        table_cols=row.find_all('td')
        print(table_cols)

        temp_list=[]

        for col_data in table_cols:
            data = col_data.text.strip()
            temp_list.append(data)
        
        scraped_data.append(temp_list)

   
scrape()


stars_data=[]

for i in range(0,len(scraped_data)):
    Star_names=scraped_data[i][1]
    Distance=scraped_data[i][3]
    Mass=scraped_data[i][5]
    Radius=scraped_data[i][6]
    Lum=scraped_data[i][7]

    required_data=[Star_names,Distance,Mass,Radius,Lum]
    stars_data.append(required_data)

def scrape_more_data(hyperlink):
    try:
        page=requests.get(hyperlink)
        soup=BeautifulSoup(page.content,"html.parser")
        temp_list=[]
        for tr_tag in soup.find_all("tr",attrs={"class":"fact_row"}):
            td_tags=tr_tag.find_all("td")
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div",attrs={"class":"value"})[0].contents[0])
                except:
                    temp_list.append("")
        new_planet_data.append(temp_list)
    except:
        time.sleep()
        scrape_more_data(hyperlink)


new_planet_df_1.drop(columns=['distance','mass','radius'])
new_planet_df_1.head()

final_planet_df.to_csv('final_scrapd_data.csv')
from google.colab import files
files.download('main.csv')

dropna('Luminosity')
axis=1

headers = ['Star_name','Distance','Mass','Radius','Lum']
star_df_1=pd.DataFrame(stars_data,columns=headers)
star_df_1.to_csv('scrap_data_csv',index=True, index_label="id")
        


