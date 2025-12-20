from ultralytics import YOLO
import cv2

MODEL_PATH = '../models/best.pt'
VIDEO_DOSYA_ADI = '../videos/kare_hedef_deneme.mp4'

print("Başlatılıyor...")

model = YOLO(MODEL_PATH)
cap = cv2.VideoCapture(VIDEO_DOSYA_ADI)

while True:
    success, frame = cap.read()
    if not success:
        print("Video bitti.")
        break

    results = model(frame, conf=0.5)
    resim_sonucu = results[0].plot()

    gosterim = cv2.resize(resim_sonucu, (1020, 720))
    cv2.imshow("Video Analizi - Sade", gosterim)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("İşlem tamamlandı.")