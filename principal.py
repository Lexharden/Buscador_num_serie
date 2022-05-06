import os
import re
import datetime
import time
from pathlib import Path
import math

base = os.path.join(os.getcwd(), 'Mi_Gran_Directorio')
base_patron = re.compile(r'(N\D{3})-(\d{5})')
fecha = datetime.date.today()
numeros = []
archivos_encontrados = []


def recorrer_carpetas():
    for carpetas, subcarp, archivos in os.walk(base):
        for archivo in archivos:
            result = buscar_numeros(Path(carpetas, archivo), base_patron)
            if result != '':
                numeros.append(result.group())
                archivos_encontrados.append(archivo.title())


def buscar_numeros(archivo, patron):
    new_archivo = open(archivo, 'r')
    text = new_archivo.read()
    if re.search(patron, text):
        return re.search(patron, text)
    else:
        return ''


def inciar():
    indice = 0
    print(f'Fecha de hoy: {fecha.day}/{fecha.month}/{fecha.year} ')
    print('_' * 30)
    print(f'| ARCHIVO \t\t NO° SERIE |')
    print(f'_' * 30)
    incio = time.time()
    for i in archivos_encontrados:
        print(f'| {i} | {numeros[indice]} |')
        print(f'_'*30)
        indice += 1
    final = time.time()
    print(f'Numeros encontrados: {len(numeros)}')
    tiempo = (final - incio)
    print(f'Duracion de la busqueda: {math.ceil(tiempo)} s')


recorrer_carpetas()
inciar()
