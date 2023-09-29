import streamlit as st
from app.plots.fruits_graph import create_radial_scatter, make_custom_subplots, plot_slop
from app.utils.data_loader import get_fruit_data
from app.utils.display import align_caption
from src.data.clean_dataset import check_valeur_moy, cast_fruit_datetime_cols, remove_2023
from models.fruits import LIST_FRUITS
from src.data.preprocessing import compute_trend, agg_by_year

st.set_page_config("Pacific Challenge", ":rocket:", layout="wide")

st.title("Fruits and Vegetables visualizations")
st.subheader("Objectives")
st.text("1 - Highlight the price evolution by product")
st.text("2 - Overall trends among all products")
st.divider()
with st.expander("1 - Highlight the price evolution by product"):
    selected_fruit = st.selectbox("Pick a fruit", LIST_FRUITS, index=1)
    df_fruits = (
        get_fruit_data(selected_fruit).pipe(cast_fruit_datetime_cols).pipe(check_valeur_moy).pipe(remove_2023)
    )
    df_fruits_agg = agg_by_year(df_fruits)
    slope, intercept, r2_value, p_value, std_err = compute_trend(df_fruits_agg)

    st.subheader("Average price evolution by year")
    st.metric("Average Price Raise", f"{round(slope)} FR/year")
    st.caption(f"r2: {round(r2_value, 2)}, p_value: {round(p_value, 4)}")

    fig_value = create_radial_scatter(df_fruits, "valeur_moy")
    fig_quantity = create_radial_scatter(df_fruits, "poids_enquete_kg", True)
    fig = make_custom_subplots([fig_value, fig_quantity])
    st.plotly_chart(fig)
    cols = st.columns(2)
    align_caption(cols[0], "Highlight the price evolutions")
    align_caption(cols[1], "Highlight the seasonnality")


with st.expander("2 - Overall trends among all products"):
    with st.form("Launch calculation"):
        pass
