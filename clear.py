import os
import glob

# Silinecek dosya yolları listesi
directories = [
    r"C:\Users\Dell\Desktop\0-90\Data",
    r"C:\Users\Dell\Desktop\0-90\Excel Data",
    "."
]

# Her bir dizindeki tüm .xlsx dosyalarını bulur ve siler
for directory in directories:
    # Belirtilen dizindeki tüm .xlsx dosyalarını bulur
    xlsx_files = glob.glob(os.path.join(directory, "*.xlsx"))
    
    # Her bir dosyayı siler
    for file in xlsx_files:
        os.remove(file)
        print(f"{file} silindi.")
