# Usage Guide

Learn how to use the ATVaP system for analyzing and predicting cryptocurrency trading volumes.

## Running the Analysis

1. To run the main analysis script:
   ```
   python main.py
   ```

2. Customize the analysis by editing the parameters in `config.yml`:
   - `exchange`: The exchange to fetch data from (default: our internal exchange)
   - `symbol`: The trading pair to analyze (e.g., "BTC/USDT")
   - `timeframe`: The candlestick timeframe (e.g., "1h" for 1 hour)
   - `look_back`: The number of past periods to consider for prediction

3. To visualize results:
   ```
   python visualize.py
   ```

For more detailed options, consult the [Project Structure](project-structure.md) section.
