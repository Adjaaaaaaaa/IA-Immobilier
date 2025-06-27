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
|   |comparaison.ipynb
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


Sur le plan technique, l’API a été développée avec FastAPI pour bénéficier d’un framework léger, rapide et compatible avec les standards modernes (OpenAPI, Pydantic). Le projet est structuré de manière modulaire avec une séparation claire entre les routes, le chargement des modèles, la logique métier de prédiction et le prétraitement des données. Les modèles de machine learning ont été préalablement entraînés, puis sérialisés avec joblib dans un fichier unique, ce qui permet un chargement rapide en mémoire à chaque appel. J’ai opté pour des routes asynchrones (async def) afin de simuler le comportement d'appels I/O non bloquants (ex. appels à des APIs externes), en utilisant await asyncio.sleep() comme outil pédagogique. L’API expose trois endpoints POST, dont un endpoint dynamique /predict permettant de basculer entre les deux modèles via une seule interface. Ce choix facilite la mise en place d’un A/B testing contrôlé entre les modèles de Lille et Bordeaux pour évaluer leur performance respective.