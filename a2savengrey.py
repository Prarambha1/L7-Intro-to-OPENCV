import cv2

image = cv2.imread("example.jpg")
#convert the image to gray scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resize_image = cv2.resize(gray_image,(200,200))

cv2.imshow("Processed grayscale image", resize_image)

key= cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite("Processed grayscale image.jpg", resize_image)
    print("Image is saved as Processed grayscale image.jpg")

else:
    print("Image not saved")

cv2.destroyAllWindows()

print(f"Processed image dimension {resize_image.shape}")