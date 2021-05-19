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


def add_profile(response):
    """
    Adds the user inputs from streamlit to SQL as new profiles

    """


    razon_social = engine.execute(f"""SELECT razon_social FROM Company WHERE razon_social = "{response['razon_social']}" """)
    razon_social = razon_social.fetchall()[0][0]
    CIF = engine.execute(f""" SELECT CIF FROM Company WHERE CIF = "{response['CIF']}" """)
    CIF = CIF.fetchall()[0][0]
    telefono = engine.execute(f""" SELECT telefono FROM Company WHERE telefono = "{response['telefono']}" """)
    telefono = telefono.fetchall()[0][0]
    email = engine.execute(f""" SELECT email FROM Company WHERE email = "{response['email']}" """)
    email = email.fetchall()[0][0]
    web = engine.execute(f""" SELECT web FROM Company WHERE web = "{response['web']}" """)
    web = web.fetchall()[0][0]
    domicilio = engine.execute(f""" SELECT domicilio FROM Company WHERE domicilio = "{response['domicilio']}" """)
    domicilio = domicilio.fetchall()[0][0]
    codigo_postal = engine.execute(f""" SELECT codigo_postal FROM Company WHERE codigo_postal = "{response['codigo_postal']}" """)
    codigo_postal = codigo_postal.fetchall()[0][0]
    provincia = engine.execute(f""" SELECT provincia FROM Company WHERE provincia = "{response['provincia']}" """)
    provincia = provincia.fetchall()[0][0]
    pais = engine.execute(f""" SELECT pais FROM Company WHERE pais = "{response['pais']}" """)
    pais = pais.fetchall()[0][0]
    cnae = engine.execute(f""" SELECT cnae FROM Company WHERE cnae = "{response['cnae']}" """)
    cnae = cnae.fetchall()[0][0]
    area_principal = engine.execute(f""" SELECT area_principal FROM Company WHERE area_principal = "{response['area_principal']}" """)
    area_principal = area_principal.fetchall()[0][0]
    descripcion_actividad = engine.execute(f""" SELECT descripcion_actividad FROM Company WHERE descripcion_actividad = "{response['descripcion_actividad']}" """)
    descripcion_actividad = descripcion_actividad.fetchall()[0][0] 

    engine.execute(f"""
    INSERT INTO Company (razon_social, CIF, telefono, email, web, domicilio, municipio, codigo_postal, provincia, pais, cnae, area_principal, descripcion_actividad)
    VALUES ("{razon_social}", "{CIF}", "{telefono}", "{email}", "{web}", "{domicilio}", "{codigo_postal}", "{provincia}", "{pais}", "{cnae}", "{area_principal}", "{descripcion_actividad}");
    """ )







