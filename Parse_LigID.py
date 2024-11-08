import pandas as pd
import re

# .xlsx dosyasını oku
file_path = 'C:\\Users\\Dell\\Desktop\\0-90\Güncel_ham_dosya1.xlsx'  # Dosya yolunu buraya ekleyin
df = pd.read_excel(file_path)

# Lig ID'sini çıkarmak için bir fonksiyon tanımlayalım
def extract_lig_id(file_name):
    # Regex kullanarak S610 ile başlayan ve büyük harflerle devam eden ID'yi alır
    match = re.search(r'S635[A-Z0-9]+', file_name)
    if match:
        return match.group(0)
    return None

# 'File_Name' sütunundan Lig ID'yi çıkar ve yeni bir sütuna ekle
df['Lig ID'] = df['File_Name'].apply(extract_lig_id)

# Sonuçları aynı dosyaya veya yeni bir dosyaya kaydedelim
output_path = 'C:\\Users\\Dell\\Desktop\\0-90\\Güncel_ham_dosya1.xlsx'  # Kaydetmek istediğiniz yolu belirtin
df.to_excel(output_path, index=False)

print("İşlem tamamlandı, dosya kaydedildi.")