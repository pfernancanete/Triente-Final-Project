import pandas as pd
import sqlite3
import folium
import json
import os
import pandas as pd
import requests
import sys
from config.config import engine

conn = sqlite3.connect('data.db')
c = conn.cursor()


def add_data(razon_social, cif, domicilio, id_municipio_ine, municipio, provincia, pais, codigo_postal, telefono, fax, web, email, cnae, descripcion_actividad, area_principal, actividad_1, actividad_2, actividad_3, actividad_4, actividad_5, actividad_6, facturacion_2019, inversion_2019, inversion_2020, n_empleados, capital):
    c.execute('INSERT INTO Company((razon_social, cif, domicilio, id_municipio_ine, municipio, provincia, pais, codigo_postal, telefono, fax, web, email, cnae, descripcion_actividad, area_principal, actividad_1, actividad_2, actividad_3, actividad_4, actividad_5, actividad_6, facturacion_2019, inversion_2019, inversion_2020, n_empleados, capital)VALUES) (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(razon_social, cif, domicilio, id_municipio_ine, municipio, provincia, pais, codigo_postal, telefono, fax, web, email, cnae, descripcion_actividad, area_principal, actividad_1, actividad_2, actividad_3, actividad_4, actividad_5, actividad_6, facturacion_2019, inversion_2019, inversion_2020, n_empleados, capital))
    conn.commit()


def view_all_comps(razon_social):
    company = engine.execute(f"""
    SELECT razon_social, cif, domicilio, municipio, codigo_postal, provincia, pais, telefono, web, email, cnae, descripcion_actividad 
    FROM Company
    WHERE razon_social = "{razon_social}"
    """)
    try:
        data = company.fetchall()
        return data
    except:
        print('Ese usuario no está registrado')



def get_comp_by_country(pais):
	pais = engine.execute(f"""
    SELECT razon_social 
    FROM Company 
    WHERE pais = '{pais}'
    """)
    try:
        data = pais.fetchall()
        return data
    except:
        print('No existen empresas en ese pais')



def get_comp_by_provincia(provincia):
	provincia = engine.execute(f"""
    SELECT razon_social 
    FROM Company 
    WHERE provincia = "{provincia}"
    """)
    try:
        data = provincia.fetchall()
        return data
    except:
        print('No existen empresas en esa provincia')




def get_comp_by_actividad(actividad):
    df = pd.read_sql_query(f"""
        SELECT razon_social 
        FROM Company 
        WHERE actividad_1 = "{actividad}" OR actividad_2 = "{actividad}" OR actividad_3 = "{actividad}" OR actividad_4 = "{actividad}" OR actividad_5 = "{actividad}" OR actividad_6 = "{actividad}"
        """, engine)
    return df

def add_company(razon_social, cif, domicilio, id_municipio_ine, municipio, provincia, pais, codigo_postal, telefono, fax, web, email, cnae, descripcion_actividad, area_principal, actividad_1, actividad_2, actividad_3, actividad_4, actividad_5, actividad_6, facturacion_2019, inversion_2019, inversion_2020, n_empleados, capital):
    engine.execute(
        f"""
        INSERT INTO Company((razon_social, cif, domicilio, id_municipio_ine, municipio, provincia, pais, codigo_postal, telefono, fax, web, email, cnae, descripcion_actividad, area_principal, actividad_1, actividad_2, actividad_3, actividad_4, actividad_5, actividad_6, facturacion_2019, inversion_2019, inversion_2020, n_empleados, capital)VALUES)
        (razon_social, cif, domicilio, id_municipio_ine, municipio, provincia, pais, codigo_postal, telefono, fax, web, email, cnae, descripcion_actividad, area_principal, actividad_1, actividad_2, actividad_3, actividad_4, actividad_5, actividad_6, facturacion_2019, inversion_2019, inversion_2020, n_empleados, capital))
    conn.commit()























