import time
import picamera

VIDEO_DAYS = 1
FRAMES_PER_HOUR = 60
FRAMES = FRAMES_PER_HOUR * 24 * VIDEO_DAYS

def capture_frame(frame):
    with picamera.PiCamera() as cam:
        time.sleep(2)
        cam.capture('/home/pi/cameraPi/frames/frame%03d.jpg' % frame)

for frame in range(FRAMES):
    start = time.time()
    capture_frame(frame)

    time.sleep(
        int(60 * 60 / FRAMES_PER_HOUR) - (time.time() - start)
)

# ffmpeg -y -f image2 -i /home/pi/cameraPi/frames/frame%03d.jpg -r 24 -vcodec libx264 -profile high -preset slow /home/pi/cameraPi/timelapse.mp4
