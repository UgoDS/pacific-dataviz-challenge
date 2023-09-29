import streamlit as st
from src.data.data_manager import get_all_fruits, transform_listdict_to_df

from src.data.clean_dataset import (
    check_valeur_moy,
    cast_fruit_datetime_cols,
    remove_2023,
)
from models.fruits import LIST_FRUITS
from src.data.preprocessing import compute_trend, agg_by_year


def get_fruit_data(fruit_name: str):
    list_fruits = get_all_fruits(filter_name=fruit_name)
    return transform_listdict_to_df(list_fruits)


@st.cache_data
def get_all_fruits_trends():
    progress_text = "Collecting Data from data.gouv.nc"
    my_bar = st.progress(0, text=progress_text)
    dict_result = {}
    for idx, fruit in enumerate(LIST_FRUITS):
        df_fruits = (
            get_fruit_data(fruit)
            .pipe(cast_fruit_datetime_cols)
            .pipe(check_valeur_moy)
            .pipe(remove_2023)
        )
        df_fruits_agg = agg_by_year(df_fruits)
        slope, intercept, r2_value, p_value, std_err = compute_trend(df_fruits_agg)
        dict_result[fruit] = [
            slope,
            intercept,
            r2_value,
            p_value,
            std_err,
            df_fruits_agg,
        ]
        my_bar.progress(
            idx / len(LIST_FRUITS),
            text=f"{idx} items were collected, out of {len(LIST_FRUITS)}",
        )
    my_bar.empty()
    return dict_result
