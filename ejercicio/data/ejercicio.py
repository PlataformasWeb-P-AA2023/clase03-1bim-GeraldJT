

archivo =  open ('/home/salab/Escritorio/ejercicios/clase03-1bim-GeraldJT/ejercicio/data/Listado-Instituciones-Educativas-distribuidas-por-zona-distrito-y-circuito.csv')
lineas = archivo.readlines()
  
for row in lineas :
  file = open('/home/salab/Escritorio/ejercicios/clase03-1bim-GeraldJT/ejercicio/data/columna.html','w')
  row = row.split("|")
  codigo = """
    <!DOCTYPE html>
  <html>
  <head>
	  <meta charset="utf-8">
	  <meta name="viewport" content="width=device-width, initial-scale=1">
	  <title></title>
</head>
<body>
	<h1>Nombre de la institución</h1>
	<h2>row[1]</h2>
	<hr>
	<h3>datos relevantes</h3>
	<hr>
	<h4>Provincia: row[3]</h4>
	<h4>Canton: row[5]</h4>
	<h4>Parroquia: row[7]</h4>
	<hr>
	<h5>autor @gerald</h5>
</body>
</html>
  print(row[0])
"""
archivo.write(codigo)
archivo.close()