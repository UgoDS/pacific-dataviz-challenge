import pandas as pd
from kedro.extras.datasets.api import APIDataSet


def get_all_fruits(filter_name: str):
    nb_items_collected = 0
    nb_items_to_collect = 0
    chunk_size = 100
    list_items = []
    while nb_items_collected <= nb_items_to_collect:
        nb_items_to_collect, list_items = get_fruit_data_with_filter(
            list_items, filter_name, limit=chunk_size, offset=nb_items_collected
        )
        nb_items_collected += chunk_size
    return list_items


def get_fruit_data_with_filter(
    list_items: list, filter_name: str, limit: int = 100, offset: int = 0
):
    data_set = APIDataSet(
        url="https://data.gouv.nc/api/explore/v2.1/catalog/datasets/pacificdatavizchallenge_fruits_et_legumes_regroupement1/records",
        params={
            "select": "annee, mois, regroupement1, regroupement2, poids_enquete_kg, poids_mg_kg, valeur_tot_mg_fr, valeur_moy",
            "order_by": "annee, mois",
            "where": f'regroupement1 like "{filter_name}"',
            "limit": limit,
            "offset": offset,
        },
    )
    raw_result = data_set.load().json()
    nb_items = raw_result["total_count"]
    list_items += raw_result["results"]
    return nb_items, list_items


def transform_listdict_to_df(list_dict):
    return pd.DataFrame(list_dict)
