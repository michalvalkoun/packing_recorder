import cv2
import msvcrt
import sys

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
while(True):
    print("Scan barcode")
    sys.stdout.flush()
    code = input()
    if (code == "end"):
        break
    output = '{}.avi'.format(code)
    out = cv2.VideoWriter(output, fourcc, 20.0, (640, 480))
    print("Saving to ", output)

    print("Recording Started")
    while(cap.isOpened()):
        ret, frame = cap.read()
        out.write(frame)
        # cv2.imshow("frame", frame)
        # if cv2.waitKey(1) == ord('q'):
        #     break
        if msvcrt.kbhit():
            while(msvcrt.kbhit()):
                msvcrt.getch()
            break
    print("Recording Ended")
    out.release()
cap.release()
