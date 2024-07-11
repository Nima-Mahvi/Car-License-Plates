# Car-License-Plates
Detecting car license plates and predicting their location using OpenCV and Random Forest.

This project aims to detect and predict car license plate numbers using various technologies, including OpenCV, Random Forest, and Tkinter.

## Project Overview:

1. **Data Preprocessing**: Initially, the data related to car license plates is processed and converted into CSV format.
2. **Image Processing**: Images of car license plates are processed, and important features are extracted from them.
3. **Model Training**: The Random Forest model is trained to predict license plate numbers.
4. **Alphanumeric and Digit Detection**: Using the trained model, alphanumeric characters and digits of the license plates are detected.
5. **Location Prediction**: Based on the information obtained from the license plates, their locations are predicted.

## Technologies Used:

- OpenCV for image processing.
- Random Forest for model training.
- Tkinter for user interface.

## Usage:

1. Download the necessary data file from [this link](https://www.dropbox.com/scl/fi/4wxtzmgcm7yi66zge554u/complete_digits_data.csv?rlkey=jmje04sp07kyvc2h41t9bk1d5&st=j7i8id5r&dl=1) (~200 MB).
2. Place the downloaded file next to the main program file.
3. If you want to use the image data used to create the CSV, download it from [this link](https://www.dropbox.com/scl/fi/aqp8pzb01vumg0e0q0a77/ImageData.zip?rlkey=93y4rianx5r16rebbl7mxce36&st=f1p7ma2v&dl=1).
   - The ZIP file (~115 MB) contains two folders with images of license plates and individual characters extracted from them.
   - Extract the contents and place the folders as needed.
4. Run main.py in your Python environment.
5. Select an image containing a car license plate.
6. Press the 'OK' button to start processing.
7. View the progress in the console.

Feel free to customize or expand upon this README.md file as needed. If you have any further questions or need assistance, please don't hesitate to reach out!

