import json
import joblib
import numpy as np
import os

class FertilizerRecommender:
    def __init__(self, model_dir="model"):
        with open(os.path.join(model_dir, "fert_classes.json"), "r") as f:
            self.classes = json.load(f)
        with open(os.path.join(model_dir, "fert_features.json"), "r") as f:
            self.features = json.load(f)
        self.model = joblib.load(os.path.join(model_dir, "fert_model.pkl"))
        print(f"[fertilizer] Loaded {len(self.classes)} fertilizer classes")

    def recommend(self, n, p, k, temp, humidity):
        input_dict = {
            "N": float(n), "P": float(p), "K": float(k),
            "temperature": float(temp), "humidity": float(humidity)
        }
        input_list = [input_dict[feat] for feat in self.features]
        X = np.array(input_list).reshape(1, -1)
        prediction_index = self.model.predict(X)[0]
        return self.classes[prediction_index]

def calculate_dosage_table(fert_type, n, p, k):
    """
    Returns a list of dictionaries representing the rows of a table.
    """
    if not fert_type or "No_fertilizer" in fert_type or "No fertilizer" in fert_type:
        return [{"nutrient": "N/A", "dosage": "0 kg/acre", "notes": "Soil is optimal"}]

    n_val = float(n) if n is not None else 0.0
    p_val = float(p) if p is not None else 0.0
    k_val = float(k) if k is not None else 0.0

    table = []
    
    if "Urea" in fert_type:
        deficit = max(0.0, 100.0 - n_val)
        table.append({"nutrient": "Nitrogen (N)", "dosage": f"{round(deficit * 2.17, 1)} kg/acre", "notes": "Apply via Urea"})
    elif "DAP" in fert_type:
        deficit = max(0.0, 50.0 - p_val)
        table.append({"nutrient": "Phosphorus (P)", "dosage": f"{round(deficit * 2.5, 1)} kg/acre", "notes": "Apply via DAP"})
    elif "MOP" in fert_type:
        deficit = max(0.0, 60.0 - k_val)
        table.append({"nutrient": "Potassium (K)", "dosage": f"{round(deficit * 1.6, 1)} kg/acre", "notes": "Apply via MOP"})
    elif "NPK" in fert_type:
        n_def = max(0.0, 100.0 - n_val)
        p_def = max(0.0, 50.0 - p_val)
        k_def = max(0.0, 60.0 - k_val)
        table.append({"nutrient": "Nitrogen (N)", "dosage": f"{round(n_def * 0.8, 1)} kg/acre", "notes": "From NPK Blend"})
        table.append({"nutrient": "Phosphorus (P)", "dosage": f"{round(p_def * 0.8, 1)} kg/acre", "notes": "From NPK Blend"})
        table.append({"nutrient": "Potassium (K)", "dosage": f"{round(k_def * 0.8, 1)} kg/acre", "notes": "From NPK Blend"})
    
    if not table:
        table.append({"nutrient": "General", "dosage": "Consult agronomist", "notes": "Complex requirement"})
        
    return table