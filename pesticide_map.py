# pesticide_map.py

DISEASE_INFO = {
    "Apple___Apple_scab": {"common": "Apple - Apple scab", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Apple___Cedar_apple_rust": {"common": "Apple - Cedar apple rust", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Apple___healthy": {"common": "Apple - healthy", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Blueberry___healthy": {"common": "Blueberry - healthy", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Cherry___healthy": {"common": "Cherry - healthy", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Corn___Cercospora_leaf_spot": {"common": "Corn - Cercospora leaf spot", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Corn___Common_rust": {"common": "Corn - Common rust", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Corn___Northern_Leaf_Blight": {"common": "Corn - Northern Leaf Blight", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Grape___Black_rot": {"common": "Grape - Black rot", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Grape___healthy": {"common": "Grape - healthy", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Peach___healthy": {"common": "Peach - healthy", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Pepper__bell___Bacterial_spot": {"common": "Pepper  bell - Bacterial spot", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Pepper__bell___healthy": {"common": "Pepper  bell - healthy", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Potato___Early_blight": {"common": "Potato - Early blight", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Potato___Late_blight": {"common": "Potato - Late blight", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Raspberry___healthy": {"common": "Raspberry - healthy", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Soybean___healthy": {"common": "Soybean - healthy", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Squash___Powdery_mildew": {"common": "Squash - Powdery mildew", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Strawberry___healthy": {"common": "Strawberry - healthy", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Tomato___Bacterial_spot": {"common": "Tomato - Bacterial spot", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Tomato___Early_blight": {"common": "Tomato - Early blight", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Tomato___Late_blight": {"common": "Tomato - Late blight", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Tomato___Leaf_Mold": {"common": "Tomato - Leaf Mold", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Tomato___Septoria_leaf_spot": {"common": "Tomato - Septoria leaf spot", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Tomato___Tomato_mosaic_virus": {"common": "Tomato - Tomato mosaic virus", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Tomato___Yellow_Leaf_Curl_Virus": {"common": "Tomato - Yellow Leaf Curl Virus", "scientific": "Pending", "pesticide": "Consult agronomist"},
    "Tomato___healthy": {"common": "Tomato - healthy", "scientific": "Pending", "pesticide": "Consult agronomist"},
}

def get_disease_info(disease_class):
    return DISEASE_INFO.get(disease_class, {
        "common": disease_class.replace("___", " ").replace("_", " "),
        "scientific": "Unknown",
        "pesticide": "Consult local agronomist"
    })
