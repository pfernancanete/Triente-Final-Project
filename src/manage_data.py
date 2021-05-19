import pandas as pd
import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()


# Functions
def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS blogtable(author TEXT,title TEXT,article TEXT,postdate DATE)')

def add_data(author,title,article,postdate):
	c.execute('INSERT INTO blogtable(author,title,article,postdate) VALUES (?,?,?,?)',(author,title,article,postdate))
	conn.commit()
    
def add_data(razon_social, cif, domicilio, id_municipio_ine, municipio, provincia, pais, codigo_postal, telefono, fax, web, email, cnae, descripcion_actividad, area_principal, actividad_1, actividad_2, actividad_3, actividad_4, actividad_5, actividad_6, facturacion_2019, inversion_2019, inversion_2020, n_empleados, capital):
    c.execute('INSERT INTO Company((razon_social, cif, domicilio, id_municipio_ine, municipio, provincia, pais, codigo_postal, telefono, fax, web, email, cnae, descripcion_actividad, area_principal, actividad_1, actividad_2, actividad_3, actividad_4, actividad_5, actividad_6, facturacion_2019, inversion_2019, inversion_2020, n_empleados, capital)VALUES) (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(razon_social, cif, domicilio, id_municipio_ine, municipio, provincia, pais, codigo_postal, telefono, fax, web, email, cnae, descripcion_actividad, area_principal, actividad_1, actividad_2, actividad_3, actividad_4, actividad_5, actividad_6, facturacion_2019, inversion_2019, inversion_2020, n_empleados, capital))
    conn.commit()

def view_all_notes():
	c.execute('SELECT * FROM blogtable')
	data = c.fetchall()
	return data
def view_all_comps():
	c.execute('SELECT razon_social FROM Company')
	data = c.fetchall()
	return data


def view_all_titles():
	c.execute('SELECT DISTINCT title FROM blogtable')
	data = c.fetchall()
	return data


def get_blog_by_title(title):
	c.execute('SELECT * FROM blogtable WHERE title="{}"'.format(title))
	data = c.fetchall()
	return data
def get_comp_by_country(pais):
	c.execute('SELECT razon_social FROM Company WHERE pais="{}"'.format(pais))
	data = c.fetchall()
	return data

def buscar_id_mail(mail):

    id_usuario = engine.execute(f"""
        SELECT usuarios.id_usuario
        FROM usuarios
        WHERE usuarios.mail = "{mail}"
    """)

    try:
        respuesta = id_usuario.fetchall()[0][0]
        return respuesta
    except:
        print('Ese usuario no está registrado')

def get_blog_by_author(author):
	c.execute('SELECT * FROM blogtable WHERE author="{}"'.format(author))
	data = c.fetchall()
	return data
def get_comp_by_city(provincia):
	c.execute('SELECT razon_social FROM Company WHERE provincia="{}"'.format(provincia))
	data = c.fetchall()
	return data

def get_comp_by_actividad(actividad):
	c.execute('SELECT razon_social FROM Company WHERE provincia="{}"'.format(actividad))
	data = c.fetchall()
	return data

def delete_data(title):
	c.execute('DELETE FROM blogtable WHERE title="{}"'.format(title))
	conn.commit()