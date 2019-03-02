import cv2
import numpy
from PIL import Image
import sqlite3

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
rec = cv2.face.LBPHFaceRecognizer_create()

rec.read('recognizer\\trainingData.yml')
id = 0
font = cv2.FONT_HERSHEY_SIMPLEX

def getProfile(id):
	conn = sqlite3.connect('faceBase.db')
	cmd =  ' SELECT * FROM People WHERE ID=' +str(id)
	cursor = conn.execute(cmd)
	profile = None
	for row in cursor:
		profile = row
	conn.close()
	return profile
	


while True:
	_,frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	faces = face_cascade.detectMultiScale(gray, 1.1, 5)
	
	for rect in faces:
		(x,y,w,h) = rect
		frame = cv2.rectangle(frame , (x,y), (x+w ,y+h), (0,255,0), 2)
		ida, conf = rec.predict(gray[y: y+h, x : x+w])
		profile = getProfile(ida)
		if(profile != None):
			
		
				cv2.putText(frame, profile[1], (x , y+h+30),font, 1 , (255,255,0), 2 , cv2.LINE_AA)
				
	
	
	
	cv2.imshow("frame",frame)
	key = cv2.waitKey(1)
	if key == 27:
		break
		
cap.release()
cv2.destroyAllWindows()
