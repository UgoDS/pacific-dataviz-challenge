import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
from plotly.offline import plot


def create_radial_scatter(df: pd.DataFrame, col_value: str, add_legend: bool=False):
    fig = px.line_polar(
        df,
        r=col_value,
        theta="mois_nom",
        color="annee",
        color_discrete_sequence=px.colors.sequential.Plotly3,
        line_close=True,
        template="plotly_dark",
        line_shape="spline"
    )
    if add_legend:
        fig.update_layout(
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=1)
        )
    return fig


def make_custom_subplots(list_figs):
    fig = make_subplots(rows=1, 
                        cols=len(list_figs), 
                        specs=[[{"type": "scatterpolar"}, {"type": "scatterpolar"}]],
                        subplot_titles=["Price (FR/kg)", "Quantity (kg)"], ) 

    for i, figure in enumerate(list_figs):
        for trace in range(len(figure["data"])):
            fig.append_trace(figure["data"][trace], row=1, col=i+1)
    fig.update_layout(template="plotly_dark", width=1100, height=550)
    fig.update_annotations(y=1.1, selector={'text':'Price (FR/kg)'})
    fig.update_annotations(y=1.1, selector={'text':'Quantity (kg)'})
    fig.update_polars(angularaxis_rotation=90)

    
    return fig
