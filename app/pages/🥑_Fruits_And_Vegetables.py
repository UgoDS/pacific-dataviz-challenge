import streamlit as st
from app.plots.fruits_graph import (
    create_radial_scatter,
    make_custom_subplots,
    plot_slops,
)
from app.utils.data_loader import get_all_fruits_trends, get_fruit_data
from app.utils.display import align_caption
from src.data.clean_dataset import (
    check_valeur_moy,
    cast_fruit_datetime_cols,
    remove_2023,
)
from models.fruits import LIST_FRUITS
from src.data.preprocessing import compute_trend, agg_by_year

st.set_page_config("Pacific Challenge", ":rocket:", layout="wide")

st.title("Fruits and Vegetables visualizations")

st.divider()

with st.expander("1 - Overall trends among all products"):
    with st.form("Get trends for all products"):
        submitted = st.form_submit_button("Launch Data collection")

    if submitted:
        all_fruits_trends = get_all_fruits_trends()
        st.subheader("Price evolution by product over the last 10 years")
        cols = st.columns([2, 1, 2])
        cols[0].markdown("<h5>How to read the viz</h5>", unsafe_allow_html=True)
        cols[0].markdown("Each product is represented by a **trend line**.")
        cols[0].markdown("If the trend goes up, it means the price has increased.")
        cols[0].markdown(
            "The **R2 coefficient** is a proxy of accuracy of this trend. The nearest it is from 1 the best it is."
        )
        cols[0].markdown(
            "The **slope** is the average price evolution by year in FR/year."
        )
        cols[2].markdown("<h5>Legend</h5>", unsafe_allow_html=True)
        cols[2].markdown(
            '<span style="color:red">Price is **raising**</span>',
            unsafe_allow_html=True,
        )
        cols[2].markdown(
            '<span style="color:#ffe476">Price is **stable**</span>',
            unsafe_allow_html=True,
        )
        cols[2].markdown(
            '<span style="color:green">Price is **decreasing**</span>',
            unsafe_allow_html=True,
        )

        all_fruits_trends_filtered = {
            fruit: values
            for fruit, values in all_fruits_trends.items()
            if values[0] == values[0]
        }
        st.plotly_chart(
            plot_slops(all_fruits_trends_filtered), use_container_width=True
        )

with st.expander("2 - Highlight the price evolution by product"):
    selected_fruit = st.selectbox("Pick a fruit", LIST_FRUITS, index=1)
    df_fruits = (
        get_fruit_data(selected_fruit)
        .pipe(cast_fruit_datetime_cols)
        .pipe(check_valeur_moy)
        .pipe(remove_2023)
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
