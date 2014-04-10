from sys import argv
from datetime import datetime
import time
import json

if (len(argv) < 3):
    print "ingrese el nuemor del archivo el menor y despues el mayor"
    exit()

config_json=[]


for x in range(int(argv[1]), int(argv[2])+1):
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

    config_json.append(project)


print 'saving geojson'

json.dump(config_json, open('config.json', 'w'))