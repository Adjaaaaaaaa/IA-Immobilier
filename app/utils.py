def preprocess_features_with_names(features: dict) -> dict:
    """
    Transforme le dictionnaire de l'API en dictionnaire compatible avec les colonnes du modèle.
    """
    return {
        "Surface reelle bati": features["surface_bati"],
        "Nombre pieces principales": features["nombre_pieces"],
        "Type local_Maison": 1 if features["type_local"] == "Maison" else 0,
        "Surface terrain": features["surface_terrain"],
        "Nombre de lots": features["nombre_lots"]
    }
