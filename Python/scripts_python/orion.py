'''
Script description: Get all data about Solar System
Developer: Santiago Torres

'''
import os
import requests
import json

def get_data(opcion):
    url = "https://api.le-systeme-solaire.net/rest/bodies/"

    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()['bodies']

        if opcion == 1: 
            filtered_data = [body for body in data if 'Planet' in body.get('bodyType', '')]
        elif opcion == 2:
            filtered_data = [body for body in data if 'Moon' in body.get('bodyType', '')]
        elif opcion == 3:
            filtered_data = [body for body in data if 'Star' in body.get('bodyType', '')]
        elif opcion == 4:
            filtered_data = [body for body in data if 'Asteroid' in body.get('bodyType', '')]
        elif opcion == 5: 
            filtered_data = [body for body in data if 'Comet' in body.get('bodyType', '')]
        elif opcion == 6: 
            filtered_data = [body for body in data if 'Dwarf Planet' in body.get('bodyType', '')]
        else:
            print("Opción inválida")
            return

        print(json.dumps(filtered_data, indent=4))

    except requests.exceptions.RequestException as e:
        print(f"Error en la conexión a la API: {e}")

while True:
    print("\n::: Menú de opciones :::")
    print("1. Visualiza toda la información de planetas")
    print("2. Visualiza toda la información de lunas")
    print("3. Visualiza toda la información de estrellas")
    print("4. Visualiza toda la información de asteroides")
    print("5. Visualiza toda la información de cometas")
    print("6. Visualiza toda la información de planetas enanos")
    print("0. Salir")

    opcion = int(input("Elige una opción (0 para salir): "))

    if opcion == 0:
        print("Saliendo del programa...")
        break

    get_data(opcion)
