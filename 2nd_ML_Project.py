import pandas as pd
import sweetviz as sv

# Takes the file's folder
filepath = r"C:\Users\Krishnendu\Desktop\Dataset\Dataset\data7\train.csv"
#EDA using Autoviz
sweet_report = sv.analyze(pd.read_csv(filepath))

#Saving results to HTML file
sweet_report.show_html('sweet_report.html')