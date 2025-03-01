import cv2
img=cv2.imread("img.jpg")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray1.jpg",gray)
cv2.imwrite("extension.png",img)
