import numpy as np
import cv2

# creatae a image block
black = np.zeros([600,600])
# print(black)

# f_row = black[1:2]
# print(f_row)

black[200:400, 200:400]=255
print(black)

cv2.imshow("black", black)
cv2.waitKey()