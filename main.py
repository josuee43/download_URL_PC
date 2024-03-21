import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import module

def obtener_url():
    url = input("Ingrese la URL a analizar: ")
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    return url

def guardar_hipervinculos(url, soup):
    archivo_hipervinculos = "hipervinculos.txt"
    with open(archivo_hipervinculos, "w") as file:
        for a_tag in soup.find_all("a", href=True):
            link = urljoin(url, a_tag["href"])
            file.write(link + "\n")

def main():
    url = obtener_url()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    module.descargar_imagenes(url, soup)
    module.descargar_pdfs(url, soup)
    guardar_hipervinculos(url, soup)

if __name__ == "__main__":
    main()
