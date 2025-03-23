"""
Intentar descargar archivos con nombres de países en inglés y años al final
"""

import requests

# URL base
base_url = "https://www.stampalbums.com/pages/"

# Lista de nombres de países en inglés (en minúsculas)
country = input("Ingrese el nombre: ")

# Generar nombres de archivo con años al final
def generate_file_names(country, years, extension=".pdf"):
    for year in years:
            yield f"{country}{year}{extension}"

# Descargar archivos si existen
def download_file(file_url, file_name):
    response = requests.get(file_url)
    if response.status_code == 200:
        with open(file_name, "wb") as file:
            file.write(response.content)
        print(f"Descargado: {file_name}")
    else:
        print(f"No encontrado: {file_url}")

# Probar combinaciones
for file_name in generate_file_names(country, years=range(1840, 2001)):  # Cambia el rango según lo necesites
    file_url = base_url + file_name
    download_file(file_url, file_name)