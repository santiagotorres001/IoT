'''
API: Application Programming Interface
Nasa API: https://api.nasa.gov

Ruta aleatoria de API Nasa
https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={H6DcXN4k0GjgogigilANSzbf1QqVebU2L8vqdfxv}
'''
       
'''
Script description: Get all data about Solar System
Developer: Santiago Torres

'''
import os
import requests
import json

def get_data(opcion):
    url = "https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key=H6DcXN4k0GjgogigilANSzbf1QqVebU2L8vqdfxv"
   
    try:
       
        res = requests.get(url)
        res.raise_for_status()  
        data = res.json() 

        if opcion == 1: 
            filtered_data = {"name": data.get('name', 'No disponible')}

        elif opcion == 2:  
            filtered_data = {"absolute_magnitude_h": data.get('absolute_magnitude_h', 'No disponible')}

        elif opcion == 3: 
            diameter_max_km = data.get('estimated_diameter', {}).get('kilometers', {}).get('estimated_diameter_max', 'No disponible')
            filtered_data = {"estimated_diameter_max_km": diameter_max_km}

        elif opcion == 4: 
            diameter_max_ft = data.get('estimated_diameter', {}).get('feet', {}).get('estimated_diameter_max', 'No disponible')
            filtered_data = {"estimated_diameter_max_ft": diameter_max_ft}

        elif opcion == 5:
            filtered_data = {
                "name": data.get('name', 'No disponible'),
                "absolute_magnitude_h": data.get('absolute_magnitude_h', 'No disponible'),
                "estimated_diameter_max_km": data.get('estimated_diameter', {}).get('kilometers', {}).get('estimated_diameter_max', 'No disponible'),
                "estimated_diameter_max_ft": data.get('estimated_diameter', {}).get('feet', {}).get('estimated_diameter_max', 'No disponible')
            }

        else:
            print("Opción inválida")
            return


        print(json.dumps(filtered_data, indent=4))


    except requests.exceptions.RequestException as e:
        print(f"Error en la conexión a la API: {e}")

while True:
    print("\n::: Menú de opciones :::")
    print("1. Visualiza el nombre del NEO.")
    print("2. Visualiza la magnitud absoluta del NEO.")
    print("3. Visualiza el máximo diámetro estimado en kilómetros.")
    print("4. Visualiza el máximo diámetro estimado en pies.")
    print("5. Visualiza toda la información anterior.")
    print("0. Salir")

    opcion = int(input("Elige una opción (0 para salir): "))

    if opcion == 0:
        print("Saliendo del programa...")
        break
  
    get_data(opcion)
