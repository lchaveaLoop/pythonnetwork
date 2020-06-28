# !wget - -no - check - certificate \
#     https: // storage.googleapis.com / laurencemoroney - blog.appspot.com / rps.zip \
#               - O / tmp / rps.zip
#
# !wget - -no - check - certificate \
#     https: // storage.googleapis.com / laurencemoroney - blog.appspot.com / rps - test - set.zip \
#               - O / tmp / rps - test - set.zip
import matplotlib
import tensorflow as tf
import os
import zipfile

from pasta.augment import inline

url1='https: // storage.googleapis.com / laurencemoroney - blog.appspot.com / rps.zip'
name1='rps.zip'
url2='https: // storage.googleapis.com / laurencemoroney - blog.appspot.com / rps - test - set.zip'
name2='rps - test - set.zip'
PATH="E:/temp/"
train_data = tf.keras.utils.get_file(name1,url1,PATH)
validation_data=tf.keras.utils.get_file(name2,url2,PATH)

zip_ref = zipfile.ZipFile("E:/temp/rps.zip", 'r')
zip_ref.extractall("/temp/")
zip_ref=zipfile.ZipFile('E:/temp/rps-test-set.zip','r')
zip_ref.extractall('/temp/')
zip_ref.close()

rock_dir = os.path.join('/tmp/rps/rock')
paper_dir = os.path.join('/tmp/rps/paper')
scissors_dir = os.path.join('/tmp/rps/scissors')

print('total training rock images:', len(os.listdir(rock_dir)))
print('total training paper images:', len(os.listdir(paper_dir)))
print('total training scissors images:', len(os.listdir(scissors_dir)))

rock_files = os.listdir(rock_dir)
print(rock_files[:10])

paper_files = os.listdir(paper_dir)
print(paper_files[:10])

scissors_files = os.listdir(scissors_dir)
print(scissors_files[:10])

# %matplotlib inline

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

pic_index = 2

next_rock = [os.path.join(rock_dir, fname)
                for fname in rock_files[pic_index-2:pic_index]]
next_paper = [os.path.join(paper_dir, fname)
                for fname in paper_files[pic_index-2:pic_index]]
next_scissors = [os.path.join(scissors_dir, fname)
                for fname in scissors_files[pic_index-2:pic_index]]

for i, img_path in enumerate(next_rock+next_paper+next_scissors):
  #print(img_path)
  img = mpimg.imread(img_path)
  plt.imshow(img)
  plt.axis('Off')
  plt.show()