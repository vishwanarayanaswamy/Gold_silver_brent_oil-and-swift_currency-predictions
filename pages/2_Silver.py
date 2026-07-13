import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet


st.set_page_config(
    page_title="Silver Forecast",
    layout="wide"
)


st.title("📈 Silver Price Forecast Dashboard")


# =============================
# Load Data
# =============================

silver = pd.read_csv(
    "Datasets/silver 100 years (1).csv"
)


# =============================
# Rename Columns for Prophet
# =============================

silver.rename(
    columns={
        "Date": "ds",
        "Value": "y"
    },
    inplace=True
)


# Convert Date column

silver["ds"] = pd.to_datetime(
    silver["ds"]
)


# Sort by date

silver = silver.sort_values(
    "ds"
)


# Remove missing values

silver = silver.dropna(
    subset=["ds", "y"]
)



# =============================
# Current Price
# =============================

current_price = silver.iloc[-1]["y"]



# =============================
# Dashboard Metrics
# =============================

col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "Current Silver Price",
        f"{current_price:.2f}"
    )


with col2:
    st.metric(
        "Records",
        len(silver)
    )


with col3:
    st.metric(
        "Start Year",
        silver["ds"].dt.year.min()
    )



st.divider()



# =============================
# Historical Chart
# =============================

st.subheader(
    "📊 Historical Silver Prices"
)


fig = px.line(
    silver,
    x="ds",
    y="y",
    title="Historical Silver Price Trend"
)


st.plotly_chart(
    fig,
    use_container_width=True
)



st.divider()



# =============================
# Train Prophet Model
# =============================

st.subheader(
    "🤖 Training AI Forecast Model"
)


model = Prophet()


model.fit(
    silver
)



# =============================
# Forecast 2027
# =============================

future = model.make_future_dataframe(
    periods=365
)


forecast = model.predict(
    future
)



forecast_date = forecast.iloc[-1]["ds"]


forecast_price = forecast.iloc[-1]["yhat"]



# Percentage Change

change = (
    (forecast_price - current_price)
    /
    current_price
) * 100



# =============================
# Recommendation
# =============================

st.subheader(
    "🤖 AI Investment Recommendation"
)



if change > 5:

    recommendation = "🟢 BUY"

    reason = (
        "The AI model predicts that silver prices "
        "may increase by 2027."
    )


elif change < -5:

    recommendation = "🔴 SELL"

    reason = (
        "The AI model predicts that silver prices "
        "may decrease by 2027."
    )


else:

    recommendation = "🟠 HOLD"

    reason = (
        "The AI model predicts a stable silver "
        "price movement."
    )



st.metric(
    "Recommendation",
    recommendation
)



st.info(
f"""
### Forecast Summary

- **Current Silver Price:** {current_price:.2f}

- **Forecast Date:** {forecast_date.strftime('%d %B %Y')}

- **Predicted Silver Price:** {forecast_price:.2f}

- **Expected Change:** {change:.2f}%


**Reason:** {reason}

"""
)



# =============================
# Forecast Metrics
# =============================

st.subheader(
    "🔮 AI Forecast for 2027"
)



col1, col2, col3 = st.columns(3)



col1.metric(
    "Current Silver Price",
    f"{current_price:.2f}"
)


col2.metric(
    "Predicted Price (2027)",
    f"{forecast_price:.2f}"
)


col3.metric(
    "Prediction Date",
    forecast_date.strftime("%d-%m-%Y")
)



st.divider()



# =============================
# Forecast Graph
# =============================

st.subheader(
    "📈 Forecast Graph"
)



fig2 = model.plot(
    forecast
)


st.pyplot(
    fig2
)