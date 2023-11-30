**PROJECT DEVIN LEE**
---
**TITLE**  
*Prediction_E-Commerce_shipping_data_using_machine_learning*

---
**DATASET**  

*This dataset was created by Prachi Gopalani, An international e-commerce company based wants to discover key insights from their customer database. They want to use some of the most advanced machine learning techniques to study their customers. The company sells electronic products. The dataset used for model building contained 10999 observations of 12 variables*

---
**OBJECTIVES**  
*The purpose of this model is to predict the delivery is on time or not. with the parameters in the data*

---

**TOOLS**  
```py
import pandas as pd
from numpy import mean, median
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, OneHotEncoder
from sklearn.metrics import classification_report, ConfusionMatrixDisplay, precision_score, f1_score
from sklearn.compose import make_column_transformer
from feature_engine.outliers import Winsorizer
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from time import time
import warnings
import pickle
from sklearn.pipeline import Pipeline,make_pipeline
import plotly.express as px
```
---
**DATASET SOURCE** : [Kaggle](https://www.kaggle.com/datasets/prachi13/customer-analytics)