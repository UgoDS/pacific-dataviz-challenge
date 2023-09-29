import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def create_radial_scatter(df: pd.DataFrame, col_value: str, add_legend: bool = False):
    fig = px.line_polar(
        df,
        r=col_value,
        theta="mois_nom",
        color="annee",
        color_discrete_sequence=px.colors.sequential.Plotly3,
        line_close=True,
        template="plotly_dark",
        line_shape="spline",
    )
    if add_legend:
        fig.update_layout(
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=1)
        )
    return fig


def make_custom_subplots(list_figs):
    fig = make_subplots(
        rows=1,
        cols=len(list_figs),
        specs=[[{"type": "scatterpolar"}, {"type": "scatterpolar"}]],
        subplot_titles=["Price (FR/kg)", "Quantity (kg)"],
    )

    for i, figure in enumerate(list_figs):
        for trace in range(len(figure["data"])):
            fig.append_trace(figure["data"][trace], row=1, col=i + 1)
    fig.update_layout(template="plotly_dark", width=1100, height=550)
    fig.update_annotations(y=1.1, selector={"text": "Price (FR/kg)"})
    fig.update_annotations(y=1.1, selector={"text": "Quantity (kg)"})
    fig.update_polars(angularaxis_rotation=90, angularaxis_direction="clockwise")
    return fig


def plot_slops(dict_results: dict, nb_cols: int = 4):
    fig = go.Figure()
    fig = make_subplots(
        rows=len(dict_results) // nb_cols + 1,
        cols=nb_cols,
        subplot_titles=list(dict_results.keys()),
        shared_xaxes=True,
        print_grid=False,
    )
    for idx, (fruit, values) in enumerate(dict_results.items()):
        x = values[5]["annee"].astype(int).values
        y = values[5]["avg_price_year"].values
        slope = values[0]
        intercept = values[1]
        r2 = values[2]
        row = idx // nb_cols + 1
        col = idx % 4 + 1
        if slope / y[0] <= -0.05:
            color = "green"
        elif slope / y[0] >= 0.05:
            color = "red"
        else:
            color = "#ffe476"
        color
        fig.add_trace(
            go.Scatter(
                x=x,
                y=y,
                mode="lines",
                name="lines",
                opacity=0.3,
            ),
            row=row,
            col=col,
        )
        fig.add_trace(
            go.Scatter(
                x=x,
                y=intercept + slope * x,
                mode="lines+markers",
                name="lines+markers",
                line=dict(color=color),
            ),
            row=row,
            col=col,
        )
        fig.add_annotation(
            text=f"<i>R2: {round(r2, 2)}</i><br><i>Slope: {round(slope)}</i>",
            xref="paper",
            yref="paper",
            x=2018,
            y=max(y),
            showarrow=False,
            font=dict(size=10),
            row=row,
            col=col,
        )
    fig.update_layout(template="plotly_dark", height=2000, showlegend=False)

    return fig
