import pandas as pd
from sklearn.linear_model import LinearRegression


def forecast_prices(data):
    """
    Forecast the price for 2027 using Linear Regression.
    """

    df = data.copy()

    # Convert dates to ordinal numbers
    df["DateOrdinal"] = pd.to_datetime(df["ds"]).map(pd.Timestamp.toordinal)

    X = df[["DateOrdinal"]]
    y = df["y"]

    model = LinearRegression()
    model.fit(X, y)

    # Predict for 1 January 2027
    future_date = pd.Timestamp("2027-01-01")
    future_ordinal = future_date.toordinal()

    predicted_price = model.predict([[future_ordinal]])[0]

    return model, future_date, predicted_price