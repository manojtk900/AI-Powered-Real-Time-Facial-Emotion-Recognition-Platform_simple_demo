import tensorflow as tf

try:
    model = tf.keras.models.load_model("model.h5")
    print("✅ Model loaded successfully!")
    print("Input shape:", model.input_shape)
    print("Output shape:", model.output_shape)
except Exception as e:
    print("❌ Error loading model:")
    print(e)
