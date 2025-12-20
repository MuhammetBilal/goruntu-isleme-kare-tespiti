import cv2
from ultralytics import YOLO
import os

KLASOR_YOLU = '../images'
MODEL_PATH = '../models/best_v3.pt'
CONFIDENCE = 0.5

print("Model yükleniyor...")
model = YOLO(MODEL_PATH)

print(f"'{KLASOR_YOLU}' klasörü taranıyor...")

resim_listesi = [f for f in os.listdir(KLASOR_YOLU) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
resim_listesi.sort()

toplam_resim = len(resim_listesi)
print(f"Toplam {toplam_resim} adet resim bulundu.")

if toplam_resim == 0:
    print("HATA: Klasörde resim bulunamadı! Klasör yolunu kontrol et.")
    exit()

current_index = 0

cv2.namedWindow("Analiz Galeri", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Analiz Galeri", 1024, 768)

while True:
    dosya_adi = resim_listesi[current_index]
    tam_yol = os.path.join(KLASOR_YOLU, dosya_adi)

    frame = cv2.imread(tam_yol)

    if frame is None:
        print(f"HATA: {dosya_adi} okunamadı, sonraki resme geçiliyor.")
        current_index = (current_index + 1) % toplam_resim
        continue

    results = model(frame, conf=CONFIDENCE)
    annotated_frame = results[0].plot()

    # --- BİLGİ YAZISI EKLE ---
    info_text = f"[{current_index + 1}/{toplam_resim}] {dosya_adi}"

    cv2.rectangle(annotated_frame, (0, 0), (frame.shape[1], 40), (0, 0, 0), -1)
    cv2.putText(annotated_frame, info_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (255, 255, 255), 2)

    cv2.putText(annotated_frame, "'d': Sonraki | 'a': Onceki | 'q': Cikis",
                (10, annotated_frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 255, 255), 2)

    cv2.imshow("Analiz Galeri", annotated_frame)


    key = cv2.waitKey(0)


    if key == ord('q'):
        break

    elif key == ord('d') or key == 83:
        current_index += 1

        if current_index >= toplam_resim:
            current_index = 0

    elif key == ord('a') or key == 81:
        current_index -= 1

        if current_index < 0:
            current_index = toplam_resim - 1

cv2.destroyAllWindows()