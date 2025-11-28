import cv2, time, pyautogui, mediapipe as mp

hands = mp.solutions.hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
draw = mp.solutions.drawing_utils
W, H, SCROLL, DELAY = 640, 480, 300, 1

def detect(landmarks, hand):
    fingers = [1 for t in [8, 12, 16, 20] if landmarks.landmark[t].y < landmarks.landmark[t-2].y]

    tip, pip = landmarks.landmark[4], landmarks.landmark[3]
    if (hand == "Right" and tip.x < pip.x) or (hand == "Left" and tip.x > pip.x):
        fingers.append(1)

    return "scroll_up" if sum(fingers) == 5 else "scroll_down" if len(fingers) >= 0 else "none"

cap = cv2.VideoCapture(0)
cap.set(3, W); cap.set(4, H)

print("Gesture Scroll Active\nOpen palm → Scroll Up | Fist → Scroll Down | Press 'q' to quit")
last = time.time()

while cap.isOpened():
    ok, img = cap.read()
    if not ok: break

    img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 1)  
    res = hands.process(img)

    gesture, hand = "none", "Unknown"

    if res.multi_hand_landmarks:
        for h, info in zip(res.multi_hand_landmarks, res.multi_handedness):
            hand = info.classification[0].label
            gesture = detect(h, hand)
            draw.draw_landmarks(img, h, mp.solutions.hands.HAND_CONNECTIONS)

    if time.time() - last > DELAY:
        pyautogui.scroll(SCROLL if gesture == "scroll_up" else -SCROLL if gesture == "scroll_down" else 0)
        last = time.time()

    cv2.putText(img, f"Hand: {hand} | Gesture: {gesture}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    cv2.imshow("Gesture Control", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
             