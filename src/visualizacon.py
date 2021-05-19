
import pandas as pd
from config.config import engine
import seaborn as sns


def load_data():
    data = pd.read_csv('Data/BBDD_Empresas_clean.csv')
    return data



def grafico_barras_pais():
    data = load_data()
    data = data.groupby("País").agg({"País":'count'}).rename(columns={"País":"País", "País":"número de compañías"}).reset_index().set_index("País", drop=True).nlargest(46, 'número de compañías')
    return data



def grafico_barras_provincia():
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


def grafico_barras_fact_empl():
    data = load_data()
    data = sns.barplot('Facturación_2019', 'Nº_empleados', palette='Set2', data=data)
    return data

















