import cv2
import numpy as np

image = cv2.imread('C:\cv\latarbelakang gambar\gambar-asli.jpeg')

if image is None:
    print("Gambar tidak ditemukan!")
else:
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100, 150, 50])  
    upper_blue = np.array([140, 255, 255])  

    blue_mask = cv2.inRange(hsv_image,  lower_blue, upper_blue)

    image[blue_mask != 0] = [0, 255, 0]

    cv2.imwrite('ubah.png', image)

    cv2.imshow('Hasil Gambar', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
