import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Stock Market Analysis", layout="wide")
st.title("📈 Stock Market Analysis App")

# Sidebar - Inputs
st.sidebar.header("User Options")
symbol = st.sidebar.text_input(
    "Stock Ticker Symbol", value="AAPL", help="Example: AAPL, TSLA, RELIANCE.NS"
)
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("today"))

# Download Data Functionality
@st.cache_data
def load_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    return data


data = load_data(symbol, start_date, end_date)

if data.empty:
    st.error("No data found! Please check the symbol or dates.")
else:
    # Sidebar Navigation Menu
    menu = [
        "1. Download Stock Data",
        "2. Show Data",
        "3. Closing Price Graph",
        "4. Moving Average Chart",
        "5. Volume Chart",
        "6. Stock Summary",
    ]
    choice = st.sidebar.selectbox("Select Analysis Option", menu)

    # 1. Download Option
    if choice == "1. Download Stock Data":
        st.subheader(f"Raw Data for {symbol}")
        st.success("Data loaded successfully!")
        st.dataframe(data, use_container_width=True)

    # 2. Show Data
    elif choice == "2. Show Data":
        st.subheader("Data Preview (First 10 Rows)")
        st.dataframe(data.head(10), use_container_width=True)

    # 3. Closing Price Graph
    elif choice == "3. Closing Price Graph":
        st.subheader(f"{symbol} - Closing Price")
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(data["Close"], label="Close Price", color="blue")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        ax.legend()
        st.pyplot(fig)

    # 4. Moving Average
    elif choice == "4. Moving Average Chart":
        st.subheader("20-Day & 50-Day Moving Average")
        data_ma = data.copy()
        data_ma["MA20"] = data_ma["Close"].rolling(20).mean()
        data_ma["MA50"] = data_ma["Close"].rolling(50).mean()

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(data_ma["Close"], label="Close Price", alpha=0.5)
        ax.plot(data_ma["MA20"], label="20 Day MA", color="orange")
        ax.plot(data_ma["MA50"], label="50 Day MA", color="green")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        ax.legend()
        st.pyplot(fig)

    # 5. Volume Plot
    elif choice == "5. Volume Chart":
        st.subheader(f"{symbol} - Trading Volume")
        if "Volume" in data.columns:
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(data.index, data["Volume"], label="Volume", color="purple")
            ax.set_xlabel("Date")
            ax.set_ylabel("Volume")
            ax.legend()
            st.pyplot(fig)
        else:
            st.warning("Volume data not available.")

    # 6. Stock Summary
    elif choice == "6. Stock Summary":
        st.subheader("Stock Key Metrics")
        col1, col2, col3, col4 = st.columns(4)

        high_val = float(data["High"].max())
        low_val = float(data["Low"].min())
        avg_close = float(data["Close"].mean())
        tot_vol = int(data["Volume"].sum())

        col1.metric("Highest Price", f"${high_val:.2f}")
        col2.metric("Lowest Price", f"${low_val:.2f}")
        col3.metric("Avg Closing Price", f"${avg_close:.2f}")
        col4.metric("Total Volume", f"{tot_vol:,}")
