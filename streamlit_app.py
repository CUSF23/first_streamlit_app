import streamlit
import pandas
import requests


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

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

streamlit.header('Fruityvice Fruit Advice')
streamlit.text(fruityvice_response.json())
