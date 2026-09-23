from models.model import StockModel
from data.data_loader import load_data
from data.preprocess import preprocess_data

def train_model(source: str):
    # Load the data
    data = load_data(source)
    
    # Preprocess the data
    processed_data = preprocess_data(data)
    
    # Split the data into features and target
    X = processed_data.drop('target', axis=1)
    y = processed_data['target']
    
    # Initialize the model
    model = StockModel()
    
    # Train the model
    model.train(X, y)
    
    return model