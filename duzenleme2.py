import pandas as pd

# Excel dosyasını oku
df = pd.read_excel('incomplete_matches_with_previous_week_parameters2.xlsx')

# Sütun isimlerini düzenle
df.columns = df.columns.str.replace(r'Güncellenmiş_Mod\d+_sıralama_tablosu\.xlsx_home_ID', 'ID', regex=True)

df.columns = df.columns.str.replace(r'Güncellenmiş_Mod\d+_sıralama_tablosu\.xlsx_away_ID', 'ID', regex=True)


# Sonucu yeni bir Excel dosyasına kaydet
df.to_excel('incomplete_matches_with_previous_week_parameters2.xlsx', index=False)

print("Sütun isimleri başarıyla 'ID' ile değiştirildi ve sonuc_sutunlar_degisti.xlsx dosyasına kaydedildi.")
    


# import pandas as pd

# # Excel dosyasını oku
# df = pd.read_excel('incomplete_matches_with_previous_week_parameters2.xlsx')

# # Yeni sütun adları için bir liste
# new_column_names = []
# # Sütun adlarını belirlemek için bir sayaç
# counter = 1

# # DataFrame'deki her sütun için
# for column in df.columns:
#     # Eğer sütun adı home ile başlıyorsa
#     if 'Güncellenmiş_Mod' in column and '_home_' in column:
#         new_column_names.append(f'B{counter}')  # 'B1', 'B2', vb.
#         counter += 1  # Sayaç artır
#     elif 'Güncellenmiş_Mod' in column and '_away_' in column:  # away sütunları
#         new_column_names.append(f'B{counter}')  # 'B1', 'B2', vb.
#         counter += 1  # Sayaç artır
#     else:
#         new_column_names.append(column)  # Diğer sütunları olduğu gibi bırak

# # Sütun adlarını değiştir
# df.columns = new_column_names

# # Sonucu yeni bir Excel dosyasına kaydet
# df.to_excel('incomplete_matches_with_previous_week_parameters2.xlsx', index=False)

# print("Sütun isimleri başarıyla değiştirildi ve sonuc_sutunlar_degisti.xlsx dosyasına kaydedildi.")

