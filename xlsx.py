import os
import pandas as pd

# CSV dosyalarını .xlsx dosyalarına dönüştüren fonksiyon
def convert_csv_to_excel(csv_folder_path, excel_folder_path):
    # CSV dosyalarının bulunduğu klasörü oku
    for file_name in os.listdir(csv_folder_path):
        if file_name.endswith('.csv'):
            csv_file_path = os.path.join(csv_folder_path, file_name)
            
            # CSV dosyasını oku
            df = pd.read_csv(csv_file_path)
            
            # .xlsx dosya adını oluştur
            excel_file_name = file_name.replace('.csv', '.xlsx')
            excel_file_path = os.path.join(excel_folder_path, excel_file_name)
            
            # Excel dosyasını oluştur ve kaydet
            df.to_excel(excel_file_path, index=False)
    
    print("Tüm CSV dosyaları .xlsx formatına dönüştürüldü.")

# CSV dosyalarının bulunduğu klasör yolu
csv_folder_path = 'C:\\Users\\Dell\\Desktop\\0-90\\Data'

# .xlsx dosyalarının kaydedileceği klasör yolu
excel_folder_path = 'C:\\Users\\Dell\\Desktop\\0-90\\Excel Data'

# Dönüştürme işlemini başlat
convert_csv_to_excel(csv_folder_path, excel_folder_path)
