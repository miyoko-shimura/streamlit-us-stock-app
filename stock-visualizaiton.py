import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import date, timedelta

def get_sp500_performance(start_date, end_date):
    sp500 = yf.Ticker("^GSPC")
    sp500_data = sp500.history(start=start_date, end=end_date)
    return sp500_data['Close']

def main():
    st.title('U.S. Stock Visualization App')

    # User input
    stock_symbol = st.text_input('Enter a ticker symbol (e.g., AAPL for Apple):', 'AAPL')
    
    # Date range selection
    start_date = st.date_input('Start date:', date.today() - timedelta(days=365))
    end_date = st.date_input('End date:', date.today())

    # S&P 500 comparison option
    compare_sp500 = st.checkbox('Compare with S&P 500')

    if st.button('Show Stock Price'):
        # Fetch data
        df = yf.download(stock_symbol, start=start_date, end=end_date)

        if df.empty:
            st.error('Unable to fetch data. Please check the ticker symbol.')
        else:
            # Create graph
            fig = go.Figure()
            fig.add_trace(go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'],
                name=stock_symbol))

            if compare_sp500:
                sp500_data = get_sp500_performance(start_date, end_date)
                fig.add_trace(go.Scatter(x=sp500_data.index, y=sp500_data, name='S&P 500', line=dict(color='red')))

            fig.update_layout(
                title=f'Stock Price Chart for {stock_symbol}',
                yaxis_title='Price (USD)',
                xaxis_title='Date'
            )

            st.plotly_chart(fig, use_container_width=True)

            # Display statistics
            st.subheader('Statistics')
            st.write(f"Highest price during period: ${df['High'].max():.2f}")
            st.write(f"Lowest price during period: ${df['Low'].min():.2f}")
            st.write(f"Average closing price: ${df['Close'].mean():.2f}")

            # Calculate performance
            total_return = (df['Close'].iloc[-1] - df['Close'].iloc[0]) / df['Close'].iloc[0] * 100
            st.write(f"Total return over period: {total_return:.2f}%")

            if compare_sp500:
                sp500_return = (sp500_data.iloc[-1] - sp500_data.iloc[0]) / sp500_data.iloc[0] * 100
                st.write(f"S&P 500 return: {sp500_return:.2f}%")
                st.write(f"Relative performance to S&P 500: {total_return - sp500_return:.2f}%")

if __name__ == "__main__":
    main()