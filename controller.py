import numpy as np
import pandas as pd
from PIL import ImageGrab , Image , ImageDraw , ImageTk
import os
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter("ignore")

########################################################
from img_processing import processor
from preprocessing import pre  
from alphabets import alphabet
from digits import digit 
from locations import location

# # hello! we had several stages of data preprocessing, including converting
# # the (.txt) file to (.csv) and making features of the information 
# # that are in (preprocessing.py)

     
# data_preprocessing = pre.preprocess()    ##I created one so I disabled it 

# ##--------------------------------------------------------------------------

# # we have images of the license plates of the cars. according to the name of
# # these images that is available in the dataset and alphabet feature, we can
# # read and process the image and crop the relevant part.
# # finally give it a target and save them to a csv file.

                   
# making_alphabet_csv = alphabet.alphabets_csv() ##I created one so I disabled it

# alphabet_model_test = alphabet.alphabet_model_test()
 
# # I tested them and RF was fairly accurate
# # after this we can use RF model with our complete data for better alphabet training

# ##--------------------------------------------------------------------------

# now it's time for digits.  in NR folder we have
# digits images in 10 folders (0,1,2,3,4,5,6,7,8,9)
# we have to read them from within the folders and turn them into samples
# and finally give them targets and save them to a csv file.

                  
# making_digits_csv = digit.digits_csv() ##I created one so I disabled it

# digit_model_test = digit.digit_model_test() 

# I tested them and RF was fairly accurate
# after this we can use RF model with our complete data for better digits training

##--------------------------------------------------------------------------

## and now it's time to process the user plate

class conotrol_proj:
    def control(self , file_path):
        
        # image path
        image_path = file_path
        
        if os.path.exists(image_path):
            print("photo found... \n Please wait a minute! ")
            
            ## ----------- alphabet process ------------
            found = False
            
            MyProcessor = processor()
            
            result , found = MyProcessor.cropped_contour(image_path , found)
            
            if found:
                # plt.imshow(result , cmap = "gray")
                try:
                    alpha_ = pd.DataFrame( result.flatten().reshape(1,-1) )
                    
                    predicted_alpha = alphabet.pred_alpha(alpha_)
                    print("predicted alphabet is: ",predicted_alpha)
                    
                except:
                    alpha_error = "Unable to read the alphabet from the photo. :( \n Please put a better one."
                    print("*****************")
                    print(alpha_error)
                    print("*****************")
        
            ## ----------- digits process ------------
            two_digits = MyProcessor.user_digits(image_path)
            
            try:
                digit1 = two_digits[:80]
                # plt.imshow(digit1 , cmap = "gray")
                digit1 = np.array(digit1)
                digit1 = pd.DataFrame( digit1.flatten().reshape(1,-1) )
                
                predicted_digit1 = digit.pred_digit(digit1)
                
                print("the prediction of 1st number is: ", predicted_digit1)
             
            except:
                print("Unable to read 1st number")
            try:    
                digit2 = two_digits[80:]
                # plt.imshow(digit2 , cmap = "gray")
                digit2 = np.array(digit2)
                digit2 = pd.DataFrame( digit2.flatten().reshape(1,-1) )
                
                predicted_digit2 = digit.pred_digit(digit2)
                
                print("the prediction of 2nd number is: ",predicted_digit2)
                
            except:
                print("Unable to read 2nd number")
                      
            try:
                first_digit = int(predicted_digit1[0]) * 10
                # print(first_digit)
                # print(type(first_digit))
            except:
                print("*****************")
                print("Unable to read first digit from the photo. :( \n Please put a better one.")
                print("*****************")
            
            try:
                second_digit = int(predicted_digit2[0])
                # print(second_digit)
                # print(type(second_digit))
            except:
                print("*****************")
                print("Unable to read second digit from the photo. :( \n Please put a better one.")
                print("*****************")
            
            try:
                city_num = first_digit + second_digit
                
                mystate = location.states(city_num)
                print("Province : " , mystate)
                
            except:
                mystate=False
                print("Unable to get the city number. :(")
            
            try:
                alpha = predicted_alpha[0]
                # print(alpha)
                # print(type(alpha))
                myexact = location.exact_city(city_num , alpha)
                print("exact location : " , myexact)
                    
            except:
                myexact=False
                print("*****************")
                print("can't read :( \n Please put a better one.")
                print("*****************")
            
            if mystate:
                if myexact:
                    try:
                        return mystate , myexact
                    except:
                        return "-" , "-"
                    
                elif not myexact:
                    try:
                        return mystate , "-"
                    
                    except:
                        return "-" ,"-"
            if not mystate:
                if myexact:
                    try:
                        return "-" , myexact
                    except:
                        return "-" , "-"
                if not myexact:
                    return "-" , "-"
            
                    
                    
        else :
            print("photo not found! :(")
            return False,False





