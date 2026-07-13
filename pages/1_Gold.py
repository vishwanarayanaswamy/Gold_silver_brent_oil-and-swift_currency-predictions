import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet

st.set_page_config(page_title="Gold Forecast", layout="wide")

st.title("📈 Gold Price Forecast Dashboard")

# Load Data
gold = pd.read_csv("Datasets/Gold_Clean.csv")
gold["ds"] = pd.to_datetime(gold["ds"])

# Current Price
current_price = gold.iloc[-1]["y"]

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Current Gold Price", f"{current_price:.2f}")

with col2:
    st.metric("Records", len(gold))

with col3:
    st.metric("Start Year", gold["ds"].dt.year.min())

st.divider()

# Historical Chart
st.subheader("📊 Historical Gold Prices")

fig = px.line(
    gold,
    x="ds",
    y="y",
    title="Historical Gold Price Trend"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# Train Prophet
model = Prophet()

model.fit(gold)

# Forecast for approximately one year (365 days)
future = model.make_future_dataframe(periods=365)

forecast = model.predict(future)

forecast_date = forecast.iloc[-1]["ds"]
forecast_price = forecast.iloc[-1]["yhat"]

change = ((forecast_price-current_price)/current_price)*100

# Recommendation

st.subheader("🤖 AI Investment Recommendation")

change = ((forecast_price - current_price) / current_price) * 100

if change > 5:
    recommendation = "🟢 BUY"
    reason = "The model predicts a significant increase in gold prices by 2027."

elif change < -5:
    recommendation = "🔴 SELL"
    reason = "The model predicts a significant decline in gold prices by 2027."

else:
    recommendation = "🟠 HOLD"
    reason = "The model predicts relatively stable gold prices by 2027."

st.metric("Recommendation", recommendation)

st.info(f"""
### Forecast Summary

- **Current Price:** {current_price:.2f}
- **Forecast Date:** {forecast_date.strftime('%d %B %Y')}
- **Predicted Price:** {forecast_price:.2f}
- **Expected Change:** {change:.2f}%

**Reason:** {reason}
""")

st.subheader("🔮 AI Forecast for 2027")

col1,col2,col3 = st.columns(3)

col1.metric(
    "Current Gold Price",
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

st.subheader("📈 Forecast Graph")

fig2 = model.plot(forecast)

st.pyplot(fig2)