import os

# Создание папки
def create_directory(path):
    if not os.path.exists(path):
        os.mkdir(path)
        print(f"Folder '{path}' created")
    else:
        print(f"Folder '{path}' already exists")

# Создание вложенных папок
def create_nested_directories(path):
    os.makedirs(path, exist_ok=True)
    print(f"Nested folders '{path}' created")

# Просмотр содержимого папки
def list_directory(path):
    print(f"Contents of '{path}':")
    for item in os.listdir(path):
        print(item)

# Примеры
create_directory("test_folder")
create_nested_directories("parent/child/grandchild")
list_directory(".")