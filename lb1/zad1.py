import shutil

filename = input("Podaj nazwe pliku: ")
destination = "lab1zad1.txt"
shutil.copy(filename, destination)
print(f"plik {filename} skopiowany do {destination}.")