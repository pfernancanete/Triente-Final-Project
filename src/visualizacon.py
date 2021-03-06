
import pandas as pd
from config.config import engine
import seaborn as sns
import plotly.express as px


def load_data():
    """
    Loads the data of the dataset
    Returns:
        The dataset
    """
    data = pd.read_csv('Data/BBDD_Empresas_clean.csv')
    return data



def grafico_barras_pais():
    """
    Plots a bargraph of the different countries
    Args:
        data: we call the data function to import the data into our graph
        columns: we select the columns that apply to the graph
    Returns:
        The bargraph
    """
    data = load_data()
    data = data.groupby("País").agg({"País":'count'}).rename(columns={"País":"País", "País":"número de compañías"}).reset_index().set_index("País", drop=True).nlargest(46, 'número de compañías')
    return data



def grafico_barras_provincia():
    """
    Plots a bargraph of the different provinces
    Args:
        data: we call the data function to import the data into our graph
        columns: we select the columns that apply to the graph
    Returns:
        The bargraph
    """
    data = load_data()
    data = data.groupby("Provincia").agg({"Provincia":'count'}).rename(columns={"Provincia":"Provincia", "Provincia":"número de compñías"}).reset_index().set_index("Provincia", drop=True).nlargest(30, 'número de compñías')
    return data



def view_all_comps(razon_social):
    df = pd.read_sql_query(f"""
    SELECT razon_social, cif, domicilio, municipio, codigo_postal, provincia, pais, telefono, web, email, cnae, descripcion_actividad 
    FROM Company
    WHERE razon_social = "{razon_social}"
    """, engine)
    return df


def grafico_barras_actividad():
    data = load_data()
    data = data.groupby("Área_principal").agg({"Área_principal":'count'}).rename(columns={"Área_principal":"Área_principal", "Área_principal":"número de compañías"}).reset_index().set_index("Área_principal", drop=True).nlargest(3,'número de compañías')
    return data


def grafico_actividad(columna1, columna2, datos):
    graph = sns.lineplot(x=columna1, y=columna2, data=datos)
    graph.figure.savefig('grafico.png')


def scatter(columna1, columna2, columna3, dats):
    scatter = sns.scatterplot(x=columna1, y=columna2, hue = columna3, data=dats)
    scatter.legend(loc='center left', bbox_to_anchor=(1.25, 0.5), ncol=1)
    scatter.figure.savefig('scatter.png')






