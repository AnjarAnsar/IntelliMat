from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from pipelines.prediction_pipeline import predict_properties
from pipelines.recommendation_pipeline import recommend_materials


# =========================
# FASTAPI APP
# =========================

app = FastAPI()


# =========================
# CORS CONFIGURATION
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# INPUT DATA MODEL
# =========================

class MaterialInput(BaseModel):

    hardness: float
    density: float
    temperature: float
    load: float
    speed: float


# =========================
# HOME ROUTE
# =========================

@app.get("/")
def home():

    return {
        "message": "Material Recommendation API Running"
    }


# =========================
# MAIN RECOMMENDATION ROUTE
# =========================

@app.post("/recommend")
def recommend(data: MaterialInput):

    print("\nReceived Input:")
    print(data)

    # =========================
    # PIPELINE 1
    # PROPERTY PREDICTION
    # =========================

    predicted_properties = predict_properties(
        hardness=data.hardness,
        density=data.density,
        temperature=data.temperature,
        load=data.load,
        speed=data.speed
    )

    print("\nPredicted Properties:")
    print(predicted_properties)

    # =========================
    # PIPELINE 2
    # MATERIAL RECOMMENDATION
    # =========================

    recommended_materials = recommend_materials(
        predicted_wear_rate=predicted_properties["WearRate"],
        predicted_friction=predicted_properties[
            "FrictionCoefficient"
        ]
    )

    print("\nRecommended Materials:")
    print(recommended_materials)

    # =========================
    # FINAL RESPONSE
    # =========================

    return {

        "predicted_properties": predicted_properties,

        "recommended_materials": recommended_materials
    }