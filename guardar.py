if choice == "NUEVO PERFIL":
	empresa_col.header("Conviertete en parte de la comunidad Triente")
	st.text("")
	empresa_col.subheader("Información Empresa")
	try:
		perfil_nuevo = {}

	#------------------------------------------FILA 1------------------------------------------------------	
		with empresa_col1:
			perfil_nuevo['Empresa'] = st.text_input('Introduce el nombre de tu empresa *')
			perfil_nuevo['Razon_Social'] = st.text_input('Razón Social *')
			perfil_nuevo['CIF'] = st.text_input('CIF *')

		with empresa_col2:
			perfil_nuevo['Teléfono'] = st.text_input('Teléfono')
			perfil_nuevo['Email'] = st.text_input('Email')
			perfil_nuevo['WEB'] = st.text_input('WEB')

		with empresa_col3:
			perfil_nuevo['Instagram'] = st.text_input('Instagram')
			perfil_nuevo['Linkedin'] = st.text_input('LinkedIn')
			perfil_nuevo['Facebook'] = st.text_input('Facebook')
	#------------------------------------------FILA 2------------------------------------------------------
		st.text("")

		with direccion_col1:
			perfil_nuevo['Domicilio'] = st.text_input('Domicilio')
			perfil_nuevo['Municipio'] = st.text_input('Municipio')
		with direccion_col2:
			perfil_nuevo['Codigo_Postal'] = st.text_input('Código Postal')
			perfil_nuevo['Provincia'] = st.text_input('Provincia *')
			perfil_nuevo['País'] = st.text_input('País *')

		st.text("")
	#------------------------------------------FILA 3------------------------------------------------------
		with obra_col1:
			perfil_nuevo['Area_Principal'] =  st.selectbox('Selecciona área principal *', ["select..","Proyectos inmobiliarios","Distribución","Materiales"])
			perfil_nuevo['Area_Principal'] =  st.selectbox('Selecciona categoria', ["select..","Consultoría inmobiliaria", "Diseño y gestión de proyectos", "Constructoras", "Internet: plataformas", "Software", "Promotoras inmobiliarias", "Instaladoras"])
			perfil_nuevo['Actividad_Principal'] = st.text_input('Actividad *')
			perfil_nuevo['Tipo_Edificio'] = st.text_input('Tipo de edificio')
		with obra_col2:
			perfil_nuevo['Tipo_Obra'] = st.text_input('Tipo de obra')
			perfil_nuevo['Localización'] = st.text_input('Localización')
			perfil_nuevo['Superficie_edificable'] = st.text_input('Superficie edificable')
		with obra_col3:
			perfil_nuevo['ImporteProyecto'] = st.text_input('Importe proyecto')
			perfil_nuevo['Proyectos'] = st.text_input('Proyectos notorios')
			perfil_nuevo['Clientes'] = st.text_input('Clientes principales')
			perfil_nuevo['Premios'] = st.text_input('Premios')


		if obra_col3.button('Añadir Perfil'):
			if perfil_nuevo['Empresa'] != '' and perfil_nuevo['Razon_Social'] != '' and perfil_nuevo['CIF'] != '' and perfil_nuevo['Provincia'] != '' and perfil_nuevo['País'] != '' and perfil_nuevo['Sector_Principal'] != '' and perfil_nuevo['Actividad'] != '':
					try:
						td.add_profile(perfil_nuevo)
						st.success('Restaurante incluido con exito')
						st.balloons()
					except:
						st.warning('Recuerda que hay campos olbligatorios *')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
	st.text('This will appear first')
	# Appends some text to the app.

	my_slot1 = st.empty()
	# Appends an empty slot to the app. We'll use this later.

	my_slot2 = st.empty()
	# Appends another empty slot.

	st.text('This will appear last')
	# Appends some more text to the app.

	my_slot1.text('This will appear second')
	# Replaces the first empty slot with a text string.

	my_slot2.line_chart(np.random.randn(20, 2))
	# Replaces the second empty slot with a chart.
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
	progress_bar = st.progress(0)
	status_text = st.empty()
	chart = st.line_chart(np.random.randn(10, 2))

	for i in range(100):
		# Update progress bar.
		progress_bar.progress(i + 1)

		new_rows = np.random.randn(10, 2)

		# Update status text.
		status_text.text(
			'The latest random number is: %s' % new_rows[-1, 1])

		# Append data to the chart.
		chart.add_rows(new_rows)

		# Pretend we're doing some computation that takes time.
		time.sleep(0.1)

	status_text.text('Done!')
	st.balloons()
		
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
	import numpy as np
	import time

	# Get some data.
	data = np.random.randn(10, 2)

	# Show the data as a chart.
	chart = st.line_chart(data)

	# Wait 1 second, so the change is clearer.
	time.sleep(1)

	# Grab some more data.
	data2 = np.random.randn(10, 2)

	# Append the new data to the existing chart.
	chart.add_rows(data2)



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
