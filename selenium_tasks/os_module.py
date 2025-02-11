import os

print(os.getcwd())
script_path = os.path.abspath(__file__)  
root, filename = os.path.split(script_path)
download_folder = os.path.join(root, filename.split(".")[0])
os.makedirs(download_folder, exist_ok=True)  

file_path = os.path.join(download_folder, file_name)