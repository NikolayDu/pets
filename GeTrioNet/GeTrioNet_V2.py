import matplotlib.pyplot as plt
import numpy as np
import os
import pathlib
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Проверка на доступные GPU
physical_devices = tf.config.list_physical_devices('GPU')
print(physical_devices)

print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))


# if physical_devices:
#     print("Num GPUs Available: ", len(physical_devices))
#     for gpu in physical_devices:
#         print("GPU available: ", gpu)
# else:
#     print("No GPUs detected.")
#
# # Настройка памяти GPU
# gpus = tf.config.experimental.list_physical_devices('GPU')
# if gpus:
#     try:
#         for gpu in gpus:
#             tf.config.experimental.set_virtual_device_configuration(
#                 gpu,
#                 [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=4096)])  # Установите лимит по памяти
#     except RuntimeError as e:
#         print(e)
#
# data_dir = "geometric_shapes"
# data_dir = pathlib.Path(data_dir)
#
# image_count = len(list(data_dir.glob('*/*.png')))
# print('Всего картинок', image_count)
#
# circle = list(data_dir.glob('circle/*'))
# square = list(data_dir.glob('square/*'))
# triangle = list(data_dir.glob('triangle/*'))
#
# print(len(circle), len(square), len(triangle))
#
# batch_size = 32
# img_height = 180
# img_width = 180
#
# train_ds = tf.keras.utils.image_dataset_from_directory(
#     data_dir,
#     validation_split=0.2,
#     subset="training",
#     seed=123,
#     image_size=(img_height, img_width),
#     batch_size=batch_size)
#
# val_ds = tf.keras.utils.image_dataset_from_directory(
#     data_dir,
#     validation_split=0.2,
#     subset="validation",
#     seed=123,
#     image_size=(img_height, img_width),
#     batch_size=batch_size)
#
# class_names = train_ds.class_names
# print(class_names)
#
# plt.figure(figsize=(10, 10))
# for images, labels in train_ds.take(1):
#     for i in range(9):
#         ax = plt.subplot(3, 3, i + 1)
#         plt.imshow(images[i].numpy().astype("uint8"))
#         plt.title(class_names[labels[i]])
#         plt.axis("off")
#
# AUTOTUNE = tf.data.AUTOTUNE
#
# train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
# val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
#
# normalization_layer = layers.Rescaling(1. / 255)
#
# normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
# image_batch, labels_batch = next(iter(normalized_ds))
# first_image = image_batch[0]
#
# num_classes = len(class_names)
#
# # Использование MirroredStrategy
# strategy = tf.distribute.MirroredStrategy()
# print('Number of devices: %d' % strategy.num_replicas_in_sync)
#
# with strategy.scope():
#     model = tf.keras.models.Sequential([
#         layers.Rescaling(1. / 255, input_shape=(img_height, img_width, 3)),
#         layers.Conv2D(16, 3, padding='same', activation='relu'),
#         layers.MaxPooling2D(),
#         layers.Conv2D(32, 3, padding='same', activation='relu'),
#         layers.MaxPooling2D(),
#         layers.Conv2D(64, 3, padding='same', activation='relu'),
#         layers.MaxPooling2D(),
#         layers.Flatten(),
#         layers.Dense(128, activation='relu'),
#         layers.Dense(num_classes)
#     ])
#
#     model.compile(optimizer='adam',
#                   loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
#                   metrics=['accuracy'])
#
# epochs = 10
# history = model.fit(
#     train_ds,
#     validation_data=val_ds,
#     epochs=epochs
# )
#
# acc = history.history['accuracy']
# val_acc = history.history['val_accuracy']
# loss = history.history['loss']
# val_loss = history.history['val_loss']
#
# epochs_range = range(epochs)
#
# plt.figure(figsize=(8, 8))
# plt.subplot(1, 2, 1)
# plt.plot(epochs_range, acc, label='Training Accuracy')
# plt.plot(epochs_range, val_acc, label='Validation Accuracy')
# plt.legend(loc='lower right')
# plt.title('Training and Validation Accuracy')
#
# plt.subplot(1, 2, 2)
# plt.plot(epochs_range, loss, label='Training Loss')
# plt.plot(epochs_range, val_loss, label='Validation Loss')
# plt.legend(loc='upper right')
# plt.title('Training and Validation Loss')
# plt.show()