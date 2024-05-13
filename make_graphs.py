import pandas as pd
import plotly
import plotly.express as px

def make_histogram(data):
    data_formated = data[['N° auto','situation géographique','entrées 2022']]

