import numpy as np
import cv2
import os

def slash():
    if os.name == "posix":
        return "/"
    if os.name == "nt":
        return "\\"

dir_path = input("Mappe med bilder som skal skaleres: ")
photo_size = float(input("Prosent av originalbilde: ")) / 100
prefix = input("Skalert bilde prefix: ")

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        
        img = cv2.imread(f'{dir_path}{slash()}{path}',1)

        img_scaled = cv2.resize(img, None, fx=photo_size, fy=photo_size, interpolation = cv2.INTER_AREA)

        if not os.path.isdir(f'{dir_path}{slash()}Skalert'):
            os.mkdir(f'{dir_path}{slash()}Skalert')

        cv2.imwrite(f'{dir_path}{slash()}Skalert{slash()}{prefix}{path}', img_scaled)

        print(f"{path} : scaled complete")