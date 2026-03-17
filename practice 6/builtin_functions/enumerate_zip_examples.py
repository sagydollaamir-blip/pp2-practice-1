# enumerate — дает индекс + значение
files = ["file1.txt", "file2.txt", "file3.txt"]

print("Using enumerate:")
for index, file in enumerate(files):
    print(index, file)


# zip — объединяет несколько списков
names = ["file1.txt", "file2.txt", "file3.txt"]
sizes = [100, 200, 300]

print("\nUsing zip:")
for name, size in zip(names, sizes):
    print(f"{name} -> {size} KB")


# пример с файлами (имитация)
file_names = ["a.txt", "b.txt", "c.txt"]
file_types = ["text", "text", "text"]

combined = list(zip(file_names, file_types))
print("\nCombined list:", combined)