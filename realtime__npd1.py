import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

print("**************Realtime Car Number Plate Detection System******************\n")

print("----------------------------------------------------------------------------\n\n")
print("-------------------------INSTRUCTIONS---------------------------------------\n")
print("--------Now click on the open camera window and start detection--------------")
print("---------------------Press 'S' to save the Image----------------------------")
print("-----Wait 10 secs to continue after save or press 'X' to view results--------")
print("-----After seeing results you have 10 secs to press 'E' to exit--------------")
print("-----------------------Else the program continues---------------------------")
print("--------Now click on the open camera window and start detection--------------")
print("----------------------------------------------------------------------------")
print("----------------------------------------------------------------------------\n\n")

##################################################################################
frameWidth = 640
frameHeight = 480
nPlateCascade= cv2.CascadeClassifier(cv2.haarcascades+"haarcascade_russian_plate_number.xml")
minArea = 500
color = (255,0,255)
states= ['AN', 'AP', 'AR', 'AS', 'BR', 'CH', 'DN', 'DD', 'DL', 'GA', 'GJ', 'HR', 'JK', 'KA', 'KL', 'LD',
         'MP', 'MH', 'MN', 'ML', 'MZ', 'NL', 'OD', 'PY', 'PN', 'RJ', 'SK', 'TN', 'TR', 'UP', 'WB', 'CG',
         'TS', 'JH', 'UK']
#################################################################################
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
count = 0
noplate = []
correct = []
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray,1.1,4)
 
    for (x,y,w,h) in numberPlates:
        area = w*h
        if area>minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)

            
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("ROI",imgRoi) 
            read = pytesseract.image_to_string(imgRoi)
            read = ''.join(e for e in read if e.isalnum())
            noplate.append(read)
            cv2.rectangle(img, (x, y), (x + w, y + h), (51, 51, 255), 2)
            # cv2.rectangle(img, (x, y - 40), (x + w, y), (51, 51, 255), -1)
            # cv2.putText(img, read, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Result", img)
    
    if cv2.waitKey(1) & 0xFF == ord('s'):  # Press 'S' to save image
        print(">>> Image Saved, You have 10 seconds to press X and view results else wait.\n")
        cv2.imwrite("scan_images/no_plate" + str(count) + ".jpg", imgRoi)  # Saving image to respective folder
        cv2.rectangle(img , (0,200), (640,300) , (0,255,0) , cv2.FILLED )
        cv2.putText(img, "scan saved" , (150,255) , cv2.FONT_HERSHEY_DUPLEX , 2,(0,0,255),2)
        cv2.imshow("Result", img)
        if cv2.waitKey(10000) & 0xFF == ord('x'): # else press any key to continue else wait 10 s
            noplate = list(filter(lambda a: a != "", noplate))
            for i in noplate:
                if len(i) == 10:
                    if i[0:2] in states:
                        correct.append(i)
            correct = set(correct)
            print('Number Plate:', correct)
            if(correct == []):
                print("NumberPlate Not Found \n")
            textfile = open('scan.txt', 'a+')  # File opening to write
            for texts in correct:
                textfile.write(texts + '\n')

            print(">>> You have 10 seconds to press E and exit else wait.\n")
            if cv2.waitKey(10000) & 0xFF == ord('e'): # Pressing 'E' to exit
                break
        else:
            count += 1
textfile.close()  #File Closing




