from pathlib import Path
carpeta = Path('practice')

tipos = {
    '.jpg': 'Imagenes',
    '.txt': 'Documentos',
    '.mp3': 'Musica',
    '.png': 'Imagenes',
    '.pdf': 'Documentos'
}
contador = {
    "Imagenes": 0,
    "Documentos": 0,
    "Musica": 0,
    "Otros": 0,
}

for elemento in carpeta.iterdir():
    if elemento.is_file():
        for elemento in contador:
            cuenta = tipos.get(elemento, 0) + 1
for tipo in tipos:

    print(tipos[tipo], '->', cuenta)
