import zipfile

zip_path = r'c:\Users\user\Downloads\plant-disease-prediction-cnn-deep-leanring-project-main\plant-disease-prediction-cnn-deep-leanring-project-main\model_training_notebook\plantvillage-dataset.zip'
out_path = 'zip_info.txt'

with open(out_path, 'w') as out:
    with zipfile.ZipFile(zip_path, 'r') as z:
        files = z.namelist()
        
        color_files = [f for f in files if 'plantvillage dataset/color/' in f and not f.endswith('/') and f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        out.write(f"Total image files in plantvillage dataset/color/: {len(color_files)}\n\n")
        
        out.write("Example color files:\n")
        for f in color_files[:5]:
            out.write(f"{f}\n")
            
        classes = set()
        for f in color_files:
            parts = f.split('/')
            if len(parts) >= 2:
                classes.add(parts[-2])
                
        out.write(f"\nTotal classes found: {len(classes)}\n")
        out.write("Classes:\n")
        for c in list(classes):
            out.write(f"{c}\n")
