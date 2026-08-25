# 📈 Stock Market Visualizer & Technical Analyzer

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![yfinance](https://img.shields.io/badge/API-yfinance-green.svg)](https://pypi.org/project/yfinance/)
[![pandas](https://img.shields.io/badge/Library-Pandas-150458.svg)](https://pandas.pydata.org/)
[![matplotlib](https://img.shields.io/badge/Library-Matplotlib-11557c.svg)](https://matplotlib.org/)

An end-to-end Python command-line utility for real-time financial data extraction, statistical aggregation, and multi-indicator technical charting. Built using `yfinance`, `pandas`, and `matplotlib`.

---

## 🎯 Key Architecture & Functionalities

* **Dynamic Data Retrieval:** Direct connection with Yahoo Finance API supporting global tickers (e.g., `AAPL`, `TSLA`, `RELIANCE.NS`).
* **Moving Average Convergence Analysis:** Built-in computation of 20-Day and 50-Day Simple Moving Averages (SMA) overlayed with historical close prices.
* **Volume Profile Tracking:** Trading volume visualization to identify liquidity spikes and accumulation/distribution trends.
* **Statistical Summary Engine:** Fast calculation of high/low price boundaries, arithmetic mean of closing prices, and total volume traded.
* **Robust CLI Menu:** Interactive CLI workflow with comprehensive exception handling for empty datasets or invalid tickers.

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.8+ | Core logic & OOP structure |
| **Data Fetcher** | `yfinance` | Financial market data ingestion |
| **Data Engine** | `pandas` | Time-series processing & rolling window metrics |
| **Visualization** | `matplotlib` | Multi-line charting & graphic rendering |

---

## 🚀 Getting Started

### Prerequisites
Make sure Python 3.8+ is installed on your environment.

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/stock-market-analysis.git](https://github.com/your-username/stock-market-analysis.git)
   cd stock-market-analysis
