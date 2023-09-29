import pandas as pd
import calendar


def cast_fruit_datetime_cols(df_fruits: pd.DataFrame):
    # Cast columns
    list_col_to_cast = ["annee", "mois"]
    for col in list_col_to_cast:
        df_fruits[col] = df_fruits[col].astype(int)
    df_fruits["mois_nom"] = df_fruits["mois"].map(lambda x: calendar.month_name[x])
    return df_fruits


def check_valeur_moy(df_fruits: pd.DataFrame):
    # Check valeur_moy column
    df_fruits["calculated_value"] = (
        df_fruits["valeur_tot_mg_fr"] / df_fruits["poids_mg_kg"]
    )
    df_fruits["pb_value"] = df_fruits["valeur_moy"] - df_fruits["calculated_value"]
    if df_fruits[df_fruits["pb_value"] != 0].shape[0] > 0:
        print("There might be an error in the data")
        print(df_fruits[df_fruits["pb_value"] != 0])
    return df_fruits


def remove_2023(df_fruit: pd.DataFrame):
    return df_fruit[df_fruit["annee"] != 2023]
