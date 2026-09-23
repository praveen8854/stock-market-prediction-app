def load_data(source: str):
    import pandas as pd

    if source.endswith('.csv'):
        data = pd.read_csv(source)
    else:
        raise ValueError("Unsupported data source format. Please provide a CSV file.")

    return data