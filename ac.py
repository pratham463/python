import cv2
image=cv2.imread("ex.jpg")
cv2.imshow("Original Image",image)
rotated=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Rotated Image",image)
cropped=image[50:200,100:300]
cv2.imshow("Cropped Image",cropped)
brightness=cv2.convertScaleAbs(image,alpha=1,beta=50)
cv2.imshow("Brighter Image",brightness)
cv2.waitKey(0)
cv2.destroyAllWindows