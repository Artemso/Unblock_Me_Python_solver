from PIL import Image
import numpy as np

class	Process_img():

	def	__init__(self):
		pass

	def	open_image_file(self, filename): # open an Image file and compress it to make it easier to work with and save resources
		img = Image.open(filename)
		new_wid = 75
		new_height = new_wid * (img.size[1] / img.size[0])
		img = img.resize((new_wid, int(new_height)), Image.ANTIALIAS)
		return img

	def	crop_image(self, img): # remove all unnecessary parts of the image
		wid, height = img.size
		left = wid * 0.04
		right = wid * 0.96
		top = height * 0.33
		bottom = height * 0.75
		img = img.crop((left,top,right,bottom)) # proportions were evaluated manually
		return img

	def	get_average_tile_color(self, tile):
		avg = []
		r = 0
		g = 0
		b = 0
		cnt = 0
		for line in tile:
			for cell in line:
				r += cell[0]
				g += cell[1]
				b += cell[2]
				cnt += 1
		avg = [r / cnt, g / cnt, b / cnt, 255]
		return (avg)
				

	def	detect_shapes(self, img): # split image into 36 parts, detect colors in an image, darkest- background, has red- my piece, brightest- pieces
		img = img.resize((48, 48), Image.ANTIALIAS)
		img.save('suka.png')
		img_array = np.array(img)
		print(img_array[0][0])
		blocks = list(map(lambda x : np.split(x, img_array.shape[1]/8, 1), # Split the columns
                        np.split(img_array, img_array.shape[0]/8, 0)))
		new_block = np.array(blocks)
		avg_colors = []
		for x in range(len(new_block)):
			for y in range(len(new_block[x])):
				avg_colors.append(self.get_average_tile_color(new_block[x][y]))
		new_colors = np.array(avg_colors)
		new_colors = np.reshape(new_colors, (6, 6, 4))
		print(new_colors[0][0])
		img = Image.fromarray(new_colors.astype('uint8'), 'RGBA')
		img.save('keks.png')
		img.show()

	def	detect_pieces(self, array, img):
		pass