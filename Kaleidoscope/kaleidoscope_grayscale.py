import numpy as np
import matplotlib.pyplot as plt

gray_image_generated = np.random.randint(0,256,(28,28))

# plt.imshow(gray_image_generated , cmap = 'gray')
# plt.axis('off')
# plt.show()

#Divide the 4 qs of the gray scale image generated
# q1 = gray_image_generated[:14,14:28]
# q2 = gray_image_generated[:14,:14]
# q3 = gray_image_generated[14:28,:14]
# q4 = gray_image_generated[14:28,14:28]

# fig,axs = plt.subplots(4,1,figsize=(20,5))
# axs[0].imshow(q1 , cmap='gray')
# axs[1].imshow(q2 , cmap='gray')
# axs[2].imshow(q3 , cmap='gray')
# axs[3].imshow(q4 , cmap='gray')


# # Adjust layout
# fig.tight_layout()
# plt.show()
q1 = gray_image_generated
q2 = np.fliplr(q1)
q3 = np.flipud(q1)
q4 = np.flipud(np.fliplr(q1))

above_x = np.hstack([q1,q2])
below_x = np.hstack([q3,q4])
kaleidoscope_output_image = np.vstack([above_x , below_x])

fig,(original,output) = plt.subplots(1,2,figsize=(12,4))
original.imshow(gray_image_generated,cmap="gray")
original.set_title("Original Grayscale Image",color='blue')

output.imshow(kaleidoscope_output_image,cmap="gray")
output.set_title("Output image of 4-way kaleidoscope effect",color='red')

plt.tight_layout()
original.axis('off')
output.axis('off')
plt.show()





