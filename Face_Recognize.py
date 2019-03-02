import sqlite3
import cv2
import numpy

def InsertorUpdate(Id, Name):
	conn = sqlite3.connect("faceBase.db")
	cmd = 'SELECT * FROM People Where ID =' +str(Id)
	cursor = conn.execute(cmd)
	isRecordExist = 0
	for row in cursor:
		isRecordExist = 1
	if(isRecordExist == 1):
		cmd = "UPDATE People SET Name = " + str(Name)+ "Where ID = " +str(Id)
	else:
		cmd = "INSERT INTO People(ID, Name) Values( "+str(Id)+","+str(Name)+")"
	conn.execute(cmd)
	conn.commit()
	conn.close()
	





cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
ida = input(" Enter the id : ")
name = input("Enter your name : ")
InsertorUpdate(ida, name)

sam = 0
while True:
	_,frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)	
	faces = face_cascade.detectMultiScale(gray, 1.1, 5)
	
	
	
	for rect in faces:
		(x,y,w,h) = rect
		sam += 1
		cv2.imwrite('dataSet/user.'+str(ida) +'.' + str(sam)+ '.jpg' , gray[y:y+h, x: x+w])
		
		
		
		frame = cv2.rectangle(frame , (x,y), (x+w ,y+h), (0,255,0), 2)
		
	cv2.imshow("frame",frame)
	key = cv2.waitKey(50)
	if key == 27:
		break
		
cap.release()
cv2.destroyAllWindows()
