import cv2
print("Package Imported")

#Upload Image
# img = cv2.imread("Ressources/computer.jpg")
# cv2.imshow("Output",img)
#cv2.waitKey(0)

# Uload video
# cap = cv2.VideoCapture("Ressources/videocosina.mp4")
#
# while True :
#
#     success , img = cap.read()
#     cv2.imshow("video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True :

    success , img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



