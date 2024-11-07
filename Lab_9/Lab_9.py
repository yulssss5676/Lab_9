
# Функція для відкриття файлу з обробкою помилок
def open_file(file_name, mode):
    try:
        file = open(file_name, mode)
    except IOError:
        print(f"File {file_name} wasn't opened!")
        return None
    else:
        print(f"File {file_name} was opened!")
        return file

# Функція для перевірки симетричних слів
def is_symmetric(word):
    return word == word[::-1]

# Створення файлу TF15_1.txt і запис даних
file1_name = "TF15_1.txt"
file1 = open_file(file1_name, "w")

if file1:
    file1.write("Madam Arora teaches malayalam civic racecar level anna kayak deed rotator")
    print("Information was successfully added to TF15_1.txt!")
    file1.close()
    print("File TF15_1.txt was closed!")

# Читання файлу TF15_1.txt і знаходження симетричних слів
file2_name = "TF15_2.txt"
file1 = open_file(file1_name, "r")
file2 = open_file(file2_name, "w")

if file1 and file2:
    content = file1.read().split()
    symmetric_words = [word for word in content if is_symmetric(word)]

    if symmetric_words:
        file2.write(" ".join(symmetric_words))
        print("Symmetric words were written to TF15_2.txt!")
    else:
        print("No symmetric words found.")

    file1.close()
    file2.close()
    print("Files were closed!")

# Читання файлу TF15_2.txt і виведення його вмісту по рядках
file2 = open_file(file2_name, "r")

if file2:
    for line in file2.read().split():
        print(line)
    file2.close()
    print("File TF15_2.txt was closed!")

