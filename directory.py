
import os
directory_structure = {
    'fastAPI': ['__init__.py', 'crud.py', 'database.py', 'main.py', 'models.py', 'schemas.py']
}

# Check if directories and files exist, and create them if necessary
for files in directory_structure.values():
    for file in files:
        file_path = os.path.join(file)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write('') 
