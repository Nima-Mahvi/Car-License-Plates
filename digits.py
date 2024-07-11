import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
###################################################
from img_processing import processor

class digit:
    
    def digits_csv():
        
        ## -------------------------------
        ## aligning names in photos 
        # def rename_files(path):
        #     os.chdir(path)
        
        #     i = 1
        #     for filename in os.listdir("."):
        #         if filename.endswith(".jpg"):
        #             os.rename(filename , str(i) + ".jpg")
        #             i+= 1
        
        # path = "digits/5"
        # rename_files(path)
        ## -------------------------------
        
        ## read digits from folders for image processing
        for i in range (0,10):
            print("number of folders :",i)
            path = f"digits/{i}"
            cnt=0
            samples = pd.DataFrame()
            targets = pd.DataFrame()
            for  filenames in os.listdir(path):
                myprocessor = processor()
                digit = myprocessor.digits( filenames , i )
                
                try:
                    plt.imshow(digit , cmap = "gray")
                    
                    sample = pd.DataFrame( digit.flatten().reshape(1,-1) )
                    samples = pd.concat([samples , sample] , ignore_index=True)
                    
                    number=[i]
                    target = pd.DataFrame (number)
                    targets = pd.concat([targets , target] , ignore_index=True)
            
                    cnt+=1
                except:
                    continue
            print(f"number of processed images in {i}: ",cnt)
            samples["targets"] = targets
            samples.to_csv(f"{i}.csv" , index=False)
            print(f" csv {i} created.")
            
        #-------------------------------
        
        ## read csv files
        zero = pd.read_csv("0.csv",encoding="UTF-8")
        one = pd.read_csv("1.csv",encoding="UTF-8")
        two = pd.read_csv("2.csv",encoding="UTF-8")
        three = pd.read_csv("3.csv",encoding="UTF-8")
        four = pd.read_csv("4.csv",encoding="UTF-8")
        five = pd.read_csv("5.csv",encoding="UTF-8")
        six = pd.read_csv("6.csv",encoding="UTF-8")
        seven = pd.read_csv("7.csv",encoding="UTF-8")
        eight = pd.read_csv("8.csv",encoding="UTF-8")
        nine = pd.read_csv("9.csv",encoding="UTF-8")
        
        lst = [zero,one,two,three,four,five,six,seven,eight,nine]
        data = pd.DataFrame()
        
        for numbers in lst:
            data = pd.concat([ data , numbers ] , ignore_index=True)
        
        # data.to_csv("complete_digits_data.csv" , index=False)
        # ( with this data,there's no need to have 10 csv file individually
        # anymore. so we can delete them.)
        # now we have data and targets in one csv file for (digits)
        #--------------------------------------------------------
        
    def digit_model_test():
        ##-------------------- read complete csv file--------------------
        data=pd.read_csv("complete_digits_data.csv",encoding="UTF-8")
        print(data.shape)
        print(data["targets"].unique())
        
        ##--------------------- train test split ------------------------
        
        from sklearn.model_selection import train_test_split
        
        x = data.drop("targets",axis=1)
        y = data["targets"]
        
        x_train, x_test, y_train, y_test = train_test_split(x,y,
                                                            test_size= 0.3,
                                                            random_state = 100 )
        
        ##------------------------- my KNN model ------------------------
        # from sklearn.neighbors import KNeighborsClassifier
        
        # #------Find Best K -------
        # scores=[]
        # for i in range (1,31):  #Took the range of k from 1 to 30
        #     knn=KNeighborsClassifier(n_neighbors=i)
        #     knn.fit(x_train,y_train)
        #     predict_i=knn.predict(x_test)
        #     scores.append(knn.score(x_test,y_test))
        
        # print(scores)
        # print("best score is: ",max(scores))
        # print("best k is : ",scores.index(max(scores))+1)
        # ## best k are : 1  and 3
        # #-------------------------
        # knn = KNeighborsClassifier(n_neighbors=3)
        # knn.fit(x_train, y_train)
        # y_pred = knn.predict(x_test)
        
        # print("test shape: ",x_test.shape)
        # print("knn score: ",knn.score(x_test,y_test)) 
        # # KNN accuracy is : 95%
        
        # #------------------------- my Dtree model ------------------------
        # from sklearn.tree import DecisionTreeClassifier
        # from sklearn.metrics import accuracy_score
        
        # clf_entropy = DecisionTreeClassifier(criterion = "entropy" ,
        #                                       random_state = 100)
        
        # clf_entropy.fit(x_train , y_train)
        
        # ypred = clf_entropy.predict(x_test)
        # print("Accuracy: ",accuracy_score(y_test , ypred)*100)
        
        # # Dtree accuracy is : 87%
        
        
        ##------------------------- my RandomForest model ------------------------
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import accuracy_score 
        
        rf_classifier = RandomForestClassifier(n_estimators=100 , random_state = 42)
        
        rf_classifier.fit(x_train , y_train)
        
        y_pred = rf_classifier.predict(x_test)
        accuracy = accuracy_score(y_test , y_pred)
        print(accuracy) ## RF accuracy is : 96%
        
        # random forest was chosen among our models with 96% accuracy.
        
        ## now we use our all data and targets for better training in RF
        ##-----------------------------------------------------------------------------
        
        

    def pred_digit(digit):
       
       data=pd.read_csv("complete_digits_data.csv",encoding="UTF-8")
       
       x_train = data.drop("targets",axis=1)
       y_train = data["targets"]
       
       rf_classifier = RandomForestClassifier(n_estimators=100 , random_state = 42)
       
       rf_classifier.fit(x_train , y_train)
       
       y_pred = rf_classifier.predict(digit)
       
       return y_pred
       






































    














































        
      
        
