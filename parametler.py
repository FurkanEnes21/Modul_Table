import pandas as pd

# Excel dosyasını oku
df = pd.read_excel('Modul_Table_New.xlsx')

# Yeni sütunlar oluşturma fonksiyonu
def yeni_sutun_olustur(df, yeni_sutun_adi, bolunen_sutun, bolen_sutun):
    df[yeni_sutun_adi] = df[bolunen_sutun] / df[bolen_sutun]
    return df

# B271'den B280'e kadar yeni sütunlar oluşturma şartları
sartlar = {
    'B271': ('B182', 'B2'),
    'B272': ('B192', 'B12'),
    'B273': ('B202', 'B22'),
    'B274': ('B212', 'B32'),
    'B275': ('B222', 'B42'),
    'B276': ('B232', 'B52'),
    'B277': ('B242', 'B62'),
    'B278': ('B252', 'B72'),
    'B279': ('B262', 'B82')
}

# Belirtilen şartlara göre sütunları oluştur
for yeni_sutun, (bolunen_sutun, bolen_sutun) in sartlar.items():
    df = yeni_sutun_olustur(df, yeni_sutun, bolunen_sutun, bolen_sutun)

# B280 sütununu özel hesaplamaya göre oluştur
df['B280'] = (df['B182'] + df['B192'] + df['B202'] + df['B212'] + df['B222'] + df['B232'] + df['B242'] + df['B252'] + df['B262']) / \
             (df['B2'] + df['B12'] + df['B22'] + df['B32'] + df['B42'] + df['B52'] + df['B62'] + df['B72'] + df['B82'])

# Sonucu yeni bir Excel dosyasına kaydet
df.to_excel('sonuc.xlsx', index=False)

print("Yeni sütunlar başarıyla oluşturuldu ve sonuc.xlsx dosyasına kaydedildi.")

