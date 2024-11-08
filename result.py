import pandas as pd

# Excel dosyasını oku
df = pd.read_excel('Güncel_ham_dosya1.xlsx')

# 0-45-result sütununu oluştur
df['0-45-result'] = df.apply(lambda row: 1 if row['0-45-home'] > row['0-45-away'] 
                             else (0 if row['0-45-home'] == row['0-45-away'] else 2), axis=1)

# 0-90-result sütununu oluştur
df['0-90-result'] = df.apply(lambda row: 1 if row['0-90-home'] > row['0-90-away'] 
                             else (0 if row['0-90-home'] == row['0-90-away'] else 2), axis=1)

# Sonuçları yeni bir Excel dosyasına kaydet
df.to_excel('Güncel_ham_dosya1.xlsx', index=False)

print("Dosya başarıyla güncellendi!")
