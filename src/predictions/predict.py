def make_prediction(model, input_data):
    """
    Make predictions using the trained stock market model.

    Parameters:
    model: The trained stock market model.
    input_data: The input data for which predictions are to be made.

    Returns:
    predictions: The predicted stock prices.
    """
    predictions = model.predict(input_data)
    return predictions