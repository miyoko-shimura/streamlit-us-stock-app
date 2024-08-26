# U.S. Stock Visualization App

This Streamlit app allows users to visualize the stock price of U.S. companies over a selected time period. It provides interactive candlestick charts and allows comparison with the S&P 500 index for performance benchmarking.

## Demo

Check out the live demo [https://stock-app-miyokoshimura.streamlit.app](https://stock-app-miyokoshimura.streamlit.app) 

## Features

- Visualize historical stock prices using candlestick charts.
- Compare individual stock performance with the S&P 500 index.
- Display metrics such as highest price, lowest price, and average closing price.
- Calculate and display the total return for the selected stock and the S&P 500.
- Interactive date range selection and stock symbol input.

## Installation

To run this app locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/us-stock-visualization-app.git
    cd us-stock-visualization-app
    ```

2. **Create a virtual environment (optional but recommended)**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    Create a `requirements.txt` file with the following contents:

    ```plaintext
    streamlit
    yfinance
    plotly
    pandas
    ```

    Then install the packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the app**:

    ```bash
    streamlit run app.py
    ```

    This will start a local Streamlit server and open the app in your default web browser.

## Usage

1. Enter a ticker symbol (e.g., `AAPL` for Apple, `NVDA` for NVIDIA, `MSFT` for Microsoft) in the input field.
2. Select a date range using the slider. You can choose a range up to 2 years.
3. Check the "Compare with S&P 500" option to compare the selected stock's performance with the S&P 500 index.
4. Click the "Show Stock Price" button to display the candlestick chart and performance metrics.


## Developer

Developed by [Miyoko Shimura](https://www.linkedin.com/in/miyoko-shimura/).

## Acknowledgments

- **[Streamlit](https://streamlit.io/)**: For providing a powerful and easy-to-use web application framework for data science.
- **[yfinance](https://pypi.org/project/yfinance/)**: For providing access to historical market data.
- **[Plotly](https://plotly.com/python/)**: For creating interactive and visually appealing charts.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
