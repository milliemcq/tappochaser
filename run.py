import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import time
from detection.detect import *
from detection.utils import *
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("Tappo, I am coming for you").wait_for_completed()
    # camera = robot.camera()
    suppress_labels = [label for label in voc_labels if label not in ["dog"]]
    dog_index = label_map["dog"]
    print(f"Dog index {dog_index}")

    robot.camera.image_stream_enabled = True
    robot.camera.color_image_enabled  = True   # optional

    while True:
        duration_s = 0.1  # time to display each camera frame on Cozmo's face

        latest_image = robot.world.latest_image
        output_img = None

        if latest_image is not None:

            # robot.say_text("Tappo").wait_for_completed()
            if latest_image.image_number % 10 == 0:
                print(latest_image.image_number)
                img = latest_image.raw_image
                det_boxes, det_labels, det_scores = detect_from_raw_pil(img, 0.1, 0.1, 100)
                print(det_labels)
                if dog_index in det_labels[0].tolist():
                    print("Found Tappo")
                    img.show()
                    robot.say_text("Tappo I see you").wait_for_completed()
        if output_img is not None:
            break

        if latest_image.image_number > 1000:
            break
        # time.sleep(duration_s)
        # break


    
    output_img.show()



cozmo.run_program(cozmo_program, use_viewer=True)