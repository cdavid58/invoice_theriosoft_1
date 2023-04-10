import sqlite3
list_category = [
	'Accesorios para Vehículos','Agro','Alimentos y Bebidas','Regalos','Animales y Mascotas','Antigüedades y Colecciones','Arte, Papelería y Mercería','Bebés',
'Belleza y Cuidado Personal','Celulares y Teléfonos','Computación','Consolas y Videojuegos','Construcción','Deportes y Fitness','Electrodomésticos','Electrónica, Audio y Video',
'Herramientas','Hogar y Muebles','Industrias y Oficinas','Inmuebles','Instrumentos Musicales','Juegos y Juguetes','Recuerdos, Piñatería y Fiestas','Ropa y Accesorios','Salud y Equipamiento Médico',
'Servicios','Otras categorías'
]

connect = sqlite3.connect('db.sqlite3')
cursor = connect.cursor()
for i in list_category:
	query = "insert into inventory_category(name)values(?)"
	args = (i,)
	print(i)
	cursor.execute(query,args)
connect.commit()


