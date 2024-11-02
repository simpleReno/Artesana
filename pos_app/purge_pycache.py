# Import modules
import os
import shutil

# Delete Cache
def delete_pycache(root_dir='.'):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if '__pycache__' in dirnames:
            cache_path = os.path.join(dirpath, '__pycache__')
            shutil.rmtree(cache_path)
            print(f"Deleted: {cache_path}")