from data.data_loader import load_data
from data.preprocess import preprocess_data
from models.train import train_model
from predictions.predict import make_prediction
from models.model import StockModel
import pandas as pd
import numpy as np
import os
def main():
    # Load stock market data
    data_source = 'src/data/stock_data.csv'  # Update with the correct path to your data file
    raw_data = load_data(data_source)

    # Preprocess the data
    processed_data = preprocess_data(raw_data)

    # Split data into features and target
    X = processed_data.drop('target_column', axis=1)  # Replace 'target_column' with your actual target column name
    y = processed_data['target_column']

    # Train the model
    model = train_model(data_source)  # Pass the data source path instead of (X, y)

    # Make predictions
    input_data = X.tail(1)  # Example: using the last row of features for prediction
    predictions = make_prediction(model, input_data)

    print("Predicted stock prices:", predictions)

if __name__ == "__main__":
    main()