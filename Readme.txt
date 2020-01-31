# Developer - AyazSaiyed
# Yudiz Solutions Pvt. Ltd



----------------------------------------------------------------------

Steps 1 - 


Create the encodings of the faces 

It will generate encodings.pickle ( model file )

For that Run - python encode_faces.py

It is the process of training over the faces (images) present in the dataset  

You can use any of the method either Hog or Cnn -

Hog ( Histogram oriented graphs ) - Faster Results
CNN (Convolutional Neural Network ) - Slower but accurate results than that of the hog method


Note - Train everytime when new faces added to the dataset





Step 2 - 

Run the code to recognize the faces from the image as well as video


To Recognize faces from input image       -  python recognize_faces_image.py --encodings encodings.pickle --image dataset/Ayaz/ayaz.jpg 

To Recognize faces from live video        -  python recognize_faces_video.py --encodings encodings.pickle 

To Reocgnize faces from input video file  -  python recognize_faces_video.py --encodings encodings.pickle --output output/ayaz.avi --display 0





