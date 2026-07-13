import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet


st.set_page_config(
    page_title="Brent Oil Forecast",
    layout="wide"
)


st.title("📈 Brent Oil Price Forecast Dashboard")


# =============================
# Load Data
# =============================

brent = pd.read_csv(
    "Datasets/Brent Oil (1).csv"
)



# =============================
# Rename Columns for Prophet
# =============================

brent.rename(
    columns={
        "Date": "ds",
        "Value": "y"
    },
    inplace=True
)



# Convert Date column

brent["ds"] = pd.to_datetime(
    brent["ds"]
)



# Sort data

brent = brent.sort_values(
    "ds"
)



# Remove missing values

brent = brent.dropna(
    subset=["ds", "y"]
)



# =============================
# Current Price
# =============================

current_price = brent.iloc[-1]["y"]



# =============================
# Dashboard Metrics
# =============================

col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Current Brent Oil Price",
        f"{current_price:.2f}"
    )


with col2:

    st.metric(
        "Records",
        len(brent)
    )


with col3:

    st.metric(
        "Start Year",
        brent["ds"].dt.year.min()
    )



st.divider()



# =============================
# Historical Chart
# =============================

st.subheader(
    "📊 Historical Brent Oil Prices"
)


fig = px.line(
    brent,
    x="ds",
    y="y",
    title="Historical Brent Oil Price Trend"
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
    brent
)



# =============================
# Forecast for 2027
# =============================

future = model.make_future_dataframe(
    periods=365
)


forecast = model.predict(
    future
)



forecast_date = forecast.iloc[-1]["ds"]


forecast_price = forecast.iloc[-1]["yhat"]



# Calculate Change

change = (
    (forecast_price - current_price)
    /
    current_price
) * 100



# =============================
# AI Recommendation
# =============================

st.subheader(
    "🤖 AI Investment Recommendation"
)



if change > 5:

    recommendation = "🟢 BUY"

    reason = (
        "The AI model predicts an increase "
        "in Brent oil prices by 2027."
    )


elif change < -5:

    recommendation = "🔴 SELL"

    reason = (
        "The AI model predicts a decline "
        "in Brent oil prices by 2027."
    )


else:

    recommendation = "🟠 HOLD"

    reason = (
        "The AI model predicts stable "
        "Brent oil price movement."
    )



st.metric(
    "Recommendation",
    recommendation
)



st.info(
f"""
### Forecast Summary

- **Current Brent Oil Price:** {current_price:.2f}

- **Forecast Date:** {forecast_date.strftime('%d %B %Y')}

- **Predicted Price:** {forecast_price:.2f}

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
    "Current Brent Oil Price",
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