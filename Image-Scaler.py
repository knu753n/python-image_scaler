import numpy as np
import cv2
import os

dir_path = input("Mappe med bilder som skal skaleres: ")
photo_size = float(input("Prosent av originalbilde: ")) / 100

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        
        img = cv2.imread(f'{dir_path}\{path}',1)

        img_scaled = cv2.resize(img, None, fx=photo_size, fy=photo_size, interpolation = cv2.INTER_AREA)

        if not os.path.isdir(f'{dir_path}\Skalert'):
            os.mkdir(f'{dir_path}\Skalert')

        cv2.imwrite(f'{dir_path}\Skalert\scaled_{path}', img_scaled)

        print(f"{path} : scaled complete")