import streamlit as st
from app.plots.fruits_graph import create_radial_scatter, make_custom_subplots
from app.utils.data_loader import get_fruit_data
from app.utils.display import align_caption
from src.data.clean_dataset import check_valeur_moy, cast_fruit_datetime_cols, remove_2023
from models.fruits import LIST_FRUITS

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
st.text("The project is available on my [Github]() and has been deployed using Streamlit Hub.")


selected_fruit = st.selectbox("Pick a fruit", LIST_FRUITS, index=1)
df_fruits = (
    get_fruit_data(selected_fruit).pipe(cast_fruit_datetime_cols).pipe(check_valeur_moy).pipe(remove_2023)
)
fig_value = create_radial_scatter(df_fruits, "valeur_moy")
fig_quantity = create_radial_scatter(df_fruits, "poids_enquete_kg", True)
fig = make_custom_subplots([fig_value, fig_quantity])
st.plotly_chart(fig)
cols = st.columns(2)
align_caption(cols[0], "Highlight the seasonnality")
align_caption(cols[1], "Highlight the price evolution")

