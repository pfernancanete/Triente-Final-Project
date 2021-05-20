import os
import pandas as pd
import requests
import sys
from config.config import engine






def get_comp_by_actividad(actividad):
    """
    Reads a query from SQL with the selected parameters
    Returns:
        The companies which have the selected filters from the query
    """
    df = pd.read_sql_query(f"""
        SELECT razon_social AS nombre_empresa, facturacion_2019, n_empleados
        FROM Company 
        WHERE actividad_1 = "{actividad}" OR actividad_2 = "{actividad}" OR actividad_3 = "{actividad}" OR actividad_4 = "{actividad}" OR actividad_5 = "{actividad}" OR actividad_6 = "{actividad}"
        """, engine)
    return df



def get_comp_by_country(pais):
    """
    Reads a query from SQL with the selected parameters
    Returns:
        The companies which have the selected filters from the query
    """
    df = pd.read_sql_query(f"""
    SELECT razon_social 
    FROM Company 
    WHERE pais = '{pais}'
    """, engine)
    return df



def get_comp_by_provincia(provincia):
    """
    Reads a query from SQL with the selected parameters
    Returns:
        The companies which have the selected filters from the query
    """
    df = pd.read_sql_query(f"""
    SELECT razon_social 
    FROM Company 
    WHERE provincia = "{provincia}"
    """, engine)
    return df


def empleados_total():
    """
    Reads a query from SQL with the selected parameters
    Returns:
        The companies which have the selected filters from the query
    """
    df = pd.read_sql_query(f"""
        SELECT razon_social, n_empleados 
        FROM Company 
        ORDER BY n_empleados DESC
        """, engine)
    return df


def empleados_empresa(empresa):
    """
    Reads a query from SQL with the selected parameters
    Returns:
        The companies which have the selected filters from the query
    """
    df = pd.read_sql_query(f"""
        SELECT n_empleados 
        FROM Company
        WHERE razon_social = "{empresa}"
        """, engine)
    return df


def facturacion():
    """
    Reads a query from SQL with the selected parameters
    Returns:
        The companies which have the selected filters from the query
    """
    df = pd.read_sql_query(f"""
        SELECT razon_social, facturacion_2019 
        FROM Company 
        ORDER BY facturacion_2019 DESC
        """, engine)
    return df


def facturacion_empresa(empresa):
    """
    Reads a query from SQL with the selected parameters
    Returns:
        The companies which have the selected filters from the query
    """
    df = pd.read_sql_query(f"""
        SELECT razon_social, facturacion_2019 AS facturacion_2019_millones  
        FROM Company
        WHERE razon_social = "{empresa}"
        """, engine)
    return df


def add_profile(perfil_nuevo):
    """
    Adds the user inputs from streamlit to SQL as new profiles

    """
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in perfil_nuevo.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in perfil_nuevo.values())
    engine.execute(f""" INSERT INTO %s ( %s ) VALUES ( %s );" % ('Company', columns, values)
    """ )