from PIL import Image
from PIL import ImageOps
from detect import detect
from utils import voc_labels
img_path = 'tappo.jpg'
original_image = Image.open(img_path, mode='r')
original_image = original_image.convert('RGB')
suppress_labels = [label for label in voc_labels if label not in ["dog"]]
detect(original_image, min_score=0.2, max_overlap=0.1, top_k=1000, suppress=suppress_labels).show()
print("test")