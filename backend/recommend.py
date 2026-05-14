import pandas as pd

df = pd.read_csv("dataset/materials.csv")

def recommend_material(hardness):

    df["difference"] = abs(df["Hardness"] - hardness)

    best_match = df.sort_values("difference").iloc[0]

    return best_match["Material"]