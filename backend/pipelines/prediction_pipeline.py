import joblib
import numpy as np
import os


# =========================
# GET ABSOLUTE MODEL PATHS
# =========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "property_predictor.pkl"
)

SCALER_PATH = os.path.join(
    BASE_DIR,
    "models",
    "scaler.pkl"
)


# =========================
# LOAD MODEL AND SCALER
# =========================

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

print("Model and Scaler Loaded Successfully")


# =========================
# PREDICTION FUNCTION
# =========================

def predict_properties(
    hardness,
    density,
    temperature,
    load,
    speed
):

    # Convert user input into NumPy array
    input_data = np.array([[
        hardness,
        density,
        temperature,
        load,
        speed
    ]])

    print("\nOriginal Input:")
    print(input_data)

    # Scale input
    scaled_data = scaler.transform(input_data)

    print("\nScaled Input:")
    print(scaled_data)

    # Predict
    prediction = model.predict(scaled_data)

    print("\nRaw Prediction:")
    print(prediction)

    # Extract prediction values
    wear_rate = float(prediction[0][0])
    friction = float(prediction[0][1])

    # Return final dictionary
    return {
        "WearRate": round(wear_rate, 4),
        "FrictionCoefficient": round(friction, 4)
    }


# =========================
# TESTING
# =========================

if __name__ == "__main__":

    result = predict_properties(
        hardness=65,
        density=7.8,
        temperature=200,
        load=20,
        speed=100
    )

    print("\nFinal Prediction Result:")
    print(result)