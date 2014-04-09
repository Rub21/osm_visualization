### Procesamiento de archivos 
Es posible descargar archivos de osm de las mejoras , por dia en :
Descargar de http://planet.openstreetmap.org/replication/day/000/000/

Pero para descargar mas rapido estos es bueno utilizar:

https://github.com/Rub21/osm_visualization/blob/master/data/retrieve-day

ejecutar:


		ruben@rub21:~/Apps/visualization/data$ ./retrieve-day


basado en: https://github.com/ericfischer/ebola/blob/master/retrieve-hourly

se tiene que configurar de fecha a que fecha se quiere:

por ejemplo:

se quiere trabajar desde : 01/09/2014 a 04/09/2014 que corresponde a 484 a 574


una ves descargado todos los archivos para la visualizacion:

se tiene que poner configurar el BBox del archivo, en este caso para San Francisco.
https://github.com/Rub21/osm_visualization/blob/master/data/get-sf-edits

		$minlat = 37.716045;
		$minlon = -122.51781;
		$maxlat = 37.817006;
		$maxlon = -122.34924;


que es para la creacion de de Gejson: modificado del archivo: https://github.com/ericfischer/ebola/blob/master/get-mamou-edits

Se puede ejecutar para una solo archivo:

		ruben@rub21:~/Apps/visualization/data$ ./get-sf-edits 485.osc.gz > sf485.geojson

pero su se quiere se puede ejecutar todos los archivos 

configurando la siguinete line con el nuemor de archivos que hay:
https://github.com/Rub21/osm_visualization/blob/master/data/process_all#L3

 en mi caso modifico de 484 a 574, y ejecuto:


		ruben@rub21:~/Apps/visualization/data$ ./process_all


 tomara algunos minutos procesar todos los archivos, al final se tendra archivos en geojson










