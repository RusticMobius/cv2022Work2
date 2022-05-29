from PIL import Image

img = Image.open('../datasets/test/image-parse/02_vis.png')
print(len(img.split()))
