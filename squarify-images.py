import glob
from PIL import Image
from threading import Thread

frame_size = (640, 640)
directory = 'images'

piclist = list(sorted(glob.glob(directory + '/*.png')))


class WorkerThread(Thread):

	def __init__ (self, name='Thread'):
		Thread.__init__(self)
		self.name = name

	def run(self):		
		while True:
			actual_image = None
			try:
				actual_image = piclist.pop()
			except:
				print('[%s] no able to pop anymore...' % self.name)
				return

			new_frame = Image.new('RGB', frame_size, 'white')
			new_frame.paste(Image.open(actual_image), (0, 0))

			new_frame_path = actual_image.replace('.png', '_squared.png')
			new_frame.save(new_frame_path, 'png')

			print('[%s] saved %s' % (self.name, new_frame_path))
		
threads = []
for i in range(10):
  threads.append(
    WorkerThread(name="Thread-%d" % (i + 1)),
  )

for thread in threads:
  thread.start()
