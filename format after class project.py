import cv2, time, numpy as np, mediapipe as mp
hands = mp.solutions.hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
draw = mp.solutions.drawing_utils
filters = [None, 'GRAY', 'SEPIA', 'NEG', 'BLUR']
f = 0
last = 0
delay = 1
def apply(img, t):
    if t == 'GRAY': 
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if t == 'SEPIA':
        s = np.array([[.272, .534, .131], [.393, .686, .168], [.769, .769, .189]])
        return np.clip(cv2.transform(img, s), 0, 255).astype(np.uint8)
    if t == 'NEG': 
        return cv2.bitwise_not(img)
    if t == 'BLUR': 
        return cv2.GaussianBlur(img, (15, 15), 0)
    return img
cap = cv2.VideoCapture(0)
if not cap.isOpened(): 
    exit("❌ Webcam not found")
while True:
    ok, img = cap.read()
    if not ok: 
        break
    img = cv2.flip(img, 1)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    res = hands.process(rgb)
    if res.multi_hand_landmarks:
        for h in res.multi_hand_landmarks:
            draw.draw_landmarks(img, h, mp.solutions.hands.HAND_CONNECTIONS)
            pts = [h.landmark[i] for i in [4, 8, 12, 16, 20]]
            H, W, _ = img.shape
            pts = [(int(p.x * W), int(p.y * H)) for p in pts]
            for p in pts:
                cv2.circle(img, p, 8, (255, 0, 255), cv2.FILLED)
        t, i, m, r, p = pts
        now = time.time()
        if abs(t[0] - i[0]) < 30 and abs(t[1] - i[1]) < 30 and now - last > delay:
            cv2.imwrite(f"pic_{int(now)}.jpg", img)
            last = now
            print("📸 Picture saved!")
        elif any(abs(t[0] - x[0]) < 30 and abs(t[1] - x[1]) < 30 for x in [m, r, p]) \
             and now - last > delay:
            f = (f + 1) % len(filters)
            last = now
            print(f"🎛️ Filter: {filters[f]}")
    img2 = apply(img, filters[f])

    cv2.imshow("🖼 Gesture Photo App", 
               cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR) if filters[f] == "GRAY" else img2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()