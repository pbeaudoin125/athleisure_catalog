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
    'How would you like to be contacted?', my_data_rows)

streamlit.write('You selected:', option2)
