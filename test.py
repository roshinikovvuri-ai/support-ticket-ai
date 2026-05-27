from app.model import train_model, predict_category

# Train model
train_model()

# Test prediction
result = predict_category("My payment failed")

print("Predicted Category:", result)