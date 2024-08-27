# LSTM Model for Crypto Trading Volume Prediction

## Introduction to LSTM

Long Short-Term Memory (LSTM) networks are a type of recurrent neural network (RNN) architecture designed to model temporal sequences and their long-range dependencies more accurately than conventional RNNs. In our project, we use LSTM to predict cryptocurrency trading volumes based on historical data.

## Model Architecture

Our LSTM model consists of the following layers:

1. **LSTM Layer**: This is the core of our model. It processes the input sequence and captures temporal dependencies.
   - Units: 50
   - Activation: ReLU (Rectified Linear Unit)
   - Input Shape: (look_back, 1), where look_back is the number of past time steps to consider

2. **Dense Layer**: This is the output layer that produces the final prediction.
   - Units: 1 (since we're predicting a single value - the trading volume)

## Model Parameters

- **look_back**: This parameter determines how many past time steps the model considers when making a prediction. It's set in the `config.yml` file and can be adjusted based on the specific requirements of the analysis.

## Training Process

The model is trained using the following settings:

- **Optimizer**: Adam
- **Loss Function**: Mean Squared Error (MSE)
- **Epochs**: 100 (default, can be adjusted)
- **Batch Size**: 32 (default, can be adjusted)

## Input Data

The model expects input data in the shape (n_samples, look_back, 1), where:
- n_samples is the number of training examples
- look_back is the number of past time steps to consider
- 1 represents the single feature we're using (volume)

## Output

The model outputs a single value representing the predicted trading volume for the next time step.

## Potential Improvements

1. **Feature Engineering**: Incorporate additional features such as price data, moving averages, or technical indicators.
2. **Hyperparameter Tuning**: Use techniques like grid search or random search to optimize the model's hyperparameters.
3. **Ensemble Methods**: Combine the LSTM model with other types of models to potentially improve prediction accuracy.
4. **Attention Mechanism**: Implement an attention layer to help the model focus on the most relevant parts of the input sequence.

For implementation details, please refer to the `model.py` file in the project root directory.