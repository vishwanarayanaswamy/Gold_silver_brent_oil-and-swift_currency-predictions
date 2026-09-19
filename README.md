# 📈 AI-Based Financial Market Forecasting & Recommendation System

A multi-page **Streamlit** dashboard that analyses long-run historical prices of **Gold, Silver and Brent Oil**, forecasts them with **Facebook Prophet**, and turns each forecast into a simple **BUY / HOLD / SELL** signal. A fourth page explores **SWIFT global currency tracker** data (payment share, rankings, trends).

🔗 **Live Demo:** [https://goldsilverbrentoil-and-swiftcurrency-predictions-fdu9ptadrrf8t.streamlit.app/](https://goldsilverbrentoil-and-swiftcurrency-predictions-fdu9ptadrrf8t.streamlit.app/)

> ⚠️ **Disclaimer:** This is an academic / educational project. Forecasts are based only on the bundled historical datasets and are **not financial advice**.

---

## ✨ Features

| Module | What it does |
|---|---|
| 🏠 **Home (`app.py`)** | Project overview, KPI cards and **live prices** for Gold, Silver and Brent (via Yahoo Finance) |
| 🥇 **Gold** | Historical trend chart, Prophet forecast to 2027, Buy/Hold/Sell recommendation, forecast plot |
| 🥈 **Silver** | Same pipeline as Gold, using silver price history |
| 🛢 **Brent Oil** | Same pipeline as Gold, using Brent crude price history |
| 💱 **SWIFT Currency Analysis** | Top-10 payment currencies (bar), market-share distribution (pie), currency usage trend over time (multi-select line chart), ranking table and auto-generated key insights |

### Recommendation logic

The predicted price at the end of the forecast horizon is compared with the latest price in the dataset:

| Expected change | Signal |
|---|---|
| **> +5 %** | 🟢 BUY |
| **between −5 % and +5 %** | 🟠 HOLD |
| **< −5 %** | 🔴 SELL |

---

## 🗂 Project Structure

```
├── app.py                     # Home page: overview + live market prices
├── clean_gold.py              # One-off script: cleans raw gold data -> Gold_Clean.csv
├── requirements.txt
├── Datasets/
│   ├── Gold 100years (1).csv                  # Raw gold prices (from 1915)
│   ├── Gold_Clean.csv                         # Cleaned gold data (ds, y) for Prophet
│   ├── gold_predictions.csv                   # Saved Prophet forecast output for gold
│   ├── silver 100 years (1).csv               # Silver prices (from 1915)
│   ├── Brent Oil (1).csv                      # Brent crude prices (from 1946)
│   └── swift_currency_tracker_all_reports.csv # SWIFT RMB / Global Currency Tracker data (Jan–Apr 2026 reports)
├── pages/
│   ├── 1_Gold.py
│   ├── 2_Silver.py
│   ├── 3_Brent_Oil.py
│   └── 4_SWIFT.py
└── utils/
    ├── live_prices.py         # Live prices via yfinance (GC=F, SI=F, BZ=F)
    ├── forecasting.py         # Linear-regression helper (forecast to 1 Jan 2027)
    ├── recommendation.py      # BUY / HOLD / SELL logic
    └── charts.py              # Reusable Plotly charts (historical, regression)
```

---

## 🧠 How It Works

1. **Load data** – historical CSVs from `Datasets/` (columns renamed to Prophet's `ds` / `y` format).
2. **Train** – a Prophet model is fitted on the full price history on page load.
3. **Forecast** – Prophet predicts future values via `make_future_dataframe`.
4. **Recommend** – the % change between the latest price and the forecast produces a Buy/Hold/Sell signal with a short reason.
5. **Visualise** – Plotly charts for history, Prophet's forecast plot for predictions, and Streamlit metrics for summaries.

The SWIFT page cleans the tracker CSV (numeric coercion, date parsing), aggregates by currency/economy, and renders interactive charts and insights.

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** – dashboard & multi-page navigation
- **Prophet** – time-series forecasting
- **scikit-learn** – linear regression helper
- **Pandas / NumPy** – data handling
- **Plotly** – interactive charts
- **yfinance** – live market prices

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/vishwanarayanaswamy/Gold_silver_brent_oil-and-swift_currency-predictions.git
cd Gold_silver_brent_oil-and-swift_currency-predictions
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> Prophet requires `cmdstanpy`; if the install fails, see the [Prophet installation guide](https://facebook.github.io/prophet/docs/installation.html).

### 4. (Optional) Regenerate the cleaned gold dataset

```bash
python clean_gold.py
```

### 5. Run the app

```bash
streamlit run app.py
```

Open the URL shown in the terminal (default: `http://localhost:8501`) and use the sidebar to switch between modules. Or try the [live demo](https://goldsilverbrentoil-and-swiftcurrency-predictions-fdu9ptadrrf8t.streamlit.app/).

---

## 📊 Datasets

| File | Content | Range |
|---|---|---|
| `Gold 100years (1).csv` | Gold price (`Date`, `Value`) | 1915 – 2026 |
| `silver 100 years (1).csv` | Silver price (`Date`, `Value`) | 1915 – 2026 |
| `Brent Oil (1).csv` | Brent crude price (`Date`, `Value`) | 1946 – 2026 |
| `swift_currency_tracker_all_reports.csv` | SWIFT RMB Tracker & Global Currency Tracker: global/international payment share, trade finance share, FX spot ranking, offshore RMB by economy, MoM growth | Reports Jan – Apr 2026 |

---

## ⚠️ Known Limitations

- Prophet is trained on price history alone – no macro-economic, geopolitical or sentiment features.
- Recommendations are threshold-based (±5 %) and are not backtested.
- Live prices depend on Yahoo Finance availability; the home page shows a warning if data can't be fetched.
- Models are re-trained each time a page loads, which can be slow on the full history.

---

## 🔮 Future Improvements

- Backtesting and model-evaluation metrics (MAE / RMSE / MAPE)
- Additional models (XGBoost, ARIMA / LSTM) and model comparison
- Cache trained models (`st.cache_data` / `st.cache_resource`) for faster page loads
- Forecasts for currencies and exchange rates, not just commodities

---

## 👤 Author

**Vishwa Narayanaswamy**
GitHub: [@vishwanarayanaswamy](https://github.com/vishwanarayanaswamy)

---

