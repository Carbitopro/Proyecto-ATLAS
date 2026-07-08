import shutil
from pathlib import Path
carpeta = Path("sandbox")

print(f"Contenido de {carpeta.name}:")


imagenes = carpeta / 'Imagenes'
imagenes.mkdir(exist_ok=True)

for elemento in carpeta.iterdir():
    if elemento.is_file():

        if elemento.suffix == '.jpg':
            shutil.move(elemento, imagenes)
        else:
            print('not a .jpg')
