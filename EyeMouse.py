# use mouse with the help of eyes
# right eye for mouse move movement and left eye for clicking
import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0) # capture the video
faceMesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks= True)
screen_height , screen_width = pyautogui.size() # get the screen size

while True: # continuously record the video
    _, frame = cam.read() # read the image
    frame = cv2.flip(frame, 1)  # flip image vertically ,mirror image

    frame_height, frame_width, frame_dimension = frame.shape  # get the size of frame

    rgb_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB) # convert the color of image

    output = faceMesh.process(rgb_frame)  # process the image
    points = output.multi_face_landmarks # find the points during capture the video
    # print(points)

    if points:
        point = points[0].landmark # for handling single face

        # this loop control cursor movement

        # enumerate gives id and landmark
        for ids , landmark in enumerate(point[474 : 478]): # [474 : 478] this index helps to detect eye only
            # find selective point to detect eye
            x = int(landmark.x * frame_width)
            y = int(landmark.y * frame_height)

            # print(x , y)
            cv2.circle(frame , (x , y) , 3 , (0 , 255 , 0))
            # cv2.rectangle(frame , (x , y) , (x , y) , (0 , 255 , 0) , 3)

            if ids == 1:
                screen_x = int(landmark.x * screen_width)
                screen_y = int(landmark.y * screen_height)
                pyautogui.moveTo(screen_x , screen_y) # move the cursor with eye

        # this loop helps to click on something
        left = [point[145] , point[159]] # only upper and lower part of eye

        for landmark in left:
            x = int(landmark.x * frame_width)
            y = int(landmark.y * frame_height)
            cv2.circle(frame , (x , y) , 3 , (0 , 255 , 255))

        # helps to detect eye is blinking or not
        if(left[0].y - left[1].y) < 0.004:
            # print("click")
            pyautogui.click()
            pyautogui.sleep(1)

    cv2.imshow("Eye Mouse" , frame)
    cv2.waitKey(1)
