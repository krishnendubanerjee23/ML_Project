import dtale
import pandas as pd
filepath = r"C:\Users\Krishnendu\Desktop\Dataset\Dataset\data7\train.csv"
df = dtale.show(pd.read_csv(filepath ))
df.open_browser()
