import ccxt
import pandas as pd

class DataFetcher:
    def __init__(self, exchange, symbol, timeframe):
        self.exchange = getattr(ccxt, exchange)()
        self.symbol = symbol
        self.timeframe = timeframe

    def fetch_data(self):
        # Fetch OHLCV data
        ohlcv = self.exchange.fetch_ohlcv(self.symbol, self.timeframe)

        # Convert to DataFrame
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)

        return df