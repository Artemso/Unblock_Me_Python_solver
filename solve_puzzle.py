from analyse_image import Process_img
import sys

proc = Process_img()
img = proc.open_image_file(sys.argv[1])
img = proc.crop_image(img)
proc.detect_shapes(img)