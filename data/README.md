### Download the OSM files 
Descargar Archivos de OSM de la mejoras diarias: http://planet.openstreetmap.org/replication/day/000/000/

https://github.com/Rub21/osm_osm_visualization/blob/master/data/retrieve-day

Ejecutar:

		$ ./retrieve-day arg1 arg2

donde:
arg1 is: 01/09/2014 = 484 (start file)
arg2 is: 04/09/2014 = 574 (end file)
script basado en: https://github.com/ericfischer/ebola/blob/master/retrieve-hourly

		ruben@rub21:~/osm_visualization/data$ ./retrieve-day 448 574

### Convert datos to Geojson

Se usa: https://github.com/Rub21/osm_osm_visualization/blob/master/data/get-sf-edits:
modificado de: https://github.com/ericfischer/ebola/blob/master/get-mamou-edits

Ejecutar: 

	$ ./get-sf-edits file minlat minlon maxlat maxlon > newfile.geojson

Example:
Bounds from San Francisco:

		$minlat = 37.716045;
		$minlon = -122.51781;
		$maxlat = 37.817006;
		$maxlon = -122.34924;

Ejecuta para un archivo:
		
		ruben@rub21:~/osm_visualization/data$ ./get-edits 485.osc.gz 37.716045 -122.51781 37.817006 -122.34924 > sf485.geojson


Es posible ejecutar todos los archivos con una solo line de comando:

	$ ./process_all start_file end_file minlat minlon maxlat maxlon


Example: 

	ruben@rub21:~/osm_visualization/data$ ./process_all 499 500 37.716045 -122.51781 37.817006 -122.34924 

It will take a while depending on the number of files are.










