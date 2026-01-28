from ultralytics import YOLO
import cv2

model = YOLO('../models/best_v5.pt')

cap = cv2.VideoCapture('../videos/iki_kare_video.mp4')

cv2.namedWindow("Ekran", cv2.WINDOW_NORMAL)

while True:
    success, frame = cap.read()

    # Video bittiğinde veya okunamadığında döngüyü kır
    if not success:
        print("Video bitti veya dosya bulunamadı.")
        break

    results = model(frame, conf=0.5)

    resim_sonucu = results[0].plot(labels=True, conf=True)

    cv2.imshow("Ekran", resim_sonucu)

    # 'q' tuşuna basınca çık
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()