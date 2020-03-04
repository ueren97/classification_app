from PIL import Image
import glob
import numpy as np


classes = ['img_a', 'img_b', 'img_c']
num_classes = len(classes)
image_size = 50
num_testdata = 100

# read images

# X -> test data, Y -> label
X_train = []
X_test = []
Y_train = []
Y_test = []

for index, classlabel in enumerate(classes):
    photos_dir = "./" + classlabel
    files = glob.glob(photos_dir + '/*.jpg')

    for i, file in enumerate(files):
        if i >= 200:
            break
        image = Image.open(file)
        image = image.convert('RGB')
        image = image.resize((image_size, image_size))
        data = np.asarray(image)

        if i < num_testdata:
            X_test.append(data)
            Y_test.append(index)
        else:
            for angle in range(-20, 20, 5):
                # rotate
                img_r = image.rotate(angle)
                data = np.asarray(img_r)
                X_train.append(data)
                Y_train.append(index)

                # transpose
                img_trans = image.transpose(Image.FLIP_LEFT_RIGHT)
                data = np.asarray(img_trans)
                X_train.append(data)
                Y_train.append(index)


X_train = np.array(X_train)
X_test = np.array(X_test)
y_train = np.array(Y_train)
y_test = np.array(Y_test)


# split data
xy = (X_train, X_test, y_train, y_test)

# save 4 variables to one file
np.save('./animal_augmented.npy', xy)
