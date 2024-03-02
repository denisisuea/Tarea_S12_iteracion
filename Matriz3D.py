# SEMANA 12 Iteración de arreglos multidimensionales con bucles anidados

#Crear Una Matriz 3D
# 1era Dimensión diferentes ciudades
# 2da Dimensión días de las semanas (Lunes, Martes, Miércoles, etc)
# 3era Dimensión, semanas
'''Cada celda de la matriz, almacenar temperaturas diarias para una ciudad en un día específico de una semana determinada'''
'''Utilizar bucles anidado para calcular el promedio de temperaturas para una ciudad por cada una de las semanas'''

matriz3D_temperaturas = [
	#Ciudad 1 El Coca 
	[
		# Semana 1 
		[
			{"Día": "Lunes", "temp": 92}, # lUNES
			{"Día": "Martes", "temp": 88}, # MARTES
			{"Día": "Miércoles", "temp": 85}, # MIÉRCOLES
			{"Día": "Jueves", "temp": 79}, # JUEVES
			{"Día": "Viernes", "temp": 82}, # VIERNES
			{"Día": "Sábado", "temp": 80}, # SÁBADO
			{"Día": "Domingo", "temp": 78} # DOMINGO
		],
		# Semana 2
		[
			{"Día": "Lunes", "temp": 83}, # lUNES
			{"Día": "Martes", "temp": 89}, # MARTES
			{"Día": "Miércoles", "temp": 87}, # MIÉRCOLES
			{"Día": "Jueves", "temp": 81}, # JUEVES
			{"Día": "Viernes", "temp": 83}, # VIERNES
			{"Día": "Sábado", "temp": 79}, # SÁBADO
			{"Día": "Domingo", "temp": 76} # DOMINGO
		],
		# Semana 3
		[
			{"Día": "Lunes", "temp": 95}, # lUNES
			{"Día": "Martes", "temp": 91}, # MARTES
			{"Día": "Miércoles", "temp": 88}, # MIÉRCOLES
			{"Día": "Jueves", "temp": 82}, # JUEVES
			{"Día": "Viernes", "temp": 85}, # VIERNES
			{"Día": "Sábado", "temp": 81}, # SÁBADO
			{"Día": "Domingo", "temp": 78} # DOMINGO
		],
		# Semana 4
		[
			{"Día": "Lunes", "temp": 91}, # lUNES
			{"Día": "Martes", "temp": 87}, # MARTES
			{"Día": "Miércoles", "temp": 84}, # MIÉRCOLES
			{"Día": "Jueves", "temp": 79}, # JUEVES
			{"Día": "Viernes", "temp": 80}, # VIERNES
			{"Día": "Sábado", "temp": 78}, # SÁBADO
			{"Día": "Domingo", "temp": 75} # DOMINGO
		]
	],

	# Ciudad 2 Quito
	[
		# Semana 1 
		[
			{"Día": "Lunes", "temp": 79}, # lUNES
			{"Día": "Martes", "temp": 75}, # MARTES
			{"Día": "Miércoles", "temp": 73}, # MIÉRCOLES
			{"Día": "Jueves", "temp": 70}, # JUEVES
			{"Día": "Viernes", "temp": 68}, # VIERNES
			{"Día": "Sábado", "temp": 64}, # SÁBADO
			{"Día": "Domingo", "temp": 62} # DOMINGO
		],
		# Semana 2
		[
			{"Día": "Lunes", "temp": 81}, # lUNES
			{"Día": "Martes", "temp": 77}, # MARTES
			{"Día": "Miércoles", "temp": 75}, # MIÉRCOLES
			{"Día": "Jueves", "temp": 72}, # JUEVES
			{"Día": "Viernes", "temp": 70}, # VIERNES
			{"Día": "Sábado", "temp": 66}, # SÁBADO
			{"Día": "Domingo", "temp": 63} # DOMINGO
		],
		# Semana 3
		[
			{"Día": "Lunes", "temp": 80}, # lUNES
			{"Día": "Martes", "temp": 76}, # MARTES
			{"Día": "Miércoles", "temp": 72}, # MIÉRCOLES
			{"Día": "Jueves", "temp": 70}, # JUEVES
			{"Día": "Viernes", "temp": 68}, # VIERNES
			{"Día": "Sábado", "temp": 65}, # SÁBADO
			{"Día": "Domingo", "temp": 61} # DOMINGO
		],
		# Semana 4
		[
			{"Día": "Lunes", "temp": 80}, # lUNES
			{"Día": "Martes", "temp": 77}, # MARTES
			{"Día": "Miércoles", "temp": 74}, # MIÉRCOLES
			{"Día": "Jueves", "temp": 71}, # JUEVES
			{"Día": "Viernes", "temp": 69}, # VIERNES
			{"Día": "Sábado", "temp": 67}, # SÁBADO
			{"Día": "Domingo", "temp": 64} # DOMINGO
		]
	]

]

# Calcular el promedio de temperaturas para ciudad y semana
ciudades =  ["Ciudad El Coca", "Ciudad Quito"]
for ciudad_idx, ciudad in enumerate(matriz3D_temperaturas):
	for semana_idx, semana in enumerate(ciudad):
		suma_temperaturas = sum([dia["temp"] for dia in semana])
		promedio = suma_temperaturas / len(semana)
		print(f"Promedio de temperturas en la {ciudades[ciudad_idx]}, Semana {semana_idx +1}: {promedio:.2f} grados")

	