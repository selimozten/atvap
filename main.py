import yaml
from data_fetcher import DataFetcher
from model import LSTMModel
import utils

def load_config():
    with open('config.yml', 'r') as config_file:
        return yaml.safe_load(config_file)

def main():
    # Load configuration
    config = load_config()

    # Initialize data fetcher
    data_fetcher = DataFetcher(
        exchange=config['exchange'],
        symbol=config['symbol'],
        timeframe=config['timeframe']
    )

    # Fetch and preprocess data
    data = data_fetcher.fetch_data()
    X, y = utils.prepare_data(data, look_back=config['look_back'])

    # Initialize and train model
    model = LSTMModel(look_back=config['look_back'])
    model.train(X, y)

    # Make predictions
    predictions = model.predict(X[-1:])

    # Print results
    print(f"Predicted volume for next period: {predictions[0][0]}")

if __name__ == "__main__":
    main()