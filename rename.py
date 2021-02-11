import os
archivos = []
for subdir, dirs, files in os.walk('./'):
    for file in files:
        if file[-4:] == ".mp3":
            nombre = [int(s) for s in file.split() if s.isdigit()] 
            if len(nombre) > 0:
                num = nombre[0]
                new_name= f"{num}.mp3" 
                os.rename(file, new_name)

