# camera implementation
# Using the Raspberry Pi Camera Module, you can record video when a violation is detected.
from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()

def start_video_recording():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    video_filename = f'/home/pi/videos/violation_{timestamp}.h264'
    camera.start_recording(video_filename)
    print(f"Recording video: {video_filename}")

def stop_video_recording():
    camera.stop_recording()
    print("Stopped recording")

# Example of recording a violation event
if __name__ == "__main__":
    start_video_recording()
    sleep(10)  # Record for 10 seconds
    stop_video_recording()
