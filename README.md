```
IA-IMMOBILIER/
│
├── data/                             # Fichiers sources (ex : lille_2022.csv, bordeaux_2022.csv)
│                                     # Ne pas pousser ce dossier sur GitHub
│
├── models/                           # Modèles sauvegardés (.pkl, .joblib)
│   ├── model_lille.pkl
│   └── model_bordeaux.pkl
│
├── notebooks/                        # Études exploratoires et modélisation
│   ├── phase_1_lille.ipynb
│   └── phase_2_bordeaux.ipynb
│
├── app/                              # Code source de l’API FastAPI
│   ├── main.py                       # Point d’entrée FastAPI, routes des prédictions
│   ├── predict.py                    # Fonctions de prédiction
│   ├── model_loader.py               # Chargement des modèles ML
│   ├── schemas.py                    # Modèles Pydantic pour validation des requêtes
│   └── utils.py                      # Prétraitement, nettoyage, encodage
│
├── tests/                            # Tests unitaires avec pytest
│   ├── test_predict_lille.py
│   └── test_predict_bordeaux.py
│
├── requirements.txt                  # Dépendances du projet
├── README.md                         # Documentation complète du projet
├── .gitignore                        # Exclusion des fichiers (ex: /data/, *.pkl)
└── .env.example                      # Exemple de fichier d’environnement (si besoin)
``` 

![alt text](nom_image.png)
