import cv2

cap = cv2.VideoCapture('charlie_scene1.mp4')

frame_id = 0
while (cap.isOpened()):
    ret, frame = cap.read()
    
    cv2.imshow("video", frame)

    if (frame_id >= 500 and frame_id <= 600 and frame_id % 10 == 0):
        #print('hi')
        cv2.imwrite(f"data/test/frame_{frame_id}.png", frame)

    frame_id += 1

    if cv2.waitKey(10) and 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()