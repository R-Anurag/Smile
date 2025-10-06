# CNN Model Section

This section contains the custom-trained CNN model used for smile detection.

## Important Notes

- **Independent of Base Dataset:**  
  The model (`smile_model.h5`) is trained privately and does **not rely** on the `dataset` folder present in the base repository.

- **Training Data:**  
  The training data used to build this CNN is **private** and not included in this repository.

- **Usage:**  
  - Ensure you have TensorFlow/Keras installed.
  - The model can be loaded with:

    ```python
    from tensorflow.keras.models import load_model
    model = load_model("output/smile_model.h5")
    ```

- **Integration:**  
  This CNN model can be used in parallel with the Haar cascade detector. You can switch between the two detection methods using the `DETECTOR_TYPE` variable in `app.py`.

- **Disclaimer:**  
  This model is trained for demonstration purposes and may not generalize to all lighting conditions, face angles, or diverse subjects. Adjust thresholds and parameters as needed for production usage.
