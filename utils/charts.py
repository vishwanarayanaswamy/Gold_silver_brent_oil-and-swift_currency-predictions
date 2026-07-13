import plotly.express as px
import plotly.graph_objects as go


def historical_chart(df, title):
    """
    Historical Price Chart
    """

    fig = px.line(
        df,
        x="ds",
        y="y",
        title=title,
        markers=True
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Price",
        template="plotly_white",
        height=500
    )

    return fig


def regression_chart(df, title):
    """
    Historical vs Linear Regression Trend
    """

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["ds"],
            y=df["y"],
            mode="lines",
            name="Actual Price"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["ds"],
            y=df["Prediction"],
            mode="lines",
            name="Linear Regression"
        )
    )

    fig.update_layout(
        title=title,
        xaxis_title="Date",
        yaxis_title="Price",
        template="plotly_white",
        height=500
    )

    return fig