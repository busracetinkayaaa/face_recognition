import cv2


cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    cv2.imshow("Face-Recognition",img)
    cv2.waitKey(1)





































# face_encodings = []
# face_names=[]
#
# person1_image= face_recognition.load_image_file("zendaya.jpg")
# person2_image= face_recognition.load_image_file("timothee.jpg")
#
# person1_encoding=face_recognition.face_encodings(person1_image)
# person2_encoding=face_recognition.face_encodings(person2_image)
#
# face_encodings.append(person1_encoding)
# face_encodings.append(person2_encoding)
#
# face_names.append("Zendaya")
# face_names.append("Timothee")
#
# video_capture=cv2.VideoCapture(0)
#
# while True:
#     ret,frame=video_capture.read()
#
#     face_locations= face_recognition.face_locations(frame)
#     face_encodings=face_recognition.face_encodings(frame,face_locations)
#
#     for(top,right,bottom,left),face_encoding in zip(face_locations,face_encodings):
#         matches=face_recognition.compare_faces(face_encodings,face_encoding)
#         name= "unknown"
#
#         if True in matches:
#             first_match_index=matches.index(True)
#             name=face_names[first_match_index]
#
#
#         cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
#         cv2.putText(frame,name,(left,top-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,0,255),2)
#
#
#     cv2.imshow("Video",frame)
#
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break
#
#
# video_capture.release()
# cv2.destroyAllWindows()