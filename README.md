# vehicle-detection-with-distance
A vehicle recognition project based on opencv-python . It is the classification of vehicle from video and it gives distance from camera . In future , i will add some more features in it.

in this project ,i'm using haarcascades classifier to classify vehicles , you can create your own but it needs much patience and time to collect data and train machine to create xml files.

here ,harrcascades having many classifiers like:
eye , tree ,body ,frontal face , vehicles etc.

so you can detect other things by changing name of classifier in script.py.

ex: haar_cascade = 'haarcascades/haarcascade_car.xml'
go through haarcascades folder to choose classifier.

video also can be changed according to your preference in script.py.

ex: video='video/clear_road.mp4'

Requirements:

python 3.8 above,

opencv-python ,numpy (install using pip install command)
