import pandas as pd
import numpy as np

# Excel dosyasını oku
df = pd.read_excel('Kategori5_1sonuc.xlsx')

# Boş (NaN) ve inf değerlerini 0 ile değiştir
df = df.replace([np.inf, -np.inf], np.nan)  # Sonsuz (inf) değerleri önce NaN yap
df = df.fillna(0)  # Tüm NaN değerlerini 0 ile doldur

# Sonucu yeni bir Excel dosyasına kaydet
df.to_excel('Kategori5_1sonuc.xlsx', index=False)

print("Boşluklar ve inf değerler başarıyla 0 ile değiştirildi ve sonuc_duzeltilmis.xlsx dosyasına kaydedildi.")
