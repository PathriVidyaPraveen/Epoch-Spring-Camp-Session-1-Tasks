
Implement a 4-way kaleidoscope effect using NumPy and Matplotlib.
1. Grayscale Image:
● Load or generate a grayscale image using NumPy.
● Apply a 4-way kaleidoscope transformation by reflecting and rotating the quadrants appropriately
● Use Matplotlib to visualize the transformed image.
2. RGB Image:
● Extend the implementation to work with RGB images.
● Ensure that each color channel undergoes the same transformation as the grayscale version.
● Display the resulting kaleidoscope effect using Matplotlib.

My Approach and Code Explanation : 
1) Grayscale image : I have generated a gray scale image using 0 to 255 opacity pixels in a 28x28 pixel image using numpy. Then I have applied the principle of 4 way kaleidoscope transformation in which I have taken entire gray scale image generated using numpy as q1 and then applied fliplr to flip horizontally and flipud to flip vertically. So I have created 4 images of q1,q2,q3,q4 and then stacked q1 and q2 horizontally to forn upper half image and then q3 and q4 stack horizontally to form lower half image and then stacked these 2 halves vertically to create final 4-way kaleidoscope image .
2) RGB Image : I have extended the same code for RGB image except a change in the generation of RGB image using random pixels using 0-255 and 3 channels for 3 colours. 



Note : The above are generated pixels randomly using numpy. These can be extended to loaded images using cv2.imread() whose code is written in the files kaleidoscope_grayscale_load.py and kaleidoscope_rgb_load.py. Install OpenCV i=on the machine . cv2.imread() bydefault loads images into BGR format so to convert it into grayscale image , use CV2.IMREAD_GRAYSCALE and to convert it into RGB image , use cv2.cvtColor(rgb_image_loaded, cv2.COLOR_BGR2RGB).
