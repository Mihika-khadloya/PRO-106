import pandas as pd
import plotly.express as px
import csv
import numpy as np

def plot_figure(data_path):
    with open(data_path)as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df, x='Marks In Percentage', y='Days Present')
        fig.show()

def get_data_source(data_path):
    marks=[]
    days=[]
    with open(data_path)as csv_file:
        df=csv.DictReader(csv_file)
        for row in df:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))
    return {"x": marks, "y": days}

def find_correlation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between the students' marks and days present is: /n",correlation[0,1])

def setup():
    data_path="class106c.csv"
    data_source=get_data_source(data_path)
    find_correlation(data_source)
    plot_figure(data_path)

setup()