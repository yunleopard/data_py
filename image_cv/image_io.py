'''
Created on Nov 12, 2018

@author: yangzh
'''
import cv2


image = cv2.imread("../data/Show.png",1)

cv2.imshow("image",image)

k = cv2.waitKey(0) # it waits for any key to be pressed to execute next step

if k == 27: # wait for ESC key to exit
  
    cv2.destroyAllWindows()
    
elif k == ord('s'): # wait for ‘s’ key to save and exit
  
    cv2.imwrite("../data/Show_bak.png",image)
    
    cv2.destroyAllWindows()