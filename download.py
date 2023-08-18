import matplotlib.pyplot as plt
from PIL import Image

img_path = 'data\Chapter3\狗狗2.jpg'

img = Image.open(img_path)

plt.imshow(img)
plt.axis('off')
plt.show()