import cv2
import numpy as np

image = cv2.imread("poster.jpg")
print(image)

rocket = image[120:360, 400:500]
print(rocket)

text = "My own image card!"

image[0:240, 500:600]=rocket
cv2.putText(image,text,(40,40),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.2, color=(233,76,50))

cv2.imshow("mywindow", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
