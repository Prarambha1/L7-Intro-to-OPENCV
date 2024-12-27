import cv2
#to check the version of opencv
#print(cv2.__version__)

image = cv2.imread("example.jpg")

cv2.namedWindow("Activity 1",cv2.WINDOW_NORMAL)

#setting window size
cv2.resizeWindow("Activity 1",800,500)

#display image
cv2.imshow("Activity 1", image)

#wait for keypress
cv2.waitKey(0)

#closing the window
cv2.destroyAllWindows()

print(f"Image dimension: {image.shape}")