import streamlit as st

st.set_page_config("Pacific Challenge", ":rocket:", layout="wide")

st.header("🌏 Pacific Dataviz Challenge - Food")

st.subheader("Rational")
st.text('I have discovered the challenge the ⏰ 29th of september... I have just arrived on "le Caillou". ')
st.text("It is great opportunity to highlight what can be done using [Streamlit](https://streamlit.io/) and all the great Python Viz tools.")
st.text("Considering the lack of time, I have decided to tackle the 'easiest topics'. I would have loved to play with shapefile...")

st.subheader("Topics")
st.text("""I have mainly consider to topics:
        - The first one about the **Fruit and Vegetables**: I wanted to highlight the inflation and the seasonnality effects
        - A second one about the famous **'pouvoir d achat'**: Considering a grocery list, where is it cheaper to go?""")

st.subheader("Technical infos")
st.text("Everything is coded using Python, all the graph are generated with [Plotly](https://plotly.com/) or [PyEcharts](https://pyecharts.org/#/).")
st.text("The data are provided to the app using API calls. Nothing is stored, I just use cache.")
st.text("The project is available on my [Github](https://github.com/UgoDS/pacific-dataviz-challenge) and has been deployed using Streamlit Hub.")
