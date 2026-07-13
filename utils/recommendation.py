def generate_recommendation(current_price, predicted_price):
    """
    Generates BUY / HOLD / SELL recommendation
    based on predicted future price.
    """

    change = ((predicted_price - current_price) / current_price) * 100

    if change >= 5:
        recommendation = "🟢 BUY"
        reason = (
            "The AI model predicts the future price will be "
            "more than 5% higher than the current market price."
        )

    elif change <= -5:
        recommendation = "🔴 SELL"
        reason = (
            "The AI model predicts the future price will be "
            "more than 5% lower than the current market price."
        )

    else:
        recommendation = "🟠 HOLD"
        reason = (
            "The AI model predicts only a small price movement."
        )

    return recommendation, reason, round(change, 2)