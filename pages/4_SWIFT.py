import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="SWIFT Currency Analysis",
    layout="wide"
)


st.title("💱 SWIFT Global Currency Analysis Dashboard")


# ----------------------------------------------------
# Load Dataset
# ----------------------------------------------------

swift = pd.read_csv(
    "Datasets/swift_currency_tracker_all_reports.csv"
)



# ----------------------------------------------------
# Clean Data
# ----------------------------------------------------

swift["value"] = pd.to_numeric(
    swift["value"],
    errors="coerce"
)


swift = swift.dropna(
    subset=["value"]
)



# Convert report month

swift["report_month"] = pd.to_datetime(
    swift["report_month"],
    errors="coerce"
)



# ----------------------------------------------------
# Aggregate Currency Data
# ----------------------------------------------------

currency_summary = (
    swift.groupby("currency_or_economy")["value"]
    .mean()
    .reset_index()
)



currency_summary = currency_summary.sort_values(
    "value",
    ascending=False
)



# ----------------------------------------------------
# KPI Cards
# ----------------------------------------------------

top_currency = currency_summary.iloc[0]


total_currencies = (
    currency_summary["currency_or_economy"]
    .nunique()
)



latest_report = (
    swift["report_month"]
    .max()
)



col1, col2, col3 = st.columns(3)



with col1:

    st.metric(
        "🏆 Top Currency",
        top_currency["currency_or_economy"]
    )



with col2:

    st.metric(
        "📈 Highest Share (%)",
        f"{top_currency['value']:.2f}%"
    )



with col3:

    st.metric(
        "💱 Total Currencies",
        total_currencies
    )



st.divider()



# ----------------------------------------------------
# Top 10 Currency Chart
# ----------------------------------------------------

st.subheader(
    "📊 Top 10 Global Payment Currencies"
)



top10 = currency_summary.head(10)



fig = px.bar(
    top10,
    x="currency_or_economy",
    y="value",
    text="value",
    title="Top 10 Currencies by Global Payment Share"
)



st.plotly_chart(
    fig,
    use_container_width=True
)



st.divider()



# ----------------------------------------------------
# Pie Chart
# ----------------------------------------------------

st.subheader(
    "🥧 Market Share Distribution"
)



fig2 = px.pie(
    top10,
    names="currency_or_economy",
    values="value",
    hole=0.45,
    title="Global Payment Share Distribution"
)



st.plotly_chart(
    fig2,
    use_container_width=True
)



st.divider()



# ----------------------------------------------------
# Monthly Currency Trend
# ----------------------------------------------------

st.subheader(
    "📈 Currency Usage Trend Over Time"
)



selected_currencies = st.multiselect(
    "Select currencies",
    currency_summary["currency_or_economy"].tolist(),
    default=currency_summary.head(5)["currency_or_economy"].tolist()
)



trend_data = (
    swift[
        swift["currency_or_economy"]
        .isin(selected_currencies)
    ]
    .groupby(
        [
            "report_month",
            "currency_or_economy"
        ]
    )["value"]
    .mean()
    .reset_index()
)



fig3 = px.line(
    trend_data,
    x="report_month",
    y="value",
    color="currency_or_economy",
    markers=True,
    title="Monthly SWIFT Currency Payment Share Trend"
)



st.plotly_chart(
    fig3,
    use_container_width=True
)



st.divider()



# ----------------------------------------------------
# Currency Ranking Table
# ----------------------------------------------------

st.subheader(
    "📋 Currency Ranking"
)



st.dataframe(
    currency_summary,
    use_container_width=True
)



st.divider()



# ----------------------------------------------------
# Insights
# ----------------------------------------------------

st.subheader(
    "💡 Key Insights"
)



st.success(
f"""
• Latest Report Available: **{latest_report.strftime('%B %Y')}**

• **{top_currency['currency_or_economy']}** has the highest average share in SWIFT global payments.

• The dataset contains **{total_currencies}** currencies/economies.

• The dashboard analyzes global payment dominance using SWIFT transaction data.

• The trend chart allows comparison of currency performance over different reporting months.
"""
)