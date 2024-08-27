# Advanced Crypto Trade Volume Analysis and Prediction

## Overview

This project implements an advanced system for analyzing and predicting cryptocurrency trading volumes using LSTM neural networks. It's designed to provide our exchange with insights into future market activity, helping to optimize resources and improve trading strategies.

## Features

- Real-time data fetching from our exchange API
- LSTM-based deep learning model for volume prediction
- Customizable timeframes and cryptocurrencies
- Visualization tools for analysis results

## Prerequisites

- Python 3.8+
- TensorFlow 2.4+
- pandas
- numpy
- ccxt
- matplotlib (for visualization)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/selimozten/atvap.git
   ```

2. Navigate to the project directory:
   ```
   cd crypto-volume-analysis
   ```

3. Create a virtual environment:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`

5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

6. Copy the `config.example.yml` file to `config.yml` and fill in your API credentials:
   ```
   cp config.example.yml config.yml
   ```

## Usage

1. To run the main analysis script:
   ```
   python main.py
   ```

2. To customize the analysis, edit the parameters in `config.yml`:
   - `exchange`: The exchange to fetch data from (default: our internal exchange)
   - `symbol`: The trading pair to analyze (e.g., "BTC/USDT")
   - `timeframe`: The candlestick timeframe (e.g., "1h" for 1 hour)
   - `look_back`: The number of past periods to consider for prediction

3. To visualize results:
   ```
   python visualize.py
   ```

## Project Structure

- `main.py`: The main script for data fetching, model training, and prediction
- `data_fetcher.py`: Module for fetching and preprocessing data
- `model.py`: Definition of the LSTM model
- `utils.py`: Utility functions for data manipulation and analysis
- `visualize.py`: Script for generating visualizations of results
- `config.yml`: Configuration file for project parameters
- `tests/`: Directory containing unit tests

## Contributing

1. Create a new branch for your feature or bugfix:
   ```
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them with a descriptive message:
   ```
   git commit -am "Add new feature: your feature description"
   ```

3. Push your changes to the repository:
   ```
   git push origin feature/your-feature-name
   ```

4. Create a pull request in our internal GitLab/GitHub instance for review.

5. After review and approval, your changes will be merged into the main branch.

## Testing

To run the test suite:
```
python -m pytest tests/
```

Ensure all tests pass before submitting a pull request.

## Internal Documentation

For more detailed internal documentation, including API specifications and model architecture details, please refer to the `docs/` directory in this repository.

## Support

For any questions or issues, please contact the Data Science team or create an issue in this repository.
