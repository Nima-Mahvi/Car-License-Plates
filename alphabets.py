import numpy as np
import pandas as pd
import cv2
from PIL import ImageGrab , Image , ImageDraw , ImageTk
import os
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score 
from sklearn.ensemble import RandomForestClassifier

#########################################################
from img_processing import processor


class alphabet:
    def alphabets_csv():
        ##------------------------ read csv ------------------------
        data=pd.read_csv("complete_plates_data.csv",encoding="UTF-8")
        
        ##------------------------ images names --------------------
        data.rename(columns={'Unnamed: 0':"img_name"} , inplace=True)
        
        ##------------------------ drop unnecessaries --------------
        data.drop(columns=["3num" , "2num"] , inplace = True)
        
        ##------------- the names of images ------------------------
        img_name = data["img_name"]
        
        cnt=0
        
        samples = pd.DataFrame()
        targets = pd.DataFrame()
        
        for name in img_name:
            found = False
            ## image path
            folder_name = "NR"
            file_name = name
            file_path = os.path.join(folder_name , file_name) 
            
            if not os.path.exists(file_path):
                continue
            
            ## image processor class
            MyProcessor = processor()
            result , found =MyProcessor.cropped_contour(file_path , found)
            if found:
                plt.imshow(result , cmap = "gray")
                
                ## index 
                indx = img_name[ img_name == name ].index
                try:
                    sample = pd.DataFrame( result.flatten().reshape(1,-1) , index = indx )
                    samples = pd.concat([samples , sample] , ignore_index=False)
                
                    target = pd.DataFrame ( data.iloc[indx,2:3] )
                    targets = pd.concat([targets , target] , ignore_index=False)
                    cnt+=1
                except:
                    continue
        
        print("count: ",cnt)           
        print(targets["alphabet"].unique())
        
        samples["targets"] = targets
        samples.to_csv("complete_alphabets_data.csv" , index=False)
        ## now we have data and targets in one csv file for (alphabets)
##-----------------------------------------------------------------------------
    def alphabet_model_test():
        data=pd.read_csv("complete_alphabets_data.csv",encoding="UTF-8")
        print(data.shape)
        
        print(data["targets"].unique())
        '''
        ['ص' 'ن' 'د' 'ل' 'ق' 'ب' 'س' 'ط' 'و' 'م' 'ه' 'ع' 'ج' 'ت' 'ی' 'ویلچر'
         'ولیچر' 'ش' 'هـ' 'الف' 'ق67' 'ح' 'ي' '24' 'ذ' 'ويلچر' 'گ' 'چ' 'و87' 'ز'
         '73']
        ''' 
        ## drop numbers from tragets
        mask = data["targets"].str.isnumeric()
        data.drop(data[mask].index, inplace = True)
        data.drop(data[data.targets == 'ق67'].index , inplace = True)
        data.drop(data[data.targets == 'و87'].index , inplace = True)
        print(data.shape)
        print(data["targets"].unique())
        
        # #----------------------- train test split ----------------------
        from sklearn.model_selection import train_test_split
        
        x = data.drop("targets",axis=1)
        y = data["targets"]
        
        x_train, x_test, y_train, y_test = train_test_split(x,y,
                                                            test_size= 0.3,
                                                            random_state = 42 )
        
        # #------------------------- my KNN model ------------------------
        
        # from sklearn.neighbors import KNeighborsClassifier
        
        # # #------Find Best K -------
        # # scores=[]
        # # for i in range (1,31):  #Took the range of k from 1 to 30
        # #     knn=KNeighborsClassifier(n_neighbors=i)
        # #     knn.fit(x_train,y_train)
        # #     predict_i=knn.predict(x_test)
        # #     scores.append(knn.score(x_test,y_test))
        
        # # print(scores)
        # # print("best score is: ",max(scores))
        # # print("best k is : ",scores.index(max(scores))+1)
        # # ## best k is : 3
        # # #-------------------------
        
        # knn = KNeighborsClassifier(n_neighbors=3)
        # knn.fit(x_train, y_train)
        # y_pred = knn.predict(x_test)
        
        # print("test shape: ",x_test.shape)
        # print("knn score: ",knn.score(x_test,y_test))
        # # KNN accuracy is : 78%
        
        ##------------------------- my Dtree model ------------------------
        # from sklearn.tree import DecisionTreeClassifier
        # from sklearn.metrics import accuracy_score
        
        # clf_entropy = DecisionTreeClassifier(criterion = "entropy" ,
        #                                       random_state = 100)
        
        # clf_entropy.fit(x_train , y_train)
        
        # ypred = clf_entropy.predict(x_test)
        # print("Accuracy: ",accuracy_score(y_test , ypred)*100)
        
        # # Dtree accuracy is : 70%
        
        ##------------------------- my RandomForest model ------------------------
        
        rf_classifier = RandomForestClassifier(n_estimators=100 , random_state = 42)
        
        rf_classifier.fit(x_train , y_train)
        
        y_pred = rf_classifier.predict(x_test)
        accuracy = accuracy_score(y_test , y_pred)
        print(accuracy) ## RF accuracy is : 85%
        
        ## random forest was chosen among our models with 85% accuracy.
        ##-----------------------------------------------------------------------------
##-----------------------------------------------------------------------------
    def pred_alpha(alpha_):
        
        data=pd.read_csv("complete_alphabets_data.csv",encoding="UTF-8")
        
        x_train = data.drop("targets",axis=1)
        y_train = data["targets"]
        
        rf_classifier = RandomForestClassifier(n_estimators=100 , random_state = 42)
        
        rf_classifier.fit(x_train , y_train)
        
        y_pred = rf_classifier.predict(alpha_)
        
        return y_pred
        
        





