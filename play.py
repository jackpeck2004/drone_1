#!/usr/bin/env python3

# import the necessary packages
from imutils.video import FileVideoStream
import imutils
import time
import cv2
import sys
 
# start the file video stream thread and allow the buffer to
# start to fill
fvs = FileVideoStream(sys.argv[1]).start()

# loop over frames from the video file stream
while fvs.more():
	# grab the frame from the threaded video file stream, resize
	# it, and convert it to grayscale (while still retaining 3
	# channels)
	frame = fvs.read()
	 
	# show the frame and update the FPS counter
	cv2.imshow("Frame", frame)
	cv2.waitKey(1)

	time.sleep(0.0034)
	
# do a bit of cleanup
cv2.destroyAllWindows()
fvs.stop()
