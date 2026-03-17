import shutil
import os

# Перемещение файла
def move_file(src, dest):
    shutil.move(src, dest)
    print(f"Moved '{src}' to '{dest}'")

# Копирование файла
def copy_file(src, dest):
    shutil.copy(src, dest)
    print(f"Copied '{src}' to '{dest}'")

# Переименование файла
def rename_file(old_name, new_name):
    os.rename(old_name, new_name)
    print(f"Renamed '{old_name}' to '{new_name}'")

# Примеры
# move_file("test.txt", "test_folder/test.txt")
# copy_file("test.txt", "copy_test.txt")
# rename_file("copy_test.txt", "renamed_test.txt")