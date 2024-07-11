import numpy as np
import pandas as pd
import cv2
from PIL import ImageGrab , Image , ImageDraw , ImageTk
import os
import matplotlib.pyplot as plt


class processor:
    def cropped_contour(self , file_path , found):

        ##--------------- read image --------------
        image = cv2.imread(file_path)
        # plt.imshow(image , cmap = "gray")
        
        ##--------------- resize image -------------
        resized = cv2.resize(image, (350,150)) 
        # plt.imshow(resized , cmap = "gray")
    
        ##--------------- gray ----------------------
        gray = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
        # plt.imshow(gray , cmap = "gray")
        
        ##--------------- blur -----------------------
        blur = cv2.GaussianBlur(gray, (5,5), 3)
        # plt.imshow(blur , cmap = "gray")
        
        ##--------------- threshold range ------------
        trsh = [-27,-10,0,-30,-40,-50,-60,-70,-80,-90,-100,
                -5,5,10,15,20,30,40,50,60,70,80,90,100]
        
        for i in trsh:
            i = int(i)
            ##----------- brightness threshold ---------
            mean_brightness = (cv2.mean(blur)[0])+(i)
            # print(mean_brightness)
            
            ##----------- binary image -----------------
            _ , binary = cv2.threshold(blur ,mean_brightness, 255,
                                        cv2.THRESH_BINARY)
            # plt.imshow(binary, cmap = "gray")
            
            ##----------- draw a line around subjects ----
            canny = cv2.Canny(binary,30, 150, 3)
            # plt.imshow(canny , cmap = "gray")
            
            ##----------- intensifying lines --------------
            dilated = cv2.dilate(canny, (1,1), iterations=3)
            # plt.imshow(dilated , cmap = "gray")
            
            ##--- drawing square contours around the subject
            contours , _ = cv2.findContours(dilated,
                                            cv2.RETR_EXTERNAL,
                                            cv2.CHAIN_APPROX_SIMPLE)
            
            for j , contour in enumerate(contours):
                x , y , w , h = cv2.boundingRect(contour)
                
                ##--- adjust width and height to remove too small or large squares
                max_width ,min_width ,max_hight ,min_hight = 70 ,15,150 ,12
                ## use width and height to remove too small or large squares
                if min_width < w < max_width and min_hight < h < max_hight:
                    cv2.rectangle(resized , (x-5 ,y-20), (x+w+5,y+h+25),(0,255,0),1)
                    
                    ##--- adjust possible location-------------------
                    x_min, y_min, x_max, y_max =99 , 10, 155, 145
                    ## use min_max in x and y to remove other squares
                    if x_min < x < x_max and y_min < y < y_max:
                        cropped_contour = dilated[y-19:y+h+24 , x-4:x+w+5]
                        
                        ##------ equalize the size of subject to (60 , 100)
                        try:
                            resized_cropped = cv2.resize(cropped_contour, (60,100))
                            found = True
                        except:
                            break
                if found:
                    break
            if found:
                ## showing base on cropped image
                # plt.imshow(cropped_contour , cmap = "gray")
                return resized_cropped , found
                break
            if not found:
                result = np.nan
                return result , found
        
    def digits(self , filenames , i):
        try:
            ##--------------- read digits --------------
            image = cv2.imread(f"digits/{i}/{filenames}")
            # plt.imshow(image , cmap = "gray")
            
            ##--------------- resize image -------------
            resized = cv2.resize(image, (30,80)) 
            # plt.imshow(resized , cmap = "gray")
            
            ##--------------- gray ----------------------
            gray = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
            # plt.imshow(gray , cmap = "gray")
            
            ##--------------- blur -----------------------
            blur = cv2.GaussianBlur(gray, (5,5), 3)
            # plt.imshow(blur , cmap = "gray")
            
            ##----------- brightness threshold ---------
            mean_brightness = (cv2.mean(blur)[0])-10
            # print(mean_brightness)
            
            ##----------- binary image -----------------
            _ , binary = cv2.threshold(blur ,mean_brightness, 255,
                                        cv2.THRESH_BINARY)
            # plt.imshow(binary, cmap = "gray")
            
            ##----------- draw a line around subjects ----
            canny = cv2.Canny(binary,30, 150, 3)
            # plt.imshow(canny , cmap = "gray")
            
            ##----------- intensifying lines --------------
            dilated = cv2.dilate(canny, (1,1), iterations=2)
            # plt.imshow(dilated , cmap = "gray")
            
            return dilated
        
        except:
            print("error")
        
    def user_digits(self , file_path ):
        
        ##--------------- read image --------------
        image = cv2.imread(file_path)
        # plt.imshow(image , cmap = "gray")

        ##--------------- resize image -------------
        resized = cv2.resize(image, (350,150)) 
        # plt.imshow(resized , cmap = "gray")

        ##--------------- gray ----------------------
        gray = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
        # plt.imshow(gray , cmap = "gray")

        ##--------------- blur -----------------------
        blur = cv2.GaussianBlur(gray, (5,5), 3)
        # plt.imshow(blur , cmap = "gray")

        ##--------------- threshold range ------------
        trsh = [-27,-10,0,-30,-40,-50,-60,-70,-80,-90,-100,
                -5,5,10,15,20,30,40,50,60,70,80,90,100]

        for i in trsh:
            i = int(i)
            ##----------- brightness threshold ---------
            mean_brightness = (cv2.mean(blur)[0])+(i)
            # print(mean_brightness)
            
            ##----------- binary image -----------------
            _ , binary = cv2.threshold(blur ,mean_brightness, 255,
                                        cv2.THRESH_BINARY)
            # plt.imshow(binary, cmap = "gray")
            
            ##----------- draw a line around subjects ----
            canny = cv2.Canny(binary,30, 150, 3)
            # plt.imshow(canny , cmap = "gray")
            
            ##----------- intensifying lines --------------
            dilated = cv2.dilate(canny, (1,1), iterations=3)
            # plt.imshow(dilated , cmap = "gray")
            
            ##--- drawing square contours around the subject
            contours , _ = cv2.findContours(dilated,
                                            cv2.RETR_EXTERNAL,
                                            cv2.CHAIN_APPROX_SIMPLE)
            # print(type(contours))

            cnt=0
            found = False
            sorting_dct = {}
            
            for j , contour in enumerate(contours):

                x , y , w , h = cv2.boundingRect(contour)
                
                ##--- adjust width and height to remove too small or large squares
                max_width ,min_width ,max_hight ,min_hight = 60 ,10 ,120 ,10
                ## use width and height to remove too small or large squares
                if min_width < w < max_width and min_hight < h < max_hight:
                    cv2.rectangle(resized , (x-5 ,y-20), (x+w+5,y+h+25),(0,255,0),1)
                    
                    ##--- adjust possible location-------------------
                    x_min, y_min, x_max, y_max = 260, 10, 350, 140
                    ## use min_max in x and y to remove other squares
                    if x_min < x < x_max and y_min < y < y_max:
                        
                        cropped_contour = dilated[y:y+h , x:x+w]
                        ##------ equalize the size of subject to (30 , 80)
                        try:
                            digit = cv2.resize(cropped_contour, (30,80))
                            ## showing base on cropped and resized image
                            # plt.imshow(digit , cmap = "gray")
                            
                            digit = pd.DataFrame(digit)
                            ## we need x axis for sorting contours of digits
                            ## so we creat a dct with x key and digit values
                            ## and sorting base on keys
                            sorting_dct[x] = digit
                            
                            cnt+=1
                            found = True
                        except:
                            break
                if found:
                    if cnt==2:
                        break
                    continue
                    
            if found:
                break
            
        ## we have x location and it's usable DataFrame contour in one dct
        # print(sorting_dct)
        
        sorting = sorted(sorting_dct)
        
        two_digits = pd.DataFrame()
        for s in sorting :
            digit = sorting_dct[s]
            two_digits = pd.concat([two_digits , digit ])
        return two_digits
        
        
        
        
        
        
        
        
        
