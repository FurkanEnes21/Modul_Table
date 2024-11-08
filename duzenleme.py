import pandas as pd

# Excel dosyasını oku
df = pd.read_excel('Modul_Tablo.xlsx')

# 2. satırı (row2) sil
df = df.drop(df.index[1])

# 'Team Name' sütunundan önceki tüm sütunları sil
team_name_index = df.columns.get_loc('Team Name')  # 'Team Name' sütununun indeksini bul
df = df.iloc[:, team_name_index:]  # Bu indeksten sonraki tüm sütunları tut

# 'Cumulative Point' sütununun adını 'B182' olarak değiştir
df.columns = df.columns.str.replace('Cumulative Point', 'B182')


# Sonucu yeni bir Excel dosyasına kaydet
df.to_excel('Modul_Tablo.xlsx', index=False)

print("2. satır silindi, 'Team Name' sütunundan önceki sütunlar kaldırıldı ve 'Cumulative Point' sütununun adı 'B182' olarak değiştirildi.")
