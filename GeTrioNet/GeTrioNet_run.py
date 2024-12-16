"""
GeTrioNet - нейросеть, которая определяет на фотографии круг, квадрат, треугольник.
"""
import os
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tf_keras.preprocessing.image import load_img, img_to_array

def load_data(path_to_data):
    images = []
    labels = []
    class_names = ['circle', 'square', 'triangle']

    for class_name in class_names:
        class_folder = os.path.join(path_to_data, class_name)
        for img_name in os.listdir(class_folder):
            img_path = os.path.join(class_folder, img_name)
            img = load_img(img_path, target_size=(100, 100))
            img = img_to_array(img)
            images.append(img)
            labels.append(class_names.index(class_name))

    images = np.array(images)
    labels = np.array(labels)

    return images, labels


if __name__ == "__main__":

    # Путь к данным для обучения
    data_path = "geometric_shapes"

    # Загружаем данные из базы
    images, labels = load_data(data_path)

    # Разделение на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)


    y_train_cat = tf.keras.utils.to_categorical(y_train, num_classes=3)
    y_test_cat = tf.keras.utils.to_categorical(y_test, num_classes=3)

    # Создание модели
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(3, activation='softmax')  # 3 класса: круг, квадрат, треугольник
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Обучение модели
    model.fit(X_train, y_train_cat, epochs=10, batch_size=16, validation_data=(X_test, y_test_cat))

    loss, accuracy = model.evaluate(X_test, y_test_cat)
    print(f'Accuracy: {accuracy * 100:.2f}%')