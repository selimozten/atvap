# Installation Guide

Follow these steps to set up the ATVaP project on your local machine.

## Prerequisites

- Python 3.8+
- TensorFlow 2.4+
- pandas
- numpy
- ccxt
- matplotlib (for visualization)

## Installation Steps

1. Clone this repository:
   ```
   git clone https://github.com/selimozten/atvap.git
   ```

2. Navigate to the project directory:
   ```
   cd atvap
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

Proceed to the [Usage Section](usage.md) to start running the analysis.
