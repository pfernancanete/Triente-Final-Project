import streamlit as st
from PIL import Image
import src.manage_data as dat
import plotly.express as px
import pandas as pd
import streamlit.components.v1 as components
import os
import src.prueba as fi
import time
from datetime import datetime
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import src.visualizacon as vi


st.set_page_config(page_title="TRIENTE", page_icon="👷", layout='centered', initial_sidebar_state='auto')


imagen = Image.open('Images/Logo/Construction.jpg')	
st.image(imagen)



weekday = datetime.today().weekday()

empresa_col, direccion_col, obra_col = st.beta_columns([2.8,0.1,0.1])
empresa_col1, empresa_col2 = st.beta_columns([1,1])
direccion_col1, direccion_col2 = st.beta_columns([1,1])


menu = ["HOME", "BUSCADOR", "EXPLORA", "NUEVO PERFIL"]
choice = st.sidebar.selectbox("Menu",menu)


#-----------------------------------------HOME---------------------------------------------------------------------------------

if choice == "HOME":
	st.subheader("Busca a tu socio")


	name = st.text_input('Enter your name')

	years = st.number_input('Enter your age')

	gender = st.selectbox('Enter your gender', ['Select..','Female','Male','Other','Prefer not to answer'])

	ocupation = st.selectbox('Enter your ocupation', ['Select..','Working','Studying','None'])

	children = st.selectbox('Do you have any children?', ['Select..','YES','NO'])

	world = st.selectbox('Where do you live?', ['Select..','Madrid','Another city in Spain','Outside of Spain'])

	time_ = datetime.now()

	weekday = datetime.today().weekday()

	h= 	st.button('Hit me')
	f=	st.checkbox('Check me out')
	g=	st.radio('Radio', [1,2,3])
	i=	st.selectbox('Select', [1,2,3])
	j=	st.multiselect('Multiselect', [1,2,3])
	k=	st.slider('Slide me', min_value=0, max_value=10)
	l=	st.select_slider('Slide to select', options=[1,'2'])
	m=	st.text_input('Enter some text')
	n=	st.number_input('Enter a number')
	o=	st.text_area('Area for textual entry')
	p=	st.date_input('Date input')
	q=	st.time_input('Time entry')
	r=	st.file_uploader('File uploader')
	s=	st.color_picker('Pick a color')
	st.spinner(text='Thinking🧠')

	if ((years != 0.0) and (gender in ['Female','Male','Other','Prefer not to answer'])) and ((ocupation in ['Working','Studying','None']) and (children in ['YES','NO'])) and world in ['Madrid','Another city in Spain','Outside of Spain']:
    
		st.header(f"Hello {name}. What do you want to do today? ⚡️⚡️ ")

		st.write("""
		How do you want to search?
		""")




#-----------------------------------------BUSCADOR---------------------------------------------------------------------------------



if choice == "BUSCADOR":
	st.subheader("Busca a tu socio")

	search_area_principal = st.selectbox('Selecciona área principal', ["select..","Proyectos inmobiliarios","Distribución","Materiales"])
	

	if search_area_principal == "Proyectos inmobiliarios":
		search_subarea1 = st.selectbox('Selecciona categoria', ["select..","Consultoría inmobiliaria", "Diseño y gestión de proyectos", "Constructoras", "Internet: plataformas", "Software", "Promotoras inmobiliarias", "Instaladoras"])

		if search_subarea1 == "Consultoría inmobiliaria":
			search_actividad1 = st.selectbox('Selecciona sub-categoria', ["select..","Consultoría inmobiliaria", "Consultoras para el sector hostelero"]) 
			
			if search_actividad1 == "Consultoría inmobiliaria":    
				datos = fi.get_comp_by_actividad(search_actividad1)
				st.dataframe(datos.style.highlight_max(axis=0))
				chart_data = pd.DataFrame(
			 		np.random.randn(50, 3),
			    	columns=["a", "b", "c"])
		
				st.bar_chart(chart_data)

			if search_actividad1 == "Consultoras para el sector hostelero":    
				datos = fi.get_comp_by_actividad(search_actividad1)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea1 == "Diseño y gestión de proyectos":
			search_actividad2 = st.selectbox('Selecciona sub-categoria', ["select..","Arquitectura", "Decoración integral para hostelería","Ingeniería / construcción","Project management"])

			if search_actividad2 == "Arquitectura":    
				datos = fi.get_comp_by_actividad(search_actividad2)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad2 == "Decoración integral para hostelería":    
				datos = fi.get_comp_by_actividad(search_actividad2)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad2 == "Ingeniería / construcción":    
				datos = fi.get_comp_by_actividad(search_actividad2)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad2 == "Project management":    
				datos = fi.get_comp_by_actividad(search_actividad2)
				st.dataframe(datos.style.highlight_max(axis=0))				


		if search_subarea1 == "Constructoras":
			search_actividad3 = st.selectbox('Selecciona sub-categoria', ["select..","Cimentación y estructuras hormigón", "Construcción especial","Construcción estructuras madera","Construcción estructuras metálicas","Construcción obra civil","Constructoras","Excavaciones y derribos","Grandes grupos constructores"])

			if search_actividad3 == "Cimentación y estructuras hormigón":    
				datos = fi.get_comp_by_actividad(search_actividad3)
				st.dataframe(datos.style.highlight_max(axis=0))
				
			if search_actividad3 == "Construcción especial":    
				datos = fi.get_comp_by_actividad(search_actividad3)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad3 == "Construcción estructuras madera":    
				datos = fi.get_comp_by_actividad(search_actividad3)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad3 == "Construcción estructuras metálicas":    
				datos = fi.get_comp_by_actividad(search_actividad3)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad3 == "Construcción obra civil":    
				datos = fi.get_comp_by_actividad(search_actividad3)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad3 == "Constructoras":    
				datos = fi.get_comp_by_actividad(search_actividad3)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad3 == "Excavaciones y derribos":    
				datos = fi.get_comp_by_actividad(search_actividad3)
				st.dataframe(datos.style.highlight_max(axis=0))


			if search_actividad3 == "Grandes grupos constructores":    
				datos = fi.get_comp_by_actividad(search_actividad3)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea1 == "Internet: plataformas":
			search_actividad4 = st.selectbox('Selecciona sub-categoria', ["select..","Ferias / recintos feriales", "Internet: plataformas de construcción"])      

			if search_actividad4 == "Ferias / recintos feriales":    
				datos = fi.get_comp_by_actividad(search_actividad4)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad4 == "Internet: plataformas de construcción":    
				datos = fi.get_comp_by_actividad(search_actividad4)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea1 == "Software":
			search_actividad5 = st.selectbox('Selecciona sub-categoria', ["select..","Software para construcción"])   

			if search_actividad5 == "Software para construcción":    
				datos = fi.get_comp_by_actividad(search_actividad5)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea1 == "Promotoras inmobiliarias":
			search_actividad6 = st.selectbox('Selecciona sub-categoria', ["select..","Gestoras-promotoras de viviendas", "Gestora / explotadora hotelera","Grandes grupos inmobiliarios","Promoción de centros comerciales","Parques / zonas logísticas","Promotoras inmobiliarias","Propietaria de inmuebles hoteleros (patrimonio)","Services y patrimoniales inmobiliarias"])

			if search_actividad6 == "Gestoras-promotoras de viviendas":    
				datos = fi.get_comp_by_actividad(search_actividad6)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad6 == "Gestora / explotadora hotelera":    
				datos = fi.get_comp_by_actividad(search_actividad6)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad6 == "Grandes grupos inmobiliarios":    
				datos = fi.get_comp_by_actividad(search_actividad6)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad6 == "Promoción de centros comerciales":    
				datos = fi.get_comp_by_actividad(search_actividad6)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad6 == "Parques / zonas logísticas":    
				datos = fi.get_comp_by_actividad(search_actividad6)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad6 == "Promotoras inmobiliarias":    
				datos = fi.get_comp_by_actividad(search_actividad6)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad6 == "Propietaria de inmuebles hoteleros (patrimonio)":    
				datos = fi.get_comp_by_actividad(search_actividad6)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad6 == "Services y patrimoniales inmobiliarias":    
				datos = fi.get_comp_by_actividad(search_actividad6)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea1 == "Instaladoras":
			search_actividad7 = st.selectbox('Selecciona sub-categoria', ["select..","Instalación aislantes", "Instalación aislantes / impermeabilizantes","Instalación climatización / fontanería","Instalación electricidad / telefonía", "Instalaciones industriales / mecánicas", "Instalaciones tratamiento de agua", "Otras instalaciones"])

			if search_actividad7 == "Instalación aislantes":    
				datos = fi.get_comp_by_actividad(search_actividad7)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad7 == "Instalación aislantes / impermeabilizantes":    
				datos = fi.get_comp_by_actividad(search_actividad7)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad7 == "Instalación climatización / fontanería	":    
				datos = fi.get_comp_by_actividad(search_actividad7)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad7 == "Instalación electricidad / telefonía":    
				datos = fi.get_comp_by_actividad(search_actividad7)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad7 == "Instalaciones industriales / mecánicas":    
				datos = fi.get_comp_by_actividad(search_actividad7)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad7 == "Instalaciones tratamiento de agua":    
				datos = fi.get_comp_by_actividad(search_actividad7)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad7 == "Otras instalaciones":    
				datos = fi.get_comp_by_actividad(search_actividad7)
				st.dataframe(datos.style.highlight_max(axis=0))



	elif search_area_principal == "Distribución":
		search_subarea2 = st.selectbox('Selecciona categoria', ["select..","Distribución de materiales", "Máquinas y herramientas", "Distribución máq. y herramientas", "Transporte", "Central de compras materiales"])
		
		if search_subarea2 == "Distribución de materiales":
			search_actividad8 = st.selectbox('Selecciona sub-categoria', ["select..","Distribución azulejos, sanitarios y grifería", "Distribución bricolaje","Distribución carpintería metálica","Distribución ferretería / industriales","Distribución fontanería y climatización","Distribución hierros","Distribución maderas","Distribución mobiliario","Distribución material eléctrico","Distribución multiproducto","Distribución minorista electro","Distribución pinturas y productos químicos","Distribución vidrio","Otros distribuidores especializados"])

			if search_actividad8 == "Distribución azulejos, sanitarios y grifería":    
				datos = fi.get_comp_by_actividad(search_actividad8)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad8 == "Distribución bricolaje":    
				datos = fi.get_comp_by_actividad(search_actividad8)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad8 == "Distribución carpintería metálica":    
				datos = fi.get_comp_by_actividad(search_actividad8)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad8 == "Distribución ferretería / industriales":    
				datos = fi.get_comp_by_actividad(search_actividad8)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad8 == "Distribución fontanería y climatización":    
				datos = fi.get_comp_by_actividad(search_actividad8)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad8 == "Distribución hierros":    
				datos = fi.get_comp_by_actividad(search_actividad8)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad8 == "Distribución maderas":    
				datos = fi.get_comp_by_actividad(search_actividad8)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad8 == "Distribución mobiliario":    
				datos = fi.get_comp_by_actividad(search_actividad8)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad8 == "Distribución material eléctrico":    
				datos = fi.get_comp_by_actividad(search_actividad8)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad8 == "Distribución multiproducto":    
				datos = fi.get_comp_by_actividad(search_actividad8)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad8 == "Distribución minorista electro":    
				datos = fi.get_comp_by_actividad(search_actividad8)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad8 == "Distribución pinturas y productos químicos":    
				datos = fi.get_comp_by_actividad(search_actividad8)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad8 == "Distribución vidrio":    
				datos = fi.get_comp_by_actividad(search_actividad8)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad8 == "Otros distribuidores especializados":    
				datos = fi.get_comp_by_actividad(search_actividad8)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea2 == "Máquinas y herramientas":
			search_actividad9 = st.selectbox('Selecciona sub-categoria', ["select..","Equipos de protección laboral", "Fabricación de herramientas", "Fabricación de máquinas"])  

			if search_actividad9 == "Equipos de protección laboral":    
				datos = fi.get_comp_by_actividad(search_actividad9)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad9 == "Fabricación de herramientas":    
				datos = fi.get_comp_by_actividad(search_actividad9)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad9 == "Fabricación de máquinas":    
				datos = fi.get_comp_by_actividad(search_actividad9)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea2 == "Distribución máq. y herramientas":
			search_actividad10 = st.selectbox('Selecciona sub-categoria', ["select..","Distribución y alquiler de herramientas", "Distribución y alquiler de maquinaria"])  

			if search_actividad10 == "Distribución y alquiler de herramientas":    
				datos = fi.get_comp_by_actividad(search_actividad10)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad10 == "Distribución y alquiler de maquinaria":    
				datos = fi.get_comp_by_actividad(search_actividad10)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea2 == "Transporte":
			search_actividad11 = st.selectbox('Selecciona sub-categoria', ["select..","Vehículos industriales / comerciales", "Accesorios vehículos industriales / comerciales", "Carretillas / movimiento de cargas", "Transporte mercancía general carretera"])  

			if search_actividad11 == "Vehículos industriales / comerciales":    
				datos = fi.get_comp_by_actividad(search_actividad11)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad11 == "Accesorios vehículos industriales / comerciales":    
				datos = fi.get_comp_by_actividad(search_actividad11)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad11 == "Carretillas / movimiento de cargas":    
				datos = fi.get_comp_by_actividad(search_actividad11)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad11 == "Transporte mercancía general carretera":    
				datos = fi.get_comp_by_actividad(search_actividad11)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea2 == "Central de compras materiales":
			search_actividad12 = st.selectbox('Selecciona sub-categoria', ["select..","Central de compras materiales", "Plataformas mayoristas electro"])  

			if search_actividad12 == "Central de compras materiales":    
				datos = fi.get_comp_by_actividad(search_actividad12)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad12 == "Plataformas mayoristas electro":    
				datos = fi.get_comp_by_actividad(search_actividad12)
				st.dataframe(datos.style.highlight_max(axis=0))



	elif search_area_principal == "Materiales":
		search_subarea3 = st.selectbox('Selecciona categoria', ["select..","Materiales de construcción", "Material eléctrico", "Equipamiento logístico", "Equipamiento doméstico", "Equipamiento comercial", "Equipamiento urbano / vial", "Equipamiento hostelería", "Equipamiento para geriátricos y centros sanitarios", "Envases", "Climatización", "Elevación", "Energía solar", "Equipamiento baño", "Equipos fabricación materiales", "Hierros y carpintería metálica"])


		if search_subarea3 == "Materiales de construcción":
			search_actividad13 = st.selectbox('Selecciona sub-categoria', ["select..","Yeso y escayola", "Ladrillos y tejas","Hormigón","Piedra: mármol, granito y pizarra","Vidrio","Cemento","Otros materiales","Madera","Azulejos y pavimentos","Pintura","Fontanería","Bazar y menaje","Bricolaje","Ferretería","Prefabricados de hormigón","Aislantes e impermeabilizantes","Productos asfálticos","Productos químicos y pinturas"])

			if search_actividad13 == "Yeso y escayola":    
				datos = fi.get_comp_by_actividad(search_actividad13)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad13 == "Ladrillos y tejas":    
				datos = fi.get_comp_by_actividad(search_actividad13)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad13 == "Hormigón":    
				datos = fi.get_comp_by_actividad(search_actividad13)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad13 == "Piedra: mármol, granito y pizarra":    
				datos = fi.get_comp_by_actividad(search_actividad13)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad13 == "Vidrio":    
				datos = fi.get_comp_by_actividad(search_actividad13)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad13 == "Cemento":    
				datos = fi.get_comp_by_actividad(search_actividad13)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad13 == "Otros materiales":    
				datos = fi.get_comp_by_actividad(search_actividad13)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad13 == "Madera":    
				datos = fi.get_comp_by_actividad(search_actividad13)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad13 == "Azulejos y pavimentos":    
				datos = fi.get_comp_by_actividad(search_actividad13)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad13 == "Pintura":    
				datos = fi.get_comp_by_actividad(search_actividad13)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad13 == "Fontanería":    
				datos = fi.get_comp_by_actividad(search_actividad13)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad13 == "Bazar y menaje":    
				datos = fi.get_comp_by_actividad(search_actividad13)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad13 == "Bricolaje":    
				datos = fi.get_comp_by_actividad(search_actividad13)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad13 == "Ferretería":    
				datos = fi.get_comp_by_actividad(search_actividad13)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad13 == "Prefabricados de hormigón":    
				datos = fi.get_comp_by_actividad(search_actividad13)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad13 == "Aislantes e impermeabilizantes":    
				datos = fi.get_comp_by_actividad(search_actividad13)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad13 == "Productos asfálticos":    
				datos = fi.get_comp_by_actividad(search_actividad13)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad13 == "Productos químicos y pinturas":    
				datos = fi.get_comp_by_actividad(search_actividad13)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea3 == "Material eléctrico":
			search_actividad14 = st.selectbox('Selecciona sub-categoria', ["select..","Iluminación", "Electrónica de consumo", "Material eléctrico"])  

			if search_actividad14 == "Iluminación":    
				datos = fi.get_comp_by_actividad(search_actividad14)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad14 == "Electrónica de consumo":    
				datos = fi.get_comp_by_actividad(search_actividad14)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad14 == "Material eléctrico":    
				datos = fi.get_comp_by_actividad(search_actividad14)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea3 == "Equipamiento logístico":
			search_actividad15 = st.selectbox('Selecciona sub-categoria', ["select..","Informática para transporte y logística", "Informática para distribución", "Logística"])  

			if search_actividad15 == "Informática para transporte y logística":    
				datos = fi.get_comp_by_actividad(search_actividad15)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad15 == "Informática para distribución":    
				datos = fi.get_comp_by_actividad(search_actividad15)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad15 == "Logística":    
				datos = fi.get_comp_by_actividad(search_actividad15)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea3 == "Equipamiento doméstico":
			search_actividad16 = st.selectbox('Selecciona sub-categoria', ["select..","Equipamiento doméstico", "Informática (hardware doméstico)", "Software para electro", "Electrodomésticos línea blanca", "P.a.e. (pequeño aparato electrodoméstico)"]) 

			if search_actividad16 == "Equipamiento doméstico":    
				datos = fi.get_comp_by_actividad(search_actividad16)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad16 == "Informática (hardware doméstico)":    
				datos = fi.get_comp_by_actividad(search_actividad16)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad16 == "Software para electro":    
				datos = fi.get_comp_by_actividad(search_actividad16)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad16 == "Electrodomésticos línea blanca":    
				datos = fi.get_comp_by_actividad(search_actividad16)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad16 == "P.a.e. (pequeño aparato electrodoméstico)":    
				datos = fi.get_comp_by_actividad(search_actividad16)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea3 == "Equipamiento comercial":
			search_actividad17 = st.selectbox('Selecciona sub-categoria', ["select..","Equipamiento comercial", "Equipamiento comercial electro"])  

			if search_actividad17 == "Equipamiento comercial":    
				datos = fi.get_comp_by_actividad(search_actividad17)
				st.dataframe(datos.style.highlight_max(axis=0))
	
			if search_actividad17 == "Equipamiento comercial electro":    
				datos = fi.get_comp_by_actividad(search_actividad17)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea3 == "Equipamiento urbano / vial":
			search_actividad18 = st.selectbox('Selecciona sub-categoria', ["select..","Equipamiento urbano / vial"]) 

			if search_actividad18 == "Equipamiento urbano / vial":    
				datos = fi.get_comp_by_actividad(search_actividad18)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea3 == "Equipamiento hostelería":
			search_actividad19 = st.selectbox('Selecciona sub-categoria', ["select..","Proveedores de equipamiento a hostelería ", "Hardware para hostelería (TPVs, etc)", "Informática para hostelería", "Mobiliario para hostelería", "Minibares y armarios bodega"]) 

			if search_actividad19 == "Proveedores de equipamiento a hostelería ":    
				datos = fi.get_comp_by_actividad(search_actividad19)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad19 == "Hardware para hostelería (TPVs, etc)":    
				datos = fi.get_comp_by_actividad(search_actividad19)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad19 == "Informática para hostelería":    
				datos = fi.get_comp_by_actividad(search_actividad19)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad19 == "Mobiliario para hostelería":    
				datos = fi.get_comp_by_actividad(search_actividad19)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad19 == "Minibares y armarios bodega":    
				datos = fi.get_comp_by_actividad(search_actividad19)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea3 == "Equipamiento para geriátricos y centros sanitarios":
			search_actividad20 = st.selectbox('Selecciona sub-categoria', ["select..","Muebles y equipamientos para centros sanitarios / geriátricos", "Otros equipamientos para geriátricos y centros sanitarios"])  

			if search_actividad20 == "Muebles y equipamientos para centros sanitarios / geriátricos":    
				datos = fi.get_comp_by_actividad(search_actividad20)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad20 == "Otros equipamientos para geriátricos y centros sanitarios":    
				datos = fi.get_comp_by_actividad(search_actividad20)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea3 == "Envases":
			search_actividad21 = st.selectbox('Selecciona sub-categoria', ["select..","Envases / embalajes de EPS-embalajes de protección", "Cajas-contenedores-palés de plástico"])  

			if search_actividad21 == "Envases / embalajes de EPS-embalajes de protección":    
				datos = fi.get_comp_by_actividad(search_actividad21)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad21 == "Cajas-contenedores-palés de plástico":    
				datos = fi.get_comp_by_actividad(search_actividad21)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea3 == "Climatización":
			search_actividad22 = st.selectbox('Selecciona sub-categoria', ["select..","Climatización", "Climatización doméstica", "Calefacción doméstica", "Frío comercial"])  

			if search_actividad22 == "Climatización":    
				datos = fi.get_comp_by_actividad(search_actividad22)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad22 == "Climatización doméstica":    
				datos = fi.get_comp_by_actividad(search_actividad22)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad22 == "Calefacción doméstica":    
				datos = fi.get_comp_by_actividad(search_actividad22)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad22 == "Frío comercial":    
				datos = fi.get_comp_by_actividad(search_actividad22)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea3 == "Elevación":
			search_actividad23 = st.selectbox('Selecciona sub-categoria', ["select..","Elevación"]) 

			if search_actividad23 == "Elevación":    
				datos = fi.get_comp_by_actividad(search_actividad23)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea3 == "Energía solar":
			search_actividad23 = st.selectbox('Selecciona sub-categoria', ["select..","Equipos de energía para construcción"]) 

			if search_actividad23 == "Equipos de energía para construcción":    
				datos = fi.get_comp_by_actividad(search_actividad23)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea3 == "Equipamiento baño":
			search_actividad24 = st.selectbox('Selecciona sub-categoria', ["select..","Grifería", "Mobiliario de baño", "Calefacción doméstica", "Sanitarios"]) 
			
			if search_actividad24 == "Grifería":    
				datos = fi.get_comp_by_actividad(search_actividad24)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad24 == "Mobiliario de baño":    
				datos = fi.get_comp_by_actividad(search_actividad24)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad24 == "Sanitarios":    
				datos = fi.get_comp_by_actividad(search_actividad24)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea3 == "Equipos fabricación materiales":
			search_actividad25 = st.selectbox('Selecciona sub-categoria', ["select..","Equipos fabricación de cemento", "Equipos fabricación de hierros y carp. metálica","Equipos fabricación de hormigón y prefabricados","Equipos fabricación de madera","Equipos fabricación de materiales","Equipos fabricación de materiales plásticos","Equipos fabricación de varios sectores","Equipos fabricación de vidrio","Equipos / maquinaria para industria materiales","Maquinaria formadora de envases"])

			if search_actividad25 == "Equipos fabricación de cemento":    
				datos = fi.get_comp_by_actividad(search_actividad25)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad25 == "Equipos fabricación de hierros y carp. metálica":    
				datos = fi.get_comp_by_actividad(search_actividad25)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad25 == "Equipos fabricación de hormigón y prefabricados":    
				datos = fi.get_comp_by_actividad(search_actividad25)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad25 == "Equipos fabricación de madera":    
				datos = fi.get_comp_by_actividad(search_actividad25)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad25 == "Equipos fabricación de materiales":    
				datos = fi.get_comp_by_actividad(search_actividad25)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad25 == "Equipos fabricación de materiales plásticos":    
				datos = fi.get_comp_by_actividad(search_actividad25)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad25 == "Equipos fabricación de varios sectores":    
				datos = fi.get_comp_by_actividad(search_actividad25)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad25 == "Equipos fabricación de vidrio":    
				datos = fi.get_comp_by_actividad(search_actividad25)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad25 == "Equipos / maquinaria para industria materiales":    
				datos = fi.get_comp_by_actividad(search_actividad25)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad25 == "Maquinaria formadora de envases":    
				datos = fi.get_comp_by_actividad(search_actividad25)
				st.dataframe(datos.style.highlight_max(axis=0))


		if search_subarea3 == "Hierros y carpintería metálica":
			search_actividad26 = st.selectbox('Selecciona sub-categoria', ["select..","Cerrajería y carpintería metálica", "Hierros", "Siderurgia", "Panel y chapa", "Perfiles metálicos y de PVC", "Puertas y ventanas metálicas / PVC"]) 

			if search_actividad26 == "Cerrajería y carpintería metálica":    
				datos = fi.get_comp_by_actividad(search_actividad26)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad26 == "Hierros":    
				datos = fi.get_comp_by_actividad(search_actividad26)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad26 == "Siderurgia":    
				datos = fi.get_comp_by_actividad(search_actividad26)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad26 == "Panel y chapa":    
				datos = fi.get_comp_by_actividad(search_actividad26)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad26 == "Perfiles metálicos y de PVC":    
				datos = fi.get_comp_by_actividad(search_actividad26)
				st.dataframe(datos.style.highlight_max(axis=0))

			if search_actividad26 == "Puertas y ventanas metálicas / PVC":    
				datos = fi.get_comp_by_actividad(search_actividad26)
				st.dataframe(datos.style.highlight_max(axis=0))



#-----------------------------------------EXPLORA---------------------------------------------------------------------------------

if choice == "EXPLORA":
	st.header("¿Qué deseas saber?")
	st.text("")
	st.subheader("Número de empleados")

	company_data = vi.load_data()

	st.subheader('Compañías')
	st.write(company_data)

	st.subheader('Países con compañías:')
	st.dataframe(vi.grafico_barras_pais())
	datos = vi.grafico_barras_pais()
	st.bar_chart(datos)

	st.subheader('Top 30 provincias con compañías:')
	st.dataframe(vi.grafico_barras_provincia())
	datos = vi.grafico_barras_provincia()
	st.bar_chart(datos)

	st.subheader("Actividades")
	st.dataframe(vi.grafico_barras_actividad())
	datos = vi.grafico_barras_actividad()
	st.bar_chart(datos)





	busca_empleados = st.text_input('Introduce el nombre de la empresa')
	if busca_empleados == {f"busca_empleados"}:
		datos = vi.empleados(busca_empleados)
		st.bar_chart(datos)






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


#-----------------------------------------NUEVO PERFIL---------------------------------------------------------------------------------


if choice == "NUEVO PERFIL":
	empresa_col.header("Conviertete en parte de la comunidad Triente")
	st.text("")
	empresa_col.subheader("Información Empresa")
	try:
		perfil_nuevo = {}

	#------------------------------------------FILA 1------------------------------------------------------	
		with empresa_col1:
			perfil_nuevo['razon_social'] = st.text_input('Razón Social *')
			perfil_nuevo['CIF'] = st.text_input('CIF *')

		with empresa_col2:
			perfil_nuevo['telefono'] = st.text_input('Teléfono')
			perfil_nuevo['email'] = st.text_input('Email')
			perfil_nuevo['web'] = st.text_input('WEB')

	#------------------------------------------FILA 2------------------------------------------------------
		st.text("")

		with direccion_col1:
			perfil_nuevo['domicilio'] = st.text_input('Domicilio')
			perfil_nuevo['codigo_postal'] = st.text_input('Código Postal')
		with direccion_col2:
			perfil_nuevo['provincia'] = st.text_input('Provincia *')
			perfil_nuevo['pais'] = st.text_input('País *')

		st.text("")
	#------------------------------------------FILA 3------------------------------------------------------

		perfil_nuevo['cnae'] = st.text_input('CNAE')	
		perfil_nuevo['area_principal'] = st.selectbox('Selecciona área principal *', ["select..","Proyectos inmobiliarios","Distribución","Materiales"])		
		perfil_nuevo['descripcion_actividad'] =  st.text_area("Descripción actividad", max_chars=300)


		st.button('Añadir Perfil')
		if perfil_nuevo['razon_social'] != '' and perfil_nuevo['CIF'] != '' and perfil_nuevo['Provincia'] != '' and perfil_nuevo['País'] != '' and perfil_nuevo['area_principal'] != '':
				try:
					fi.add_profile(perfil_nuevo)
					st.success('Perfil añadido con éxito!')
					st.balloons()
				except:
					st.warning('No se ha añadido el perfil exitosamente *')
	except:
		st.warning('Recuerda que hay campos olbligatorios *')


