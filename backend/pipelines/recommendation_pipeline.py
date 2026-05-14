print("STARTED")

import pandas as pd
import numpy as np
import os

from sklearn.metrics.pairwise import euclidean_distances

# =========================
# LOAD DATASET
# =========================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "materials.csv"
)

df = pd.read_csv(DATASET_PATH)

print("Dataset Loaded Successfully")


# =========================
# RECOMMENDATION FUNCTION
# =========================

def recommend_materials(
    predicted_wear_rate,
    predicted_friction,
    top_n=5
):

    print("\nPredicted Values:")
    print("Wear Rate:", predicted_wear_rate)
    print("Friction Coefficient:", predicted_friction)

    # User vector
    user_vector = np.array([[
        predicted_wear_rate,
        predicted_friction
    ]])

    # Dataset vectors
    dataset_vectors = df[[
        "WearRate",
        "FrictionCoefficient"
    ]].values

    # =========================
    # CALCULATE EUCLIDEAN DISTANCE
    # =========================

    distances = euclidean_distances(
        user_vector,
        dataset_vectors
    )

    distances = distances[0]

    print("\nDistances:")
    print(distances)

    # =========================
    # CONVERT TO SIMILARITY
    # =========================

    similarities = 1 / (1 + distances)

    # Convert to percentage
    df["Similarity"] = similarities * 100

    # =========================
    # SORT MATERIALS
    # =========================

    recommended = df.sort_values(
        by="Similarity",
        ascending=False
    )

    print("\nSorted Similarity Scores:\n")

    for _, row in recommended.iterrows():

        print(
            f"{row['Material']} : "
            f"{row['Similarity']:.2f}%"
        )

    # =========================
    # TOP MATERIALS
    # =========================

    top_materials = recommended.head(top_n)

    results = []

    for _, row in top_materials.iterrows():

        results.append({
            "Material": row["Material"],
            "WearRate": round(
                row["WearRate"], 4
            ),
            "FrictionCoefficient": round(
                row["FrictionCoefficient"], 4
            ),
            "SimilarityScore": round(
                row["Similarity"], 2
            )
        })

    return results


# =========================
# TESTING
# =========================

if __name__ == "__main__":

    recommendations = recommend_materials(
        predicted_wear_rate=0.25,
        predicted_friction=0.40
    )

    print("\nRecommended Materials:\n")

    for material in recommendations:
        print(material)