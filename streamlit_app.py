import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Zena\'s Amazing Athleisure Catalog')

option = streamlit.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

streamlit.write('You selected:', option)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select color_or_style from catalog_for_website")
my_data_rows = my_cur.fetchall()
my_cnx.close()

option2 = streamlit.selectbox(
    'Pick a sweatsuit color or style:', my_data_rows)

streamlit.write('You selected:', option2)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("select price from catalog_for_website where color_or_style = '" + option2 + "'" )
my_cur.execute("select price from catalog_for_website where color_or_style = 'Burgundy'" )
price = my_cur.fetchall()
my_cnx.close()
streamlit.write('Price:', price)

price_normalized = pandas.json_normalize(price.json())
streamlit.write('Price:', price_normalized)
