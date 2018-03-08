#creador de data
'''Ejemplo --> https://maps.googleapis.com/maps/api/staticmap?center=40.3328353,-3.7785943&scale=2
&zoom=18&format=jpg&size=640x640&maptype=satellite&key=AIzaSyDzqBTBX6dQUG98RLaspplZ-WKam3h87Pg


40.3325643,-3.7786665,305
40.3350814,-3.7790878,306
Moverse hacia arriba
25171		4213


Ejemplo 1280x1280 (lo de scale=2):

40.3325353,-3.7785943
[+|-]26700 en latitud para moverse arriba o abajo
40.3352053,-3.7785943


[+|-]35100 en longitud para moverse derecha o izquierda
40.3352053,-3.7821043


'''

import urllib.request as urlr

regiones =[{'region': 'leganes_izq1','anchura':5,'altura':5,'lat':40.3434744, 'lon':-3.7869616}
           ]

# url
base = 'https://maps.googleapis.com/maps/api/staticmap?center='
parametros_comunes = '&zoom=18&format=jpg&size=640x640&maptype=satellite&ket='
key = 'AIzaSyDzqBTBX6dQUG98RLaspplZ-WKam3h87Pg'
repositorio = 'data\downloaded\\'
arriba = 0.0026700
derecha = 0.0035100

def obtenerImagen(lat, lon):

    url_rquest = base + lat.__str__() + ','+ lon.__str__() + parametros_comunes + key
    urlr.urlretrieve(url_rquest, repositorio + lat.__str__() + '_' + lon.__str__() +'.jpg')
    print(url_rquest)

def obtener_imagenes(lat_partida, lon_partida, altura, anchura):


    lat = lat_partida
    lon = lon_partida

    for i in range(0,anchura):
        for j in range(0,altura):
            obtenerImagen(lat,lon)
            lat = round(lat - arriba,7)
        lat = lat_partida
        lon = round(lon + derecha,7)

def leer_dicc(dicc):

    for region in dicc:
        obtener_imagenes(region['lat'],region['lon'],region['altura'],region['anchura'])




if __name__ == "__main__":
    leer_dicc(regiones)