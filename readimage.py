import cv2
import numpy

image = cv2.imread("cv.jpg")
image2 = cv2.imread("grey.jpeg",0)
# color_image = cv2.cvtColor(image2,cv2.COLOR_GRAy2BGR555)
grey_image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

#show the image on the screen

cv2.imshow("mywindow", grey_image)
cv2.imwrite("converted.png", grey_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# print(type(image))
# print(image.shape)

# print(grey_image)

