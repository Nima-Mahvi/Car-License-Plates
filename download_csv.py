import requests
import os
import pandas as pd

class download:
    def download_file(url, destination):
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(destination, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f'File downloaded: {destination}')
        else:
            print(f'Failed to download file. Status code: {response.status_code}')
    
    try:
        There = pd.read_csv("complete_digits_data.csv")
    except:
        if __name__ == "__main__":
            print("File (complete_digits_data.csv) could not be found. \n We need this file. Please wait until this file is completely downloaded and then run the program again.")
            url = 'https://www.dropbox.com/scl/fi/4wxtzmgcm7yi66zge554u/complete_digits_data.csv?rlkey=jmje04sp07kyvc2h41t9bk1d5&st=j7i8id5r&dl=1'
            print("If this action is not done, you will be able to download it through the following link. Please put it next to the main program file after downloading: \n" , url)
            print("******************* \n It is a csv file of about 207 MB. It contains 38206 rows and 2401 columns. Please check that the file has been downloaded correctly.")
            print("******************* \n Downloading...")
            
            file_name = url.split('/')[-1].split('?')[0]
            root_path = os.path.dirname(os.path.abspath(__file__))
            destination = os.path.join(root_path, file_name)
            
            download_file(url, destination)
    
    
    
    
    
    
    
    
    










