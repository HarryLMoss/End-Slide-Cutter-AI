# Import necessary libraries
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.applications import VGG16


# Directory paths
train_dir = '/Users/harrymoss/Library/CloudStorage/OneDrive-Personal/AI Content/Emedia AI Projects/End Slide Cutter/TRAINING STAGE/trainingSet'  # Adjust this path
validation_dir = '/Users/harrymoss/Library/CloudStorage/OneDrive-Personal/AI Content/Emedia AI Projects/End Slide Cutter/TRAINING STAGE/validationSet'  # Adjust this path
test_dir = '/Users/harrymoss/Library/CloudStorage/OneDrive-Personal/AI Content/Emedia AI Projects/End Slide Cutter/TRAINING STAGE/testSet'  # Adjust this path

# Initialize ImageDataGenerator for training and validation sets with more augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2)

validation_datagen = ImageDataGenerator(rescale=1./255)

# Updated target_size for higher resolution
target_size = (128, 128)

# Prepare data generators
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=target_size,
    batch_size=32,
    class_mode='binary')

validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=target_size,
    batch_size=32,
    class_mode='binary')

# Load the pre-trained VGG16 model as the base
base_model = VGG16(include_top=False, input_shape=target_size + (3,), weights='imagenet')
base_model.trainable = False  # Freeze the base model to avoid changing the pre-trained weights

# Model definition
model = Sequential([
    base_model,
    Flatten(),
    Dense(256, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# ModelCheckpoint to save the best model during training
checkpoint = ModelCheckpoint('best_model.h5', monitor='val_accuracy', save_best_only=True, mode='max')

# EarlyStopping callback to stop training when the validation loss stops improving
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Train the model with EarlyStopping and ModelCheckpoint callbacks
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // train_generator.batch_size,
    epochs=50,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // validation_generator.batch_size,
    callbacks=[checkpoint, early_stopping]
)

# Save the final model
model.save('final_model.h5')

# Note: Evaluate the model on your test set as needed