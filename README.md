osm_visualization
=================
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

  ruben@rub21:~/osm_visualization/data$ ./process_all 484 574 37.716045 -122.51781 37.817006 -122.34924 

It will take a while depending on the number of files are.

 ### Creating png files

 You need to install [Tilemill](https://www.mapbox.com/tilemill), and  clone [Projectmill](https://github.com/mapbox/projectmill)

      git clone https://github.com/mapbox/projectmill.git

#### Get a background PNG File:

In this case we need satelital imagen : 

we use  ericfischer' project [tile-stitch](https://github.com/ericfischer/tile-stitch), cloning in your machine an run:

    
    ruben@rub21:~/tile-stitch$ ./stitch -o sf.png -- 37.6787  -122.5171 37.8270 -122.3338 13 http://a.tiles.mapbox.com/v3/openstreetmap.map-4wvf9l0l/{z}/{x}/{y}.png

then we check the size of imagen: in my cas is :  "width":1068, "height":1093

#### Create a project in Tilemill:
I create a project in Tilemill called sfbuildings: https://github.com/Rub21/osm_visualization/tree/master/tilemill-project/sfbuildings

#### Do a config.json file
we nned to configure this file https://github.com/Rub21/osm_visualization/blob/master/make-config.py :
the exact line is:

    project={
            "source": "sfbuildings",
            "destination": "sf"+ str(x),
            "format": "png",
            "minzoom": 1,
            "maxzoom": 16,
            "width":1068, #it is a width form satelital imagen
            "height":1093, #it is a height form satelital imagen
            "mml": {
                    "Layer": [
                      {                                        
                                  "Datasource": {
                                  "file": "/home/ruben/visualization/data/sf"+str(x)+".geojson"
                                }
                  
                      }
                    ],
                    "advanced": {},
                    "name": "line"+ str(x)
               
                  }
        }

Run:

    ruben@rub21:~/visualization/projectmill$ python config.py 484 574


   	ruben@rub21:~/Apps/visualization/projectmill$ ./index.js --mill  --render  -c config.json -f -t /usr/share/tilemill

se crearan lo archivos los proyectos en Tilemill y las imagenes en la carpeta export

#### crear imagen Gif:

para ejecutar el gif nombramos la imagen satelital con un numero menor del primer archivos que procesamos:

	Ejemplo:

		la primera imagen esprocesada del archivo procesado es: sf484.png , entonces renombrar la imagen satelital a sf483.png

luego: ejecutar los siguintes comandos:

	ruben@rub21:~/Documents/MapBox/export$ mogrify -format gif *.png && gifsicle *.gif > anim.gif
	ruben@rub21:~/Documents/MapBox/export$ gifsicle --loop=0 --colors 256 *.gif > anim.gif

fuente:
http://www.lcdf.org/gifsicle/man.html
Finalmente optenemos el la imagen animada:

![](https://cloud.githubusercontent.com/assets/1152236/2662166/48d7280c-c038-11e3-94fd-05002489803d.gif)








