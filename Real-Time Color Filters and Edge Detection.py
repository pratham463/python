import cv2
import numpy as np
def apply_filter(image,filter_type):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    if filter_type in ['r','g','b']:
        color_map={'r':(1,2), 'g':(0,2), 'b':(0,1)}[filter_type]
        image[:,:,color_map[0]]=0
        image[:,:,color_map[1]]=0
    elif filter_type == 's':
        sobel_x=cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
        sobel_y=cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)
        sobel_combined=cv2.convertScaleAbs(sobel_x+sobel_y)
        image=cv2.cvtColor(sobel_combined,cv2.COLOR_GRAY2BGR)
    elif filter_type == 'c':
        canny_edges = cv2.Canny(gray,100,200)
        image=cv2.cvtColor(canny_edges,cv2.COLOR_GRAY2BGR)
    return image
image_path='exa.jpg'
image=cv2.imread(image_path)
if image is None:
    print("error")
    exit()
print("press keys to apply filter")
print("r-Red Tint\n g-Green Tint\nb-blue tint\n r-Red Tint\ns-sobel edge detection\nc-canny edge detection\nq-quit")
filter_type='original'
while True:
    filtered = apply_filter(image.copy(),filter_type)
    cv2.imshow("Filtered Image",filtered)
    key=cv2.waitKey(0)& 0xFF
    if key in map(ord,['r','g','b','s','c']):
        filter_type =chr(key)
    elif key == ord('q'):
        print("bye")
        break
    else:
        print("invalid")
cv2.destroyAllWindows()