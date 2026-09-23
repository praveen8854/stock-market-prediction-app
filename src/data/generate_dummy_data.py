import pandas as pd
import numpy as np
import csv
import os

def generate_dummy_data(file_path):
    # Generate dates
    dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="B")  # Business days only

    # Generate dummy stock data
    data = {
        "Date": dates,
        "Open": np.random.uniform(100, 200, len(dates)),
        "High": np.random.uniform(200, 300, len(dates)),
        "Low": np.random.uniform(50, 100, len(dates)),
        "Close": np.random.uniform(100, 200, len(dates)),
        "Volume": np.random.randint(1000, 10000, len(dates)),
        "Target": np.random.uniform(100, 200, len(dates))  # Target column for prediction
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Save to CSV
    df.to_csv(file_path, index=False)
    print(f"Dummy data saved to {file_path}")

def create_stock_data_csv(file_path):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Example stock data
    stock_data = [
        {"date": "2025-05-01", "open": 100, "high": 110, "low": 95, "close": 105, "volume": 1000, "target_column": 1},
        {"date": "2025-05-02", "open": 105, "high": 115, "low": 100, "close": 110, "volume": 1200, "target_column": 0},
        {"date": "2025-05-03", "open": 110, "high": 120, "low": 105, "close": 115, "volume": 1500, "target_column": 1},
    ]

    # Write to CSV
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=stock_data[0].keys())
        writer.writeheader()
        writer.writerows(stock_data)
    print(f"Sample stock data saved to {file_path}")

# Create the CSV file
create_stock_data_csv('src/data/stock_data.csv')

if __name__ == "__main__":
    generate_dummy_data("c:/Users/veer9/code/stock/stock-market-prediction-app/src/data/dummy_stock_data.csv")