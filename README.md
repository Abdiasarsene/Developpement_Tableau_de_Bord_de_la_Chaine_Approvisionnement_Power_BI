# 📦 Supply Chain Analytics Dashboard & Predictive API

## 🚀 Objectif du projet
Développer une solution complète pour **visualiser**, **analyser** et **prédire** des données de la chaîne d'approvisionnement.  
Le projet inclut :

- Un **tableau de bord interactif Power BI**.
- Un **modèle prédictif de Machine Learning** pour anticiper les retards de livraison et les besoins de réapprovisionnement.
- Une **API REST déployée avec Docker** pour fournir des prédictions en temps réel.
- Le **suivi des expériences ML** avec **MLflow**.

---

## 🧩 Fonctionnalités principales

### 📊 Dashboard Power BI
- Suivi des livraisons : délais, taux de réussite, retards.
- Gestion des stocks : niveaux, prévisions, ruptures et surstocks.
- Analyse des coûts logistiques par région, fournisseur et itinéraire.
- Visualisations interactives : KPI cards, heatmaps, line charts.

### 🧠 Machine Learning
- Prévision du `Delivery Status` (À temps / En retard / Critique).
- Prévision du `Restock Needed`.
- Tracking des expériences avec **MLflow** (metrics, params, modèles).

### 🌐 API FastAPI + Docker
- API REST pour recevoir des données logistiques et retourner une prédiction.
- Déploiement rapide dans un environnement conteneurisé avec **Docker**.

---

## 🛠️ Technologies utilisées

| Domaine               | Outils / Langages                                  |
|------------------------|----------------------------------------------------|
| Visualisation          | Power BI                                           |
| Traitement de données  | Python (Pandas, NumPy)                             |
| Machine Learning       | Scikit-learn, XGBoost, MLflow                      |
| API                    | FastAPI                                            |
| Conteneurisation       | Docker                                             |
| Tracking               | MLflow Tracking Server (local ou distant)          |
| Base de données (option) | SQLite (tracking MLflow en local)               |

---

## 🛤️ Workflow du projet

1. **Prétraitement des données**
   - Nettoyage (doublons, valeurs manquantes, standardisation).
   - Feature Engineering :
     - `Delivery Delay` (nombre de jours de retard),
     - `Delivery Urgency` (catégorisation critique/retard/à temps),
     - `Restock Needed` (en fonction du seuil de stock).

2. **Modélisation ML**
   - Entraînement avec `RandomForestClassifier`, `XGBoost`.
   - Tracking automatique avec **MLflow** :
     - `params`, `metrics`, `artifacts` (modèle sauvegardé).
   - Sélection du meilleur modèle.

3. **Développement de l'API FastAPI**
   - Endpoint `/predict/` pour prédiction temps réel.
   - Validation des données avec `Pydantic`.

4. **Déploiement avec Docker**
   - Conteneurisation de l’API avec `Dockerfile`.
   - Exposition sur le port 8000.

5. **Création du tableau de bord Power BI**
   - Connexion à la base prétraitée.
   - Construction de KPI Cards, Graphiques, Filtres dynamiques.

---

## 📂 Structure du projet

```
supply_chain_project/
├── data/
│   └── raw_data.xlsx
│   └── preprocessed_data.xlsx
├── notebooks/
│   └── preprocessing.ipynb
    └── models.py
├── models/
│   └── mlflow_runs/      # stockage des modèles
├── api/
│   ├── main.py           # FastAPI application
│   ├── Dockerfile
│   └── requirements.txt
├── dashboard/
│   └── supply_chain_dashboard.pbix
├── README.md
└── mlflow_server/
    ├── mlruns/
    └── mlflow.db
```

---

## 🔥 Comment exécuter le projet

### 1. Prétraitement et Entraînement du Modèle

```bash
# Lancer le tracking MLflow en local
mlflow ui --backend-store-uri sqlite:///mlflow_server/mlflow.db --port 5000

# Exécuter le script de traitement et modélisation
jupyter notebook notebooks/preprocessing.ipynb
python py/models.py
```

- Accéder au tableau MLflow ➔ http://localhost:5000

---

### 2. Déploiement de l'API FastAPI avec Docker

```bash
# Depuis le dossier api/
docker build -t supply_chain_api .
docker run -d -p 8000:8000 supply_chain_api
```

- Accéder à la documentation automatique Swagger ➔ http://localhost:8000/docs

---

### 3. Création du Dashboard Power BI
- Utiliser le fichier `preprocessed_data.xlsx`.
- Connecter Power BI et construire les KPI & graphiques.

---

## 🎯 Résultats attendus

| Objectif                             | Impact                                   |
|--------------------------------------|-----------------------------------------|
| Réduction des retards de livraison   | +15% de livraisons à temps              |
| Optimisation des stocks              | -10% de ruptures et surstocks           |
| Réduction des coûts logistiques      | -8% de frais de transport               |
| Analyse temps réel                   | Décisions plus rapides et basées sur la donnée |

---

## 📧 Contact

👨‍💻 **Abdias Arsène**  
IT Consultant in Innovative Technologies  
📬 Email : abdiasarsene@gmail.com  
🔗 LinkedIn : [Abdias Arsène Z](https://www.linkedin.com/in/abdias-arsene)  

---

## 📝 Licence

Ce projet est fourni à titre professionnel dans le cadre d'un contrat ou d'une mission. Toute reproduction ou usage commercial nécessite une autorisation préalable.

```
