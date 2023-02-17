# To Capture Frame
import cv2

# To process image array
import numpy as np


# import the tensorflow modules and load the model
import tensorflow as tf
import keras

model = tf.keras.models.load_model('Tensorflow.js')

# Attaching Cam indexed as 0, with the application software
camera = cv2.VideoCapture(0)

# Infinite loop
while True:

	# Reading / Requesting a Frame from the Camera 
	status , frame = camera.read()

	# if we were sucessfully able to read the frame
	if status:

		# Flip the frame
		frame = cv2.flip(frame , 1)
		#resize the frame
		img = cv2.resize(frame(224 , 224))
		
		normalised_image = test_image/255.0
		
		predictions = model.predict(normalised_image)
		
	
		cv2.imshow('feed' , frame)

		code = cv2.waitKey(1)
		
		if code == 32:
			break

camera.release()

cv2.destroyAllWindows()