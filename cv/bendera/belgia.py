import numpy as np
import cv2
import pandas as pd

height = 600
width = 900

flag = np.zeros((height, width, 3), dtype=np.uint8)

stripe_width = width // 3

flag[:, :stripe_width] = [0, 0, 0]  

flag[:, stripe_width:2*stripe_width] = [0, 255, 255]  

flag[:, 2*stripe_width:] = [0, 0, 255] 

df_flag = pd.DataFrame(flag.reshape(-1, 3), columns=['B', 'G', 'R'])
print(df_flag.head()) 

cv2.imwrite('belgia.png', flag)

cv2.imshow("Bendera Belgia", flag)
cv2.waitKey(0)
cv2.destroyAllWindows()
