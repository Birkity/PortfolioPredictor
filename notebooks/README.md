# 📈 Time Series Forecasting and Analysis for BND, SPY, and TSLA

This project involves analyzing and forecasting financial time series data for **BND (Vanguard Total Bond Market ETF)**, **SPY (S&P 500 ETF)**, and **TSLA (Tesla Inc.)** to aid in optimizing portfolio management strategies. This project is part of the Guide Me in Finance (GMF) Investments initiative, focusing on equipping trainees with skills in data preprocessing, model development, and financial trend analysis.

---

## 📁 Project Structure

```
.
├── data
│   ├── BND_data.csv              # BND historical data
│   ├── SPY_data.csv              # SPY historical data
│   └── TSLA_data.csv             # TSLA historical data
├── notebooks
│   ├── task_1.ipynb   # Main analysis and model training notebook
└── README.md                     # Project description and usage instructions
```

---

## 📊 Data Overview

The project uses historical data from **BND**, **SPY**, and **TSLA** ETFs. Each dataset contains the following columns:

- **Date**: Timestamp of the trading day
- **Open, High, Low, Close**: Daily stock prices
- **Adj Close**: Adjusted closing price (reflects corporate actions)
- **Volume**: Trading volume for the day

---

## 🧩 Project Workflow

### Step 0: Load Data

Using `pandas`, we load data from CSV files:

```python
import pandas as pd

BND_handler = pd.read_csv("../data/BND_data.csv")
SPY_handler = pd.read_csv("../data/SPY_data.csv")
TSLA_handler = pd.read_csv("../data/TSLA_data.csv")
```

### Step 1: Data Cleaning and Understanding

- **Data Summary**: Initial statistics for each dataset using `.describe()` to understand mean, standard deviation, min, max, and quartiles.
- **Missing Values**: Checked for missing values and filled them using linear interpolation for smooth time-series continuity.

```python
BND_handler = BND_handler.interpolate()
SPY_handler = SPY_handler.interpolate()
TSLA_handler = TSLA_handler.interpolate()
```

### Step 2: Data Normalization

To facilitate model training, we scaled the `Close` prices for each ETF using `MinMaxScaler`:

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

BND_handler['Close_Scaled'] = scaler.fit_transform(BND_handler[['Close']])
SPY_handler['Close_Scaled'] = scaler.fit_transform(SPY_handler[['Close']])
TSLA_handler['Close_Scaled'] = scaler.fit_transform(TSLA_handler[['Close']])
```

### Step 3: Exploratory Data Analysis (EDA)

Performed an initial exploration on each dataset:

- **Time-Series Plots**: Visualized `Close` prices over time to observe trends, seasonality, and volatility.
- **Distribution Analysis**: Examined the distribution of returns to understand the daily price movement volatility.
- **Correlation**: Checked correlations among ETFs for any interconnected trends.

### Step 4: Advanced Analysis

- **Volatility Analysis**: Calculated daily returns and standard deviation to measure risk.
- **Outlier Detection**: Detected anomalous price movements using interquartile range (IQR) analysis.
- **Time-Series Decomposition**: Separated each series into trend, seasonal, and residual components to identify underlying patterns.

### Step 5: Forecasting Model Development

#### Model Options:

1. **ARIMA/SARIMA**:

   - Created autoregressive models for each ETF, tuning parameters for best fit and accuracy.
   - Analyzed seasonality patterns using SARIMA for capturing cyclical behavior in SPY and BND.

2. **LSTM**:
   - Implemented an LSTM model to capture complex temporal dependencies in TSLA’s stock prices, which demonstrated more volatile behavior.

### Step 6: Evaluation

Evaluation metrics used:

- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**

These were used to assess the performance of the models and determine the best-fitting model for each ETF based on historical accuracy.

---

## 📊 Key Findings

1. **BND** showed steady growth with minimal volatility, making it suitable for low-risk portfolios.
2. **SPY** displayed moderate volatility, aligning with general market trends.
3. **TSLA** exhibited high volatility, indicative of its growth stock nature and higher associated risks.

### 📉 Volatility and Risk Analysis

- Calculated **Value at Risk (VaR)** and **Sharpe Ratio** for each ETF to understand the risk-reward tradeoff.
- Documented how different ETFs respond to market events, helping stakeholders make data-informed decisions.

### 📅 Seasonality and Trend Observations

- **BND** exhibited stable growth patterns with limited seasonal trends.
- **SPY** showed patterns reflective of broader economic cycles.
- **TSLA** demonstrated rapid, sometimes unpredictable changes tied to company performance and industry news.

---

## 📈 Portfolio Insights

Using forecasted trends:

- **Portfolio Optimization**: Suggested an optimal blend of assets based on risk tolerance.
- **Market Trends**: Visualized ETF performance alongside S&P500 trends, aiding investment decisions.

---

## 🛠️ Technologies Used

- **Python**: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`
- **Machine Learning Models**: ARIMA, SARIMA, LSTM
- **Forecasting Tools**: Time-Series Decomposition, EDA techniques

---

## ⚙️ Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Birkity/PortfolioPredictor.git
   ```
2. **Run the notebook**:
   Open `analysis_notebook.ipynb` in Jupyter Notebook or any Python notebook environment to execute the analysis.

---

## 📌 Project Goals

1. Understand and forecast ETF price movements.
2. Train models for predicting future prices to support portfolio management.
3. Equip users with analytical skills for financial time-series forecasting.

---

## 📢 Future Work

- **Explore additional features**: Incorporate economic indicators like interest rates and inflation.
- **Expand model complexity**: Test alternative deep learning architectures (e.g., GRU, Transformer-based models).
- **Interactive Dashboard**: Develop a visualization dashboard for real-time market insights.

---
