import numpy as np

def prepare_data(data, look_back):
    volumes = data['volume'].values
    X, y = [], []
    for i in range(len(volumes) - look_back):
        X.append(volumes[i:(i + look_back)])
        y.append(volumes[i + look_back])
    return np.array(X).reshape(-1, look_back, 1), np.array(y)

# Add more utility functions TO-DO