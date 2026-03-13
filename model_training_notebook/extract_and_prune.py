import os
import zipfile
import random

zip_path = r'c:\Users\user\Downloads\plant-disease-prediction-cnn-deep-leanring-project-main\plant-disease-prediction-cnn-deep-leanring-project-main\model_training_notebook\plantvillage-dataset.zip'
extract_path = r'c:\Users\user\Downloads\plant-disease-prediction-cnn-deep-leanring-project-main\plant-disease-prediction-cnn-deep-leanring-project-main\model_training_notebook'

def prune_and_extract(zip_path, extract_path, total_limit=3000):
    with zipfile.ZipFile(zip_path, 'r') as z:
        # Get all image files in plantvillage dataset/color
        all_files = z.namelist()
        color_files = [f for f in all_files if 'plantvillage dataset/color/' in f and not f.endswith('/') and f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        if not color_files:
            print("No files found in plantvillage dataset/color/ inside the zip")
            return
            
        classes = {}
        for f in color_files:
            # e.g., 'plantvillage dataset/color/Apple___Apple_scab/image.jpg'
            parts = f.split('/')
            if len(parts) >= 2:
                class_name = parts[-2]
                if class_name not in classes:
                    classes[class_name] = []
                classes[class_name].append(f)
            
        print(f"Found {len(classes)} classes.")
        
        num_classes = len(classes)
        limit_per_class = total_limit // num_classes
        remainder = total_limit % num_classes
        
        selected_files = []
        for i, (class_name, files) in enumerate(classes.items()):
            take_count = limit_per_class + (1 if i < remainder else 0)
            if len(files) < take_count:
                selected_files.extend(files)
            else:
                selected_files.extend(random.sample(files, take_count))
                
        print(f"Selected {len(selected_files)} files to extract.")
        
        for i, f in enumerate(selected_files):
            try:
                dest_path = os.path.join(extract_path, os.path.normpath(f))
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                with open(dest_path, 'wb') as outfile:
                    outfile.write(z.read(f))
            except Exception as e:
                print(f"Error extracting {f}: {e}")
                
            if (i+1) % 500 == 0:
                print(f"Extracted {i+1} files...")
        
        print("Extraction complete.")

prune_and_extract(zip_path, extract_path, 3000)
