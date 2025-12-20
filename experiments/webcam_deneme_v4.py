from ultralytics import YOLO
import cv2

model = YOLO('../models/best_v4.pt')
path = '../videos/webcam.mp4'
cap = cv2.VideoCapture('../videos/kare_bant_diger_nesne.mp4')

while True:
    success, frame = cap.read()
    if not success: break

    results = model(frame, conf=0.5)
    resim_sonucu = results[0].plot(labels=True, conf=True)

    cv2.imshow("Ekran", resim_sonucu)
    if cv2.waitKey(1) == ord('q'): break