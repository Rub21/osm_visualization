osm_visualization
=================

Creacion de un gif de los avances en OSM,para esto se utiliza, [Projectmill](https://github.com/mapbox/projectmill)

### Creacion de datos de geojson

para los generar los datos ir a : https://github.com/Rub21/osm_visualization/tree/master/data


### Optener Imagen Satelital

para esto utilizamos le herramienta https://github.com/ericfischer/tile-stitch

ejecutamos de la siguiente forma:

		ruben@rub21:~/Apps/tile-stitch$ ./stitch -o sf.png -- 37.6787  -122.5171 37.8270 -122.3338 13 http://a.tiles.mapbox.com/v3/openstreetmap.map-4wvf9l0l/{z}/{x}/{y}.png

#### optener imagenes de progresos diarios:

Para crear el archivo config.json, copiar  el archivo https://github.com/Rub21/osm_visualization/blob/master/make-config.py  en la carpeta de Projectmill y configurar los los parametros:

    project={
            "source": "sf",
            "destination": "sf"+ str(x),
            "format": "png",
            "minzoom": 1,
            "maxzoom": 16,
            "width":1068,
            "height":1093,
            "mml": {
                    "Layer": [
                      {                                        
                                  "Datasource": {
                                  "file": "/home/ruben/Apps/visualization/data/sf"+str(x)+".geojson"
                                }
                  
                      }
                    ],
                    "advanced": {},
                    "name": "nd"+ str(x)
               
                  }
        }

Preferentemente agrgar las dimenciones de la imagen satelital y el mismo zoom alque se exporto la imagen satelital:

           "width":1068,
           "height":1093,

y ejecutar:


		ruben@rub21:~/Apps/visualization/projectmill$ python config.py 484 574

Luego se creara el archivo config.json ,y luego ejecutar:

		ruben@rub21:~/Apps/visualization/projectmill$ ./index.js --mill  --render  -c config.json -f -t /usr/share/tilemill

se crearan lo archivos los proyectos en Tilemill y las imagenes en la carpeta export

#### crear imagen Gif:

para ejecutar el gif nombramos la imagen satelital con un numero menor del primer archivos que procesamos:

	Ejemplo:

		la primera imagen esprocesada del archivo procesado es: sf484.png , entonces renombrar la imagen satelital a sf483.png

luego: ejecutar los siguintes comandos:

	ruben@rub21:~/Documents/MapBox/export$ mogrify -format gif *.png && gifsicle *.gif > anim.gif
	ruben@rub21:~/Documents/MapBox/export$ gifsicle --loop=0 --colors 256 *.gif > anim.gif

Finalmente optenemos el la imagen animada:

![](https://cloud.githubusercontent.com/assets/1152236/2662166/48d7280c-c038-11e3-94fd-05002489803d.gif)








