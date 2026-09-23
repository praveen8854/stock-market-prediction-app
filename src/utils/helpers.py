def calculate_metrics(predictions, actuals):
    mse = ((predictions - actuals) ** 2).mean()  # Mean Squared Error
    mae = (abs(predictions - actuals)).mean()    # Mean Absolute Error
    r_squared = 1 - (sum((actuals - predictions) ** 2) / sum((actuals - actuals.mean()) ** 2))  # R-squared
    return {
        'mean_squared_error': mse,
        'mean_absolute_error': mae,
        'r_squared': r_squared
    }