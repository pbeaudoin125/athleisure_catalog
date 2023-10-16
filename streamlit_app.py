import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Zena\'s Amazing Athleisure Catalog')

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)
