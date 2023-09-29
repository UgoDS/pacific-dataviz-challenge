import pandas as pd
import numpy as np
from scipy.stats import linregress


def agg_by_year(df_fruits: pd.DataFrame):
    return df_fruits.groupby(by=["annee"], as_index=False).agg(
        avg_price_year=pd.NamedAgg(column="valeur_moy", aggfunc=lambda x: np.mean(x))
    )


def compute_trend(df_fruit_agg: pd.DataFrame):
    x = df_fruit_agg.annee.values
    y = df_fruit_agg.avg_price_year.values
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    print("slope: %f, intercept: %f" % (slope, intercept))
    print("R-squared: %f" % r_value**2)
    return slope, intercept, r_value**2, p_value, std_err
