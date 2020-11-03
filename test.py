import cv2
from collections import defaultdict

reverse_lookup = {
    'CAP_PROP_POS_FRAMES'           : 1,
    'CAP_PROP_POS_AVI_RATIO'        : 2,
    'CAP_PROP_FRAME_WIDTH'          : 3,
    'CAP_PROP_FRAME_HEIGHT'         : 4,
    'CAP_PROP_POS_MSEC'             : 0,
    'CAP_PROP_FPS'                  : 5,
    'CAP_PROP_FOURCC'               : 6,
    'CAP_PROP_FRAME_COUNT'          : 7,
    'CAP_PROP_FORMAT'               : 8,
    'CAP_PROP_MODE'                 : 9,
    'CAP_PROP_BRIGHTNESS'           : 10,
    'CAP_PROP_CONTRAST'             : 11,
    'CAP_PROP_SATURATION'           : 12,
    'CAP_PROP_HUE'                  : 13,
    'CAP_PROP_GAIN'                 : 14,
    'CAP_PROP_EXPOSURE'             : 15,
    'CAP_PROP_CONVERT_RGB'          : 16,
    'CAP_PROP_WHITE_BALANCE_BLUE_U' : 17,
    'CAP_PROP_RECTIFICATION'        : 18,
    'CAP_PROP_MONOCHROME'           : 19,
    'CAP_PROP_SHARPNESS'            : 20,
    'CAP_PROP_AUTO_EXPOSURE'        : 21,
    'CAP_PROP_GAMMA'                : 22,
    'CAP_PROP_TEMPERATURE'          : 23,
    'CAP_PROP_TRIGGER'              : 24,
    'CAP_PROP_TRIGGER_DELAY'        : 25,
    'CAP_PROP_WHITE_BALANCE_RED_V'  : 26,
    'CAP_PROP_ZOOM'                 : 27,
    'CAP_PROP_FOCUS'                : 28,
    'CAP_PROP_GUID'                 : 29,
    'CAP_PROP_ISO_SPEED'            : 30,
    'CAP_PROP_BACKLIGHT'            : 32,
    'CAP_PROP_PAN'                  : 33,
    'CAP_PROP_TILT'                 : 34,
    'CAP_PROP_ROLL'                 : 35,
    'CAP_PROP_IRIS'                 : 36,
    'CAP_PROP_SETTINGS'             : 37,
    'CAP_PROP_BUFFERSIZE'           : 38,
    'CAP_PROP_AUTOFOCUS'            : 39,
}

lookup = defaultdict(str)

for k, v in reverse_lookup.items():
    lookup[v] = k
    
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

ret1 = cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) #640
ret2 = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720) # 360
ret3 = cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 5) # was 0.25
ret4 = cap.set(cv2.CAP_PROP_EXPOSURE, -11) # -5 == 2**-5 == 1/32 seconds
ret5 = cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
ret6 = cap.set(cv2.CAP_PROP_BRIGHTNESS, 0.0)
ret7 = cap.set(cv2.CAP_PROP_FPS, 150) # was 60
ret8 = cap.set(cv2.CAP_PROP_CONTRAST, 0)

print(cv2.__version__)
print()

for i in range(1, 40):
    print(lookup[i], ': ', cap.get(i))


fourcc = cv2.VideoWriter_fourcc(*'MJPG')
writer = cv2.VideoWriter('test_file.avi', fourcc, 120.0, (1280, 720), False)
cnt = 0

ret, frame = cap.read()

while ret and cnt < 1000:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    writer.write(gray)
    cnt += 1
    cv2.waitKey(1000//150)

writer.release()
cap.release()
