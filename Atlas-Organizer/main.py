import shutil
from pathlib import Path
carpeta = Path("sandbox")

print(f"Contenido de {carpeta.name}:")


tipos = {
    '.jpg': 'Imagenes',
    '.pdf': 'Documentos',
    ".txt": "Documentos",
    ".png": "Imagenes",
}


for elemento in carpeta.iterdir():
    if elemento.is_file():

        carpeta_destino = tipos.get(elemento.suffix, "Otros")
        destino = carpeta/carpeta_destino

        destino.mkdir(exist_ok=True)
        shutil.move(elemento, destino)
