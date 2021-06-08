import pandas as pd
import plotly.express as px
import csv
import numpy as np

def plot_figure(data_path):
    with open(data_path)as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df, x='Coffee in ml', y='sleep in hours')
        fig.show()

def get_data_source(data_path):
    coffee=[]
    sleep=[]
    with open(data_path)as csv_file:
        df=csv.DictReader(csv_file)
        for row in df:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return {"x": coffee, "y": sleep}

def find_correlation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between the coffee and the amount of sleep is: /n",correlation[0,1])

def setup():
    data_path="class106d.csv"
    data_source=get_data_source(data_path)
    find_correlation(data_source)
    plot_figure(data_path)

setup()