# Importation des bibliothèques
import pandas as pd 
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, LabelBinarizer, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier

# ====== Importer le jeu de données ======
df = pd.DataFrame(r"D:\Projects\IT\Data Science & IA\Developpement_Tableau_de_Bord_de_la_Chaine_Approvisionnement_Power_BI\data\preprocessed_data_supply.xlsx")
print("Jeu de données importé✅✅")