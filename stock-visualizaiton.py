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
    
    # Display developer name in smaller font size
    st.markdown('<small>Developed by: <a href="https://www.linkedin.com/in/miyoko-shimura/" target="_blank">Miyoko Shimura</a></small>', unsafe_allow_html=True)
    st.markdown('  ')
    
    # User input
    stock_symbol = st.text_input('Enter a ticker symbol (e.g., AAPL for Apple, NVDA for NVIDIA, MSFT for Microsoft):', 'AAPL')
    
    # Date range selection using slider
    date_range = st.slider(
        "Select date range:",
        min_value=date.today() - timedelta(days=730),  # Set minimum value to 2 years ago
        max_value=date.today(),  # Set maximum value to today
        value=(date.today() - timedelta(days=365), date.today()),  # Default range set to last 1 year
        format="YYYY-MM-DD"
    )
    start_date, end_date = date_range

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

            # Summary with ticker symbol and date range in the header
            st.subheader(f'Summary for {stock_symbol} ({start_date} to {end_date})')
            highest_price = f"${df['High'].max():.2f}"
            lowest_price = f"${df['Low'].min():.2f}"
            average_closing_price = f"${df['Close'].mean():.2f}"
            
            st.write(f"**Highest Price:** {highest_price}")
            st.write(f"**Lowest Price:** {lowest_price}")
            st.write(f"**Average Closing Price:** {average_closing_price}")

            # Performance and Comparison with S&P 500
            stock_return = (df['Close'].iloc[-1] - df['Close'].iloc[0]) / df['Close'].iloc[0] * 100
            
            st.subheader('Comparison with S&P 500')
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label=f"Total Return ({stock_symbol})", value=f"{stock_return:.2f}%")

            if compare_sp500:
                sp500_return = (sp500_data.iloc[-1] - sp500_data.iloc[0]) / sp500_data.iloc[0] * 100
                relative_performance = stock_return - sp500_return

                with col2:
                    st.metric(label="S&P 500 Return", value=f"{sp500_return:.2f}%")
                with col3:
                    color = "green" if relative_performance >= 0 else "red"
                    relative_performance_str = f"+{relative_performance:.2f}%" if relative_performance >= 0 else f"{relative_performance:.2f}%"
                    st.metric(label="Relative Performance", value=relative_performance_str, delta_color=("normal" if relative_performance >= 0 else "inverse"))
            else:
                st.write("Enable 'Compare with S&P 500' to see more metrics")

if __name__ == "__main__":
    main()
