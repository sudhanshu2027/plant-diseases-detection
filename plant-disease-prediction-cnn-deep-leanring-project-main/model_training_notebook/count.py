import os

path = r'c:\Users\user\Downloads\plant-disease-prediction-cnn-deep-leanring-project-main\plant-disease-prediction-cnn-deep-leanring-project-main\model_training_notebook\plantvillage dataset'

total = 0
for root, dirs, files in os.walk(path):
    images = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    if images:
        total += len(images)
        print(f"{os.path.basename(root)}: {len(images)}")

print(f"Total image files: {total}")
