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

# 📊 **Fraud Detection and Portfolio Optimization**

Welcome to the **Fraud Detection and Portfolio Optimization** project! This project involves multiple tasks that combine machine learning, time series forecasting, and portfolio optimization techniques to analyze and forecast financial data. The project covers fraud detection and prediction, feature engineering, model training, and portfolio optimization based on market forecasts.

## 🌟 **Project Overview**

This project consists of three main tasks:

1. **Task 2**: **Exploratory Data Analysis (EDA)**:
   - Analyzing and visualizing financial data to understand the underlying patterns.
   - Identifying trends, outliers, and distributions for the datasets.
2. **Task 3**: **Time Series Forecasting & LSTM Models**:
   - Using LSTM (Long Short-Term Memory) models to forecast future stock prices.
   - Training models on multiple datasets and evaluating predictions.
3. **Task 4**: **Portfolio Optimization**:
   - Optimizing a sample investment portfolio using forecasted returns.
   - Applying the Sharpe Ratio to maximize risk-adjusted returns.

---

## 📚 **Task 2: Exploratory Data Analysis (EDA)**

### 🔍 **Objective**:

In this task, we perform an **Exploratory Data Analysis (EDA)** to gain insights into the financial data. We analyze three assets: Tesla (TSLA), Vanguard Total Bond Market ETF (BND), and S&P 500 ETF (SPY).

### 📈 **Steps Performed**:

- **Data Summary**: Reviewed the structure, central tendency, and distribution of the data.
- **Visualizations**:
  - Plotting distributions of numerical and categorical features.
  - Bivariate analysis to examine relationships between assets.
- **Correlation Analysis**:
  - Correlation matrices to identify relationships between assets.
- **Outlier Detection**:
  - Visualized outliers using box plots and histograms.

### 📊 **Key Results**:

- Summary statistics of returns for TSLA, BND, and SPY.
- Correlation and visualization insights for better asset selection.

---

## 🧠 **Task 3: Time Series Forecasting with LSTM**

### 🎯 **Objective**:

In this task, we use **LSTM models** (Long Short-Term Memory) to forecast future stock prices of **Tesla (TSLA)**, **Vanguard Total Bond Market ETF (BND)**, and **S&P 500 ETF (SPY)**. LSTM is a type of recurrent neural network that is ideal for time series forecasting.

### 🧑‍💻 **Steps Performed**:

1. **Data Preparation**:
   - Scaled the data and prepared it for the LSTM model using the `TimeseriesGenerator`.
   - Structured the data to predict future stock prices based on past data.
2. **Model Building**:
   - Built LSTM models with two layers and trained them on the scaled data.
   - Forecasted future stock prices for the next 30 days.
3. **Evaluation**:
   - Calculated performance metrics such as **Mean Absolute Error (MAE)**, **Root Mean Squared Error (RMSE)**, and **Mean Absolute Percentage Error (MAPE)** for the predictions.

### 📈 **Key Results**:

- Forecasted future prices for **TSLA**, **BND**, and **SPY**.
- Evaluated model performance using MAE, RMSE, and MAPE metrics.

### 🖼️ **Visualizations**:

- **Price Predictions**: Forecasted values are compared with actual values using line plots.
- **Error Metrics**: Visualization of model performance metrics.

---

## 💼 **Task 4: Portfolio Optimization**

### 🎯 **Objective**:

In this task, we use the forecasts from Task 3 to optimize a sample investment portfolio containing **TSLA**, **BND**, and **SPY**. The objective is to maximize returns while minimizing risks, using metrics like the **Sharpe Ratio**.

### 🧑‍💻 **Steps Performed**:

1. **Data Combination**:
   - Combined the forecasted data for TSLA, BND, and SPY into one dataframe.
2. **Returns and Volatility**:
   - Calculated **annual returns** and **daily volatility** for each asset.
3. **Covariance Matrix**:
   - Used a **covariance matrix** to understand the relationship between asset returns.
4. **Sharpe Ratio Optimization**:
   - Optimized portfolio weights to maximize the **Sharpe Ratio** (risk-adjusted returns).
5. **Risk Analysis**:
   - Calculated **Value at Risk (VaR)** and portfolio volatility.
   - Analyzed the potential loss at a 95% confidence interval.
6. **Optimization**:
   - Adjusted the portfolio allocation to minimize risks or maximize returns based on the forecasted trends.

### 📊 **Key Results**:

- **Optimized Portfolio Weights**: Calculated the best asset weights to maximize the Sharpe Ratio.
- **Portfolio Return & Volatility**: Assessed the expected return and risk.
- **Risk Metrics**: Measured **Value at Risk (VaR)** for Tesla stock and portfolio volatility.

### 📈 **Visualizations**:

- **Cumulative Return**: Visualized the cumulative return of the portfolio over time.
- **Risk-Return Analysis**: Risk-return scatter plot of different portfolio configurations.

---

## 🔧 **Installation & Setup**

To run this project, you'll need Python 3.x and the following libraries:

```bash
pip install numpy pandas matplotlib seaborn tensorflow scikit-learn yfinance
```

### **Steps to Run**:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/portfolio-optimization.git
   cd portfolio-optimization
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter notebook or Python scripts for each task:
   - Task 2: `EDA.ipynb`
   - Task 3: `time_series_forecasting.ipynb`
   - Task 4: `portfolio_optimization.ipynb`

---

## 📊 **Results & Insights**

The results from Task 3 and Task 4 can be used to:

- **Forecast Future Asset Prices**: Predict price trends and adjust portfolio allocations accordingly.
- **Optimize Portfolio Performance**: Use Sharpe Ratio optimization to maximize returns for the desired risk tolerance.

---

## 🤝 **Contributing**

If you'd like to contribute to this project, feel free to open issues, submit pull requests, or suggest improvements! You can contribute by:

- Adding new forecasting models.
- Improving the optimization algorithm.
- Enhancing visualizations or documentation.

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💬 **Contact**

For more information, please feel free to reach out to me at [your-email@example.com](mailto:your-email@example.com).

---

### ✨ **Acknowledgements**

This project uses several well-known machine learning libraries, such as `TensorFlow`, `scikit-learn`, and `pandas`, along with datasets from `yfinance` and other sources. Thanks to all contributors and authors of these tools.

---
