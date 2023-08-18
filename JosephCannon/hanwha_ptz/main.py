from source import sunapi_control
from source import sunapi_config
import time
import datetime

import numpy as np

Camera1 = sunapi_control.CameraControl('10.31.81.246', 'admin', '')
Camera2 = sunapi_config.CameraConfiguration('10.31.81.246', 'admin', '')

# Camera1.snap_shot('/home/waggle/... /name_given_to_image.jpg')
# Camera1.snap_shot()
# Camera1.absolute_control(zoom=1)


# Camera1.relative_control(pan=-220, tilt=-30,zoom=5)
# Camera1.continuous_control(normalized_speed=True, pan=40)
# Camera1.continuous_control(focus='Near')
# Camera1.stop_control()
# Camera1.attributes_information()
# Camera1.area_zoom(1000, 100, 1000, 100)
# Camera1.movement_control(movespeed=6, direction='Left')
# Camera1.requesting_cameras_position_information("print")
# Camera1.moving_to_preset_position(preset=1)
# Camera1.zoom_out()
# Camera1.aux_control('WiperOn')
# Camera1.attributes_information()
# Camera1.absolute_control(pan=143, tilt=0, zoom=2)
#
# resp = Camera1.snap_shot(directory='/home/waggle/git/summer2023/JosephCannon/hanwha_ptz/snapshots/Jul_13_2023_16_34_04_.jpg')
# image = Image.open('/home/waggle/git/summer2023/JosephCannon/hanwha_ptz/snapshots/Jul_13_2023_16_34_04_.jpg')
#
# image.show()
#
# Camera1.relative_control(pan=33)
# resp = Camera1.snap_shot(directory='/home/waggle/git/summer2023/JosephCannon/hanwha_ptz/snapshots/Jul_13_2023_16_34_04_.jpg')
# image = Image.open('/home/waggle/git/summer2023/JosephCannon/hanwha_ptz/snapshots/Jul_13_2023_16_34_04_.jpg')
#
# image.show()


# Camera1.area_zoom(8000, 9000, 7000, 8000)
# Camera1.swing_control(channel=0, mode='PanTilt')
# Camera1.group_control(channel=0, group=1, mode='Start')
# Camera1.tour_control(chanel=0, tour=1, mode='Stop')
# Camera1.trace_control(channel=0, trace=1, mode='Stop')
# Camera1.applications()

# Camera2.swing_setup(action='view', channel=0)

# Camera2.swing_setup(action='set', channel=0, mode='PanTilt', from_preset=1,
#                     to_preset=2, speed=60, dwell_time=2)

# # adds to the end of the list up to 128 preset positions
# Camera2.group_setup(action='add', channel=0, group=1, preset=4, speed=50, dwell_time=1)

# # updates the preset in the preset sequence selected. ex. if preset sequence is 3, and
# # preset is 4, update position 3 of the preset sequence to be preset 4
# Camera2.group_setup(action='update', channel=0, group=1, preset_sequence=3, preset=4, speed=50, dwell_time=1)

# Camera2.group_setup(action='remove', channel=0, group=1)

# Camera2.group_setup(action='view', channel=0, group=2)

# _ = 0
# i = 0
# Camera1.snap_shot()
#
# while _ != 4:
#     i = i + 1
#     Camera1.relative_control(pan=62.25)
#     Camera1.snap_shot()
#     _ = _ + 1
#
# Camera1.relative_control(pan=48.75)
# Camera1.snap_shot()
# Camera1.relative_control(pan=62.25)
#
# print(i)

"Camera1.absolute_control(pan=100, tilt=0, zoom=2)"
# Camera1.stop_control()
# Camera1.zoom_out()
# Camera1.swing_control(0, 'PanTilt')
# Camera1.area_zoom(4000, 5000, 6000, 7000)
# Camera1.absolute_control(pan=290, tilt=-10, zoom=10)
# Camera1.absolute_control(zoom_pulse=90)
# Camera1.relative_control(pan=180, tilt=60, zoom=5)
# Camera1.area_zoom(4000, 5000, 6000, 7000)


"""from PIL import Image

i = 0

while i < 4:
    directory = '/home/waggle/git/summer2023/JosephCannon/hanwha_ptz/snapshots/image' + str(i) + '.jpg'
    Camera1.snap_shot(directory=directory)
    Camera1.relative_control(pan=-33)
    i = i+1

#Read the array of images

image = []

for j in range(0,i):

    pic = Image.open('/home/waggle/git/summer2023/JosephCannon/hanwha_ptz/snapshots/image' + str(j) + '.jpg')

    image.append(pic)

print(image[0])
#resize, first image

# image1 = image1.crop((480,0,1440,1080))  # .crop (left, top, right, bottom)

image_size = []

for k in range(0,i):

    size = image[k].size

    image_size.append(size)

print(image_size[0][0])

# image2_size = image2.size
# image3_size = image3.size
# image4_size = image4.size
# image5_size = image5.size
#
# print(str(image1_size[0]))
#

new_image = Image.new('RGB', (i * image_size[0][0], image_size[0][1]), (250, 250, 250))

for l in range(i):
    z = image_size[0][0]*l
    print(z)
    new_image.paste(image[l],(image_size[0][0]*l,0))  # start of image at 1920
    # new_image.paste(image3,(image1_size[0]*2,0))  # start of image at 1920*2
    # new_image.paste(image4,(image1_size[0]*3,0))
    # new_image.paste(image5,(image1_size[0]*4,0))

new_image.save("/home/waggle/git/summer2023/JosephCannon/hanwha_ptz/snapshots/poster_image.jpg","JPEG")
new_image.show()"""