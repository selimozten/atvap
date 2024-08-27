# Data Fetching and Preprocessing

## Data Source

Our project fetches cryptocurrency trading data using the CCXT library, which provides a unified interface to interact with various cryptocurrency exchanges. The specific exchange, trading pair, and timeframe are configurable in the `config.yml` file.

## Data Fetching Process

1. **Exchange Connection**: We use the CCXT library to connect to the specified exchange. The exchange name is read from the configuration file.

2. **OHLCV Data Retrieval**: We fetch OHLCV (Open, High, Low, Close, Volume) data for the specified trading pair and timeframe. The `fetch_ohlcv` method of CCXT is used for this purpose.

3. **Data Conversion**: The fetched data is converted into a pandas DataFrame for easier manipulation and analysis.

## Data Structure

The fetched data is structured as follows:

- **Timestamp**: The start time of each candlestick period
- **Open**: The opening price for the period
- **High**: The highest price during the period
- **Low**: The lowest price during the period
- **Close**: The closing price for the period
- **Volume**: The trading volume during the period

## Preprocessing Steps

1. **Timestamp Conversion**: The timestamp is converted from Unix time (milliseconds) to a pandas datetime object.

2. **Data Normalization**: (Note: This step is not currently implemented in the provided code, but it's recommended)
   - Consider normalizing the volume data to a standard scale (e.g., 0 to 1) to help the LSTM model learn more effectively.
   - You might use techniques like Min-Max scaling or Standard scaling.

3. **Sequence Creation**: The volume data is reshaped into sequences for input to the LSTM model. Each sequence consists of `look_back` number of past volumes, and the target is the volume of the next period.

## Data Split

While not explicitly shown in the current code, it's important to split your data into training, validation, and test sets. A common split might be:
- 70% for training
- 15% for validation
- 15% for testing

## Potential Enhancements

1. **Additional Features**: Consider incorporating other relevant features such as price data, market indicators, or even external data sources.

2. **Data Augmentation**: Implement techniques to augment your dataset, which could help in improving model generalization.

3. **Anomaly Detection**: Implement methods to detect and handle anomalies or outliers in the volume data.

4. **Missing Data Handling**: Develop strategies to handle any missing data points in the fetched data.

For implementation details, please refer to the `data_fetcher.py` and `utils.py` files in the project root directory.