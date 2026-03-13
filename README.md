# plant-disease-prediction-cnn-deep-learning-project

# 🌿 Plant Disease Detection using Deep Learning

A deep learning based web application that detects plant diseases from leaf images.  
The system uses a Convolutional Neural Network (CNN) trained on the **PlantVillage dataset** to classify plant diseases across **38 classes** with high accuracy.

---

# 🚀 Live Demo

🔗 **Application:**  
https://plant-diseases-detection-8xlw.onrender.com

---

# 💻 GitHub Repository

🔗 **Source Code:**  
https://github.com/sudhanshu2027/plant-diseases-detection

---

# 📸 Application Demo

Upload a plant leaf image and the model predicts the disease in real time.

![Plant Disease Detection Demo](assets/demo.png)

---

# 📌 Features

- 🌱 Detects plant diseases from leaf images
- 🧠 Deep Learning based classification
- 📊 Supports **38 plant disease categories**
- ⚡ Fast prediction using trained CNN model
- 🌐 User-friendly web interface using **Streamlit**
- 📈 High accuracy model for disease detection

---

# 🧠 Model Details

| Parameter | Value |
|-----------|------|
| Model Type | Convolutional Neural Network (CNN) |
| Framework | TensorFlow / Keras (Keras 3) |
| Optimizer | Adam |
| Training Accuracy | **97%** |
| Validation Accuracy | **96.5%** |
| Dataset | PlantVillage Dataset |
| Classes | 38 |

> [!TIP]
> **Model Backup:** A backup of the trained model is available on [Google Drive](https://drive.google.com/file/d/1jhMS3HGidPxc3BUPwq4yphimqU_UrqeN/view?usp=drive_link).

---

# 🛠️ Tech Stack

### Machine Learning / Deep Learning
- Python
- TensorFlow / Keras
- NumPy
- Pillow

### Web Application
- Streamlit

---

## 📂 Project Structure

```text
plant-diseases-detection
│
├── .gitignore
├── .python-version
├── requirements.txt
├── render.yaml
├── README.md
│
├── app
│   ├── main.py
│   ├── class_indices.json
│   ├── config.toml
│   ├── credentials.toml
│   └── trained_model
│        ├── plant_disease_prediction_model1.h5
│        └── trained_model_link.txt
│
├── assets
│   └── demo.png
│
├── model_training_notebook
│   └── Plant_Disease_Prediction_CNN_Image_Classifier.ipynb
│
└── test_images
```

---

# 🧪 Dataset

The model was trained using the **PlantVillage Dataset**.

Dataset: [PlantVillage Dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/sudhanshu2027/plant-diseases-detection.git
cd plant-diseases-detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application locally:

```bash
streamlit run app/main.py
```

---

# 🖼️ How It Works

1️⃣ Upload a plant leaf image  
2️⃣ Image preprocessing is applied  
3️⃣ The trained CNN model predicts the disease  
4️⃣ The predicted class is displayed

---

# 👨‍💻 Author

**Sudhanshu Kumar**

GitHub: [sudhanshu2027](https://github.com/sudhanshu2027)  
LinkedIn: [sudhanshu2027](https://www.linkedin.com/in/sudhanshu2027/)

---
