import cv2
print("Package Imported")

#Upload Image
# img = cv2.imread("Ressources/computer.jpg")
# cv2.imshow("Output",img)
#cv2.waitKey(0)

img = cv2.imread("Ressources/dogs.png", cv2.IMREAD_UNCHANGED)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #image with Gray color
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) #image Blur
imgCanny = cv2.Canny(img,100,100)#image Canny

scale_percent = 1000  # percent of original size
width = int(imgGray.shape[1] * scale_percent / 5000)
height = int(imgGray.shape[0] * scale_percent / 5000)
dim = (width, height)

# resize image
grayImage = cv2.resize(imgGray, dim, interpolation=cv2.INTER_AREA)
blurImage = cv2.resize(imgBlur, dim, interpolation=cv2.INTER_AREA)
cannyImage = cv2.resize(imgCanny, dim, interpolation=cv2.INTER_AREA)

cv2.imshow("Gray Image", grayImage)
cv2.imshow("Blur Image", blurImage)
cv2.imshow("Canny Image", cannyImage)
cv2.waitKey(0)

# Uload video
# cap = cv2.VideoCapture("Ressources/videocosina.mp4")
#
# while True :
#
#     success , img = cap.read()
#     cv2.imshow("video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#Activate webcam
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)
#
# while True :
#
#     success , img = cap.read()
#     cv2.imshow("video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break



