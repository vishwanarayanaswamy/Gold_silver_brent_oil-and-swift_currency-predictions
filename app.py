import streamlit as st
from utils.live_prices import get_market_data


# ==============================
# Page Configuration
# ==============================

st.set_page_config(
    page_title="AI Financial Forecasting System",
    page_icon="📈",
    layout="wide"
)
st.sidebar.title("📊 Navigation")

st.sidebar.info("""
AI Financial Forecasting System

Developed using

• Streamlit

• Prophet

• Plotly

• Pandas
""")

# ==============================
# Sidebar
# ==============================




# ==============================
# Main Title
# ==============================

st.title("📈 AI-Based Financial Market Forecasting & Recommendation System")


st.markdown(
"""
Welcome to the **AI-Based Financial Market Forecasting & Recommendation System**.

This application combines:

• Historical commodity datasets  
• Machine Learning forecasting models  
• Investment recommendation analysis  

The system forecasts future commodity trends and provides market insights only based on dataset.
"""
)


st.divider()



# ==============================
# Project Overview Metrics
# ==============================

col1, col2, col3, col4 = st.columns(4)


col1.metric(
    label="📊 Datasets",
    value="4"
)

col2.metric(
    label="🤖 ML Models",
    value="1"
)

col3.metric(
    label="📈 Commodities",
    value="3"
)

col4.metric(
    label="💱 Currency Dataset",
    value="1"
)


st.divider()



# ==============================
# Live Market Prices
# ==============================

st.subheader("🟢 Latest Market Prices")


try:

    live_data = get_market_data()


    col1, col2, col3 = st.columns(3)


    with col1:

        gold = live_data["Gold"]["price"]

        st.metric(
            "🥇 Gold",
            f"${gold}"
        )


    with col2:

        silver = live_data["Silver"]["price"]

        st.metric(
            "🥈 Silver",
            f"${silver}"
        )


    with col3:

        oil = live_data["Brent Oil"]["price"]

        st.metric(
            "🛢 Brent Oil",
            f"${oil}"
        )


    st.caption(
        f"Last Updated: {live_data['Gold']['updated']}"
    )


except Exception as e:

    st.warning(
        "Live market data unavailable"
    )

    st.write(e)



st.divider()



# ==============================
# Available Modules
# ==============================

st.subheader("📂 Available Modules")


col1, col2 = st.columns(2)



with col1:


    st.info(
"""
📈 Gold Forecasting

Features:

• Historical Trend Analysis

• Future Price Prediction

• Buy / Hold / Sell Recommendation
"""
)



    st.info(
"""
🛢 Brent Oil Forecasting

Features:

• Historical Trend

• Future Prediction

• Market Recommendation
"""
)



with col2:


    st.info(
"""
🥈 Silver Forecasting

Features:

• Historical Trend

• Future Prediction

• Investment Signal
"""
)



    st.info(
"""
💱 SWIFT Currency Analysis

Features:

• Currency Trends

• Exchange Rate Charts

• Market Insights
"""
)



st.divider()



# ==============================
# Future Integration
# ==============================





