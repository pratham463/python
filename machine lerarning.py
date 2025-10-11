import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Load and normalize dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build the model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model for 10 epochs
history = model.fit(
    x_train, y_train,
    epochs=10,
    validation_data=(x_test, y_test)
)

# Evaluate model
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f"\n✅ Test accuracy: {test_acc:.4f}")

# Make predictions
predictions = model.predict(x_test)

# Change image number here 👇
img_num = 5

# Display chosen test image and prediction
plt.figure(figsize=(4, 4))
plt.imshow(x_test[img_num], cmap=plt.cm.binary)
predicted_label = tf.argmax(predictions[img_num]).numpy()
plt.title(f"Predicted: {predicted_label}, True: {y_test[img_num]}")
plt.axis('off')
plt.show()
