import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import time
from detection.detect import detect
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("Tappo, I am coming for you").wait_for_completed()
    # camera = robot.camera()

    robot.camera.image_stream_enabled = True
    robot.camera.color_image_enabled  = True   # optional

    while True:
        duration_s = 0.1  # time to display each camera frame on Cozmo's face

        latest_image = robot.world.latest_image

        if latest_image is not None:
            # robot.say_text("Tappo").wait_for_completed()

            print(latest_image.image_number)
            # print latest_image
            img = latest_image.raw_image
            img = detect(img, 0.2, 0.1, 100)
            img.show()
        break


        time.sleep(duration_s)
        # break






cozmo.run_program(cozmo_program)