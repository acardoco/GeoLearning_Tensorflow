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
import time

#ya descargadas y etiquetadas
regiones_v1 =[
{'region': 'leganes_izq1','anchura':5,'altura':5,'lat':40.3434744, 'lon':-3.7869616},
{'region': 'parking_Madrid','anchura':5,'altura':2,'lat':40.4620443, 'lon':-3.8091003},
{'region': 'Santander ','anchura':5,'altura':3,'lat':43.4580609, 'lon':-3.8590527},
{'region': 'leganes_parkings ','anchura':6,'altura':5,'lat':40.3404043, 'lon':-3.7387991},
{'region': 'leganes_derecha_abajo ','anchura':3,'altura':10,'lat':40.3312774, 'lon':-3.7344782},
{'region': 'leganes_derecha_abajo_2','anchura':5,'altura':5,'lat':40.3033989, 'lon':-3.7583494},
{'region': 'Madrid_norte','anchura':5,'altura':6,'lat':40.5583232, 'lon':-3.6624752},
{'region': 'Madrid_norte_2','anchura':10,'altura':10,'lat':40.5646439, 'lon':-3.6254172},
{'region': 'Parking_Ikea_Madrid_Este','anchura':4,'altura':7,'lat':40.5461507, 'lon':-3.6179065}]

#ya descargadas y etiquetadas
regiones_v2 =[
{'region': 'zapateira','anchura':3,'altura':4,'lat':43.3192505, 'lon': -8.4123571},
{'region': 'fuenlabrada_noroeste','anchura':3,'altura':5,'lat':40.3053734, 'lon':-3.8437664},
{'region': 'alcorcon_sur','anchura':5,'altura':5,'lat':40.3418746, 'lon':-3.8455331},
{'region': 'villaviciosa_noreste','anchura':4,'altura':4,'lat':40.3687954, 'lon':-3.8874207},
{'region': 'pozuelo_sureste','anchura':3,'altura':3,'lat':40.4478637,'lon':-3.7910613},
{'region': 'fuentelareyna','anchura':5,'altura':2,'lat':40.479813,'lon': -3.7381079}
 ]

# url
base = 'https://maps.googleapis.com/maps/api/staticmap?center='
parametros_comunes = '&zoom=18&format=jpg&size=640x640&maptype=satellite&ket='
key = 'AIzaSyB9qW-QzzGtT2xEsJlsuLgA5TOYNJS8ogo'
repositorio = 'data\downloaded_v2\\'
arriba = 0.0026700
derecha = 0.0035100

def obtenerImagen(nombre, lat, lon):

    url_rquest = base + lat.__str__() + ','+ lon.__str__() + parametros_comunes + key
    urlr.urlretrieve(url_rquest, repositorio + nombre + '_' + lat.__str__() + '_' + lon.__str__() +'.jpg')
    print(url_rquest)

def obtener_imagenes(nombre ,lat_partida, lon_partida, altura, anchura):


    lat = lat_partida
    lon = lon_partida

    img_des = 0

    for i in range(0,anchura):
        for j in range(0,altura):
            obtenerImagen(nombre, lat,lon)
            lat = round(lat - arriba,7)
            img_des +=1
            '''if (img_des%10 ==0):
                time.sleep(10)  # delay de 10 segundos'''
        lat = lat_partida
        lon = round(lon + derecha,7)
    print('Imagenes descargadas: ', img_des)

    return img_des

def leer_dicc(dicc):

    total_img = 0

    for region in dicc:
        print('Region: ',region['region'])
        total_img +=obtener_imagenes(region['region'],region['lat'],region['lon'],region['altura'],region['anchura'])
        #total_img +=region['anchura']*region['altura']

    print('Imagenes totales descargadas: ', total_img)




if __name__ == "__main__":
    leer_dicc(regiones_v2)