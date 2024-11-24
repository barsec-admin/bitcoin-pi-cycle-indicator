# Bitcoin Pi Cycle Top Indicator

Welcome to the Bitcoin Pi Cycle Top Indicator project! This tool helps you visualize and analyze the Bitcoin price in relation to the Pi Cycle Top Indicator without much overhead from you. Update the email fields and you will get an email if an indicator is found. What's an indicator? The Pi Cycle Top indicator is a valuable tool for identifying when the market is extremely overheated. This occurs when the short-term moving average—the 111-day moving average—reaches twice the value of the 350-day moving average. Historically, selling Bitcoin during these periods in its price cycles has been advantageous. When this happens, this script allows you to recieve an email.

However, it's important to note that this indicator has been effective mainly during Bitcoin's initial adoption phase, covering approximately the first 15 years of its existence. With the introduction of Bitcoin ETFs and its deeper integration into the global financial system, this indicator may eventually become less relevant in the evolving market landscape.

## Description

The Pi Cycle Top Indicator is a technical analysis tool used to identify potential market tops in the Bitcoin price cycle. This project provides a Python script to fetch Bitcoin price data, calculate the indicator, and email the results if the short-term moving average crosses 350-day average. The script will email you when it starts so you know its live and working.

## Usage

To use this tool, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```
3. Run the script:
   ```
   python bitcoin_pi_cycle_indicator.py
   ```

When an indicator happens, the script will generate and send an email showing the Bitcoin Pi Cycle Top Indicator.

## Data Source

This project uses historical Bitcoin price data from [CoinGecko](https://www.coingecko.com/), a reliable source for cryptocurrency market data.

## Note

Remember that the Pi Cycle Top Indicator is just one of many tools used in technical analysis. Always do your own research and consider multiple factors when making investment decisions.

Happy analyzing!
