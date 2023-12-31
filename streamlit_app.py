import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title("My Parents Healthy Diner")
   
streamlit.header('BreakFast Menu')
streamlit.text("🍞 Iddli & Sambhar")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothiee")
streamlit.text('🐔 Hard-Boilded Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

## Provide and Option to select
##fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Apple', 'Avocado','Banana','Cantaloupe','Grapefruit','Grapes','Honeydew','Kiwifruit','Lemon','Lemon','Nectarine','Orange','Peach','Pear','Pineapple','Plums','Strawberries','Cherries','Tangerine','Watermelon'])
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),default=[0,1,2])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display on the page
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice )

### BEautify the json
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)


######################################################

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)


streamlit.header('Fruit Load List contains')
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.dataframe(my_data_row)
fruit_choice = streamlit.text_input('What fruit would you like to add?','Kiwi')
streamlit.write('Thanks for adding ', fruit_choice)

my_cur.execute("INSERT into fruit_load_list values ('from streamlit')")



