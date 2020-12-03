from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
import tensorflow.keras.backend as K
import numpy as np


# create the base pre-trained model
# Maybe specify input_shape()
base_model = VGG16(weights='imagenet', input_shape =(224,224,11), include_top=False)

vgg16 = base_model.output
# add a conv layer
block6_conv1 = tf.keras.layers.Conv2D(512, (3, 3), activation="relu", padding="same")))(vgg16)
# add a deconv layer
block6_deconv1 = tf.keras.layers.Conv2DTranspose(256, (3,3), strides=(2,2), activation="relu", padding="same")(block6_conv1)
# add a concatenate layer
old_output = vgg16.get_layer('block4_pool').output
block6_concat1 = tf.keras.layers.Concatenate()([block6_deconv1, old_output])

# add a conv layer
block7_conv1 = tf.keras.layers.Conv2D(512, (3, 3), activation="relu", padding="same")))(block6_concat1)
# add a deconv layer
block7_deconv1 = tf.keras.layers.Conv2DTranspose(128, (3,3), strides=(2,2), activation="relu", padding="same")(block7_conv1)
# add a concatenate layer
old_output = vgg16.get_layer('block3_pool').output
block7_concat1 = tf.keras.layers.Concatenate()([block7_deconv1, old_output])

# add a conv layer
block8_conv1 = tf.keras.layers.Conv2D(256, (3, 3), activation="relu", padding="same")))(block7_concat1)
# add a deconv layer
block8_deconv1 = tf.keras.layers.Conv2DTranspose(64, (3,3), strides=(2,2), activation="relu", padding="same")(block8_conv1)
# add a concatenate layer
old_output = vgg16.get_layer('block2_pool').output
block8_concat1 = tf.keras.layers.Concatenate()([block8_deconv1, old_output])

# add a conv layer
block9_conv1 = tf.keras.layers.Conv2D(128, (3, 3), activation="relu", padding="same")))(block8_concat1)
# add a deconv layer
block9_deconv1 = tf.keras.layers.Conv2DTranspose(32, (3,3), strides=(2,2), activation="relu", padding="same")(block9_conv1)
# add a concatenate layer
old_output = vgg16.get_layer('block1_pool').output
block9_concat1 = tf.keras.layers.Concatenate()([block9_deconv1, old_output])

# add a conv layer
block10_conv1 = tf.keras.layers.Conv2D(64, (3, 3), activation="relu", padding="same")))(block9_concat1)
# add a deconv layer
block10_deconv1 = tf.keras.layers.Conv2DTranspose(16, (3,3), strides=(2,2), activation="relu", padding="same")(block10_conv1)

# get predictions
predictions = tf.keras.layers.Conv2D(1, (3, 3), activation="softmax", padding="same")))(block10_deconv1)

# this is the model we will train
model = Model(inputs=base_model.input, outputs=predictions)

# first: train only the top layers (which were randomly initialized)
# i.e. freeze all convolutional VGG16 layers
for layer in base_model.layers:
    layer.trainable = False

def BalancedClassCrossentropy:
    def loss(y_true, y_pred) {
        sample_weight = tf.Tensor()
        for batch in len(y_true):
            nonzero_weight = tf.math.count_nonzero(y_true[batch]) / len(y_true[0])
            zero_weight = (len(y_true[0]) - num_nonzero) / len(y_true[0])
            weight = np.where(y_true[batch] == 0, zero_weight, nonzero_weight)
            weight = tf.convert_to_tensor(weight)

            sample_weight = tf.concat([sample_weight, weight], 0)
        weighted_bce_loss = K.bce(y_true, y_pred, sample_weight=sample_weight, reduction=tf.keras.losses.Reduction.SUM)
        return weighted_bce_loss
    }
    return loss


# compile the model (should be done *after* setting layers to non-trainable)
model.compile(optimizer="adam", 
              loss=BalancedClassCrossentropy(),

            #   metrics=['TruePositives',
            #            'TrueNegatives',
            #            'FalsePositives',
            #            'FalseNegatives',
            #            'Precision',
            #            'Recall'],
              metrics=['accuracy'],
              run_eagerly=True
             )


####### Data #######
# need to sample training, validation, and test data




# Fit model on training data 
# history logs loss, accuracies, and metrics
history = model.fit(
    x_train,
    y_train,
    batch_size=64,
    epochs=50,
    # We pass some validation for
    # monitoring validation loss and metrics
    # at the end of each epoch
    validation_data=(x_val, y_val),
)

# Evaluate the model on the test data using `evaluate`
print("Evaluate on test data")
results = model.evaluate(x_test, y_test, batch_size=64) 
print("test loss, test acc:", results)

# Maybe delete this last part:

# Generate predictions (probabilities -- the output of the last layer)
# on new data using `predict`
print("Generate predictions for 3 samples")
predictions = model.predict(x_test[:3])
print("predictions shape:", predictions.shape)