import cv2
image =cv2.imread('OIP.jpg')
cv2.namedWindow('LoadedImage',cv2.WINDOW_NORMAL)
cv2.resizeWindow('LoadedImage',500,800)
cv2.imshow('Loaded iamge',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(f"Image DImension:{image.shape}")