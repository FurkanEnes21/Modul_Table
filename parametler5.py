
import pandas as pd

# Excel dosyasını oku
df = pd.read_excel('Kategori4_1sonuc.xlsx')

# Yeni sütunlar oluşturma fonksiyonu
def yeni_sutun_olustur(df, yeni_sutun_adi, bolunen_sutun, bolen_sutun):
    with pd.option_context('mode.use_inf_as_na', True):
        df[yeni_sutun_adi] = df[bolunen_sutun] / df[bolen_sutun]
        df[yeni_sutun_adi].fillna(0, inplace=True)  # 0/0 durumunda 0 olarak kabul et
    return df

# Belirtilen şartlara göre sütunları oluşturma
sartlar = {
    'B361': ('B182', 'B92'),
    'B362': ('B192', 'B102'),
    'B363': ('B202', 'B112'),
    'B364': ('B212', 'B122'),
    'B365': ('B222', 'B132'),
    'B366': ('B232', 'B142'),
    'B367': ('B242', 'B152'),
    'B368': ('B252', 'B162'),
    'B369': ('B262', 'B172'),
    'B371': ('B184', 'B94'),
    'B372': ('B194', 'B104'),
    'B373': ('B204', 'B114'),
    'B374': ('B214', 'B124'),
    'B375': ('B224', 'B134'),
    'B376': ('B234', 'B144'),
    'B377': ('B244', 'B154'),
    'B378': ('B254', 'B164'),
    'B379': ('B264', 'B174'),
    'B381': ('B185', 'B95'),
    'B382': ('B195', 'B105'),
    'B383': ('B205', 'B115'),
    'B384': ('B215', 'B125'),
    'B385': ('B225', 'B135'),
    'B386': ('B235', 'B145'),
    'B387': ('B245', 'B155'),
    'B388': ('B255', 'B165'),
    'B389': ('B265', 'B175'),
    'B391': ('B189', 'B19'),
    'B392': ('B199', 'B109'),
    'B393': ('B209', 'B119'),
    'B394': ('B219', 'B129'),
    'B395': ('B229', 'B139'),
    'B396': ('B239', 'B149'),
    'B397': ('B249', 'B159'),
    'B398': ('B259', 'B169'),
    'B399': ('B269', 'B179')
    
}

# Belirtilen şartlara göre sütunları oluştur
for yeni_sutun, (bolunen_sutun, bolen_sutun) in sartlar.items():
    if '-' in bolen_sutun:
        bolen_sutun_adi = bolen_sutun.split('-')
        df[yeni_sutun] = df[bolunen_sutun] / (df[bolen_sutun_adi[0]] - df[bolen_sutun_adi[1]])
    else:
        df = yeni_sutun_olustur(df, yeni_sutun, bolunen_sutun, bolen_sutun)

# Özel hesaplamalar
df['B370'] = (df['B182'] + df['B192'] + df['B202'] + df['B212'] + df['B222'] + df['B232'] + df['B242'] + df['B252'] + df['B262']) / \
             (df['B92'] + df['B102'] + df['B112'] + df['B122'] + df['B132'] + df['B142'] + df['B152'] + df['B162'] + df['B172'])

df['B380'] = (df['B184'] + df['B194'] + df['B204'] + df['B214'] + df['B224'] + df['B234'] + df['B244'] + df['B254'] + df['B264']) / \
             (df['B94'] + df['B104'] + df['B114'] + df['B124'] + df['B134'] + df['B144'] + df['B154'] + df['B164'] + df['B174'])

df['B390'] = (df['B185'] + df['B195'] + df['B205'] + df['B215'] + df['B225'] + df['B235'] + df['B245'] + df['B255'] + df['B265']) / \
             (df['B95'] + df['B105'] + df['B115'] + df['B125'] + df['B135'] + df['B145'] + df['B155'] + df['B165'] + df['B175'])

df['B400'] = (df['B189'] + df['B199'] + df['B209'] + df['B219'] + df['B229'] + df['B239'] + df['B249'] + df['B259'] + df['B269']) / \
             (df['B19'] + df['B109'] + df['B119'] + df['B129'] + df['B139'] + df['B149'] + df['B159'] + df['B169'] + df['B179'])

# Sonucu yeni bir Excel dosyasına kaydet
df.to_excel('Kategori5_1sonuc.xlsx', index=False)

print("Yeni sütunlar başarıyla oluşturuldu ve sonuc.xlsx dosyasına kaydedildi.")



# import pandas as pd

# # Excel dosyasını oku
# try:
#     df = pd.read_excel('Kategori4_1sonuc.xlsx')
# except FileNotFoundError:
#     print("Dosya bulunamadı. Lütfen dosya adını ve konumunu kontrol edin.")
#     exit()

# # Yeni sütunlar oluşturma fonksiyonu
# def yeni_sutun_olustur(df, yeni_sutun_adi, bolunen_sutun, bolen_sutun):
#     with pd.option_context('mode.use_inf_as_na', True):  # sonsuz değerleri NaN olarak kabul et
#         df[yeni_sutun_adi] = df[bolunen_sutun] / df[bolen_sutun]
#         df[yeni_sutun_adi].fillna(0, inplace=True)  # NaN değerleri 0 olarak değiştir
#     return df

# # Belirtilen şartlara göre sütunları oluşturma
# sartlar = {
#     'B361': ('B182', 'B92'),
#     'B362': ('B192', 'B102'),
#     'B363': ('B202', 'B112'),
#     'B364': ('B212', 'B122'),
#     'B365': ('B222', 'B132'),
#     'B366': ('B232', 'B142'),
#     'B367': ('B242', 'B152'),
#     'B368': ('B252', 'B162'),
#     'B369': ('B262', 'B172'),
#     'B371': ('B184', 'B94'),
#     'B372': ('B194', 'B104'),
#     'B373': ('B204', 'B114'),
#     'B374': ('B214', 'B124'),
#     'B375': ('B224', 'B134'),
#     'B376': ('B234', 'B144'),
#     'B377': ('B244', 'B154'),
#     'B378': ('B254', 'B164'),
#     'B379': ('B264', 'B174'),
#     'B381': ('B185', 'B95'),
#     'B382': ('B195', 'B105'),
#     'B383': ('B205', 'B115'),
#     'B384': ('B215', 'B125'),
#     'B385': ('B225', 'B135'),
#     'B386': ('B235', 'B145'),
#     'B387': ('B245', 'B155'),
#     'B388': ('B255', 'B165'),
#     'B389': ('B265', 'B175'),
#     'B391': ('B189', 'B19'),
#     'B392': ('B199', 'B109'),
#     'B393': ('B209', 'B119'),
#     'B394': ('B219', 'B129'),
#     'B395': ('B229', 'B139'),
#     'B396': ('B239', 'B149'),
#     'B397': ('B249', 'B159'),
#     'B398': ('B259', 'B169'),
#     'B399': ('B269', 'B179')
# }

# # Yeni sütunları oluştur
# for yeni_sutun, (bolunen_sutun, bolen_sutun) in sartlar.items():
#     try:
#         df = yeni_sutun_olustur(df, yeni_sutun, bolunen_sutun, bolen_sutun)
#     except KeyError:
#         print(f"Hata: {bolunen_sutun} veya {bolen_sutun} sütunları mevcut değil.")

# # Özel hesaplamalar
# try:
#     df['B370'] = (df['B182'] + df['B192'] + df['B202'] + df['B212'] + df['B222'] + df['B232'] + df['B242'] + df['B252'] + df['B262']) / \
#                  (df['B92'] + df['B102'] + df['B112'] + df['B122'] + df['B132'] + df['B142'] + df['B152'] + df['B162'] + df['B172'])
    
#     df['B380'] = (df['B184'] + df['B194'] + df['B204'] + df['B214'] + df['B224'] + df['B234'] + df['B244'] + df['B254'] + df['B264']) / \
#                  (df['B94'] + df['B104'] + df['B114'] + df['B124'] + df['B134'] + df['B144'] + df['B154'] + df['B164'] + df['B174'])

#     df['B390'] = (df['B185'] + df['B195'] + df['B205'] + df['B215'] + df['B225'] + df['B235'] + df['B245'] + df['B255'] + df['B265']) / \
#                  (df['B95'] + df['B105'] + df['B115'] + df['B125'] + df['B135'] + df['B145'] + df['B155'] + df['B165'] + df['B175'])

#     df['B400'] = (df['B189'] + df['B199'] + df['B209'] + df['B219'] + df['B229'] + df['B239'] + df['B249'] + df['B259'] + df['B269']) / \
#                  (df['B19'] + df['B109'] + df['B119'] + df['B129'] + df['B139'] + df['B149'] + df['B159'] + df['B169'] + df['B179'])
# except KeyError as e:
#     print(f"Hata: {e} sütunu mevcut değil veya veri eksik.")

# # Dosyayı kaydetme
# try:
#     df.to_excel('Kategori5_1sonuc.xlsx', index=False, engine='openpyxl')
#     print("Yeni sütunlar başarıyla oluşturuldu ve Kategori5_1sonuc.xlsx dosyasına kaydedildi.")
# except Exception as e:
#     print(f"Dosya kaydedilirken bir hata oluştu: {e}")
