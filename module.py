from urllib.parse import urljoin
import os, requests

def descargar_imagenes(url, soup):
    directorio_imagenes = "imagenes"
    os.makedirs(directorio_imagenes, exist_ok=True)
    for img_tag in soup.find_all("img"):
        img_url = urljoin(url, img_tag["src"])
        img_nombre = os.path.basename(img_url)
        img_path = os.path.join(directorio_imagenes, img_nombre)
        with open(img_path, "wb") as img_file:
            img_file.write(requests.get(img_url).content)

def descargar_pdfs(url, soup):
    directorio_pdfs = "pdfs"
    os.makedirs(directorio_pdfs, exist_ok=True)
    for a_tag in soup.find_all("a", href=True):
        link = urljoin(url, a_tag["href"])
        if link.endswith(".pdf"):
            pdf_nombre = os.path.basename(link)
            pdf_path = os.path.join(directorio_pdfs, pdf_nombre)
            with open(pdf_path, "wb") as pdf_file:
                pdf_file.write(requests.get(link).content)
