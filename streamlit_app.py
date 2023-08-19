import streamlit
import pandas

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
streamlit.multiselect('Pick some fruits:' , list(my_fruit_list.index))

#display on the page
streamlit.dataframe(my_fruit_list)

