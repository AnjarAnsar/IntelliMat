print("AUTO ML TRAINING STARTED")

import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.multioutput import MultiOutputRegressor

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR

from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error


# =========================
# CREATE MODELS FOLDER
# =========================

os.makedirs("models", exist_ok=True)


# =========================
# LOAD DATASET
# =========================

df = pd.read_csv("dataset/materials.csv")

print("\nDataset Loaded Successfully")


# =========================
# INPUT FEATURES
# =========================

X = df[[
    "Hardness",
    "Density",
    "Temperature",
    "Load",
    "Speed"
]]


# =========================
# TARGET OUTPUTS
# =========================

Y = df[[
    "WearRate",
    "FrictionCoefficient"
]]


# =========================
# TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)


# =========================
# FEATURE SCALING
# =========================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# =========================
# CANDIDATE MODELS
# =========================

models = {

    "Linear Regression":
    MultiOutputRegressor(
        LinearRegression()
    ),

    "Random Forest":
    RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ),

    "Support Vector Machine":
    MultiOutputRegressor(
        SVR()
    ),

    "Gradient Boosting":
    MultiOutputRegressor(
        GradientBoostingRegressor()
    )
}


# =========================
# AUTOMATED MODEL SELECTION
# =========================

best_model = None
best_model_name = ""
best_r2 = -999


print("\nTraining Multiple Models...\n")


for model_name, model in models.items():

    print(f"Training {model_name}...")

    # Train model
    model.fit(X_train_scaled, y_train)

    # Predictions
    predictions = model.predict(X_test_scaled)

    # Metrics
    r2 = r2_score(y_test, predictions)

    mse = mean_squared_error(
        y_test,
        predictions
    )

    print(f"R2 Score : {r2}")
    print(f"MSE : {mse}")
    print("-" * 40)

    # Select best model
    if r2 > best_r2:

        best_r2 = r2
        best_model = model
        best_model_name = model_name


# =========================
# FINAL BEST MODEL
# =========================

print("\nBEST MODEL SELECTED:")
print(best_model_name)

print(f"Best R2 Score: {best_r2}")


# =========================
# SAVE BEST MODEL
# =========================

joblib.dump(
    best_model,
    "models/property_predictor.pkl"
)

joblib.dump(
    scaler,
    "models/scaler.pkl"
)

print("\nBest Model Saved Successfully")