import pandas as pd
from autoviz.AutoViz_Class import AutoViz_Class

# Takes the file's folder
filepath = r"C:\Users\Krishnendu\Desktop\Dataset\Dataset\data7\train.csv"
#EDA using Autoviz
autoviz = AutoViz_Class().AutoViz(filepath)
print(autoviz)
