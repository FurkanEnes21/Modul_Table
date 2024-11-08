####  Bu Sayfadaki tüm kodları sırayla kullanıyoruz . 


# import pandas as pd

# # Excel dosyasını oku
# df = pd.read_excel('Modul_Table_New.xlsx')

# # Yeni sütunlar oluşturma fonksiyonu
# def yeni_sutun_olustur(df, yeni_sutun_adi, bolunen_sutun, bolen_sutun):
#     df[yeni_sutun_adi] = df[bolunen_sutun] / df[bolen_sutun]
#     return df

# # B271'den B280'e kadar yeni sütunlar oluşturma şartları
# sartlar = {
#     'B271': ('B182', 'B2'),
#     'B272': ('B192', 'B12'),
#     'B273': ('B202', 'B22'),
#     'B274': ('B212', 'B32'),
#     'B275': ('B222', 'B42'),
#     'B276': ('B232', 'B52'),
#     'B277': ('B242', 'B62'),
#     'B278': ('B252', 'B72'),
#     'B279': ('B262', 'B82')
# }

# # Belirtilen şartlara göre sütunları oluştur
# for yeni_sutun, (bolunen_sutun, bolen_sutun) in sartlar.items():
#     df = yeni_sutun_olustur(df, yeni_sutun, bolunen_sutun, bolen_sutun)

# # B280 sütununu özel hesaplamaya göre oluştur
# df['B280'] = (df['B182'] + df['B192'] + df['B202'] + df['B212'] + df['B222'] + df['B232'] + df['B242'] + df['B252'] + df['B262']) / \
#              (df['B2'] + df['B12'] + df['B22'] + df['B32'] + df['B42'] + df['B52'] + df['B62'] + df['B72'] + df['B82'])

# # Sonucu yeni bir Excel dosyasına kaydet
# df.to_excel('sonuc.xlsx', index=False)

# print("Yeni sütunlar başarıyla oluşturuldu ve sonuc.xlsx dosyasına kaydedildi.")




import pandas as pd
import numpy as np

# Excel dosyasını oku
df = pd.read_excel('sonuc.xlsx')

# Boş (NaN) ve inf değerlerini 0 ile değiştir
df = df.replace([np.inf, -np.inf], np.nan)  # Sonsuz (inf) değerleri önce NaN yap
df = df.fillna(0)  # Tüm NaN değerlerini 0 ile doldur

# Sonucu yeni bir Excel dosyasına kaydet
df.to_excel('sonuc.xlsx', index=False)

print("Boşluklar ve inf değerler başarıyla 0 ile değiştirildi ve sonuc_duzeltilmis.xlsx dosyasına kaydedildi.")



















# import pandas as pd

# # Excel dosyasını oku
# df = pd.read_excel('sonuc.xlsx')

# # Yeni sütunlar oluşturma fonksiyonu
# def yeni_sutun_olustur(df, yeni_sutun_adi, bolunen_sutun, bolen_sutun):
#     df[yeni_sutun_adi] = df[bolunen_sutun] / df[bolen_sutun]
#     return df

# # Belirtilen şartlara göre sütunları oluşturma
# sartlar = {
#     'B281': ('B184', 'B4'),
#     'B282': ('B194', 'B14'),
#     'B283': ('B204', 'B24'),
#     'B284': ('B214', 'B34'),
#     'B285': ('B224', 'B44'),
#     'B286': ('B234', 'B54'),
#     'B287': ('B244', 'B64'),
#     'B288': ('B254', 'B74'),
#     'B289': ('B264', 'B84'),
#     'B291': ('B185', 'B5'),
#     'B292': ('B195', 'B15'),
#     'B293': ('B205', 'B25'),
#     'B294': ('B215', 'B35'),
#     'B295': ('B225', 'B45'),
#     'B296': ('B235', 'B55'),
#     'B297': ('B245', 'B65'),
#     'B298': ('B255', 'B75'),
#     'B299': ('B265', 'B85'),
#     'B301': ('B189', 'B9'),
#     'B302': ('B199', 'B19'),
#     'B303': ('B209', 'B29'),
#     'B304': ('B219', 'B39'),
#     'B305': ('B229', 'B49'),
#     'B306': ('B239', 'B59'),
#     'B307': ('B249', 'B69'),
#     'B308': ('B259', 'B79'),
#     'B309': ('B269', 'B89'),
#     'B311': ('B190', 'B10'),
#     'B312': ('B200', 'B20'),
#     'B313': ('B210', 'B30'),
#     'B314': ('B220', 'B40'),
#     'B315': ('B230', 'B50'),
#     'B316': ('B240', 'B60'),
#     'B317': ('B250', 'B70'),
#     'B318': ('B260', 'B80'),
#     'B319': ('B270', 'B90'),
#     'B321': ('B183', 'B2'),
#     'B322': ('B193', 'B12'),
#     'B323': ('B203', 'B22'),
#     'B324': ('B213', 'B32'),
#     'B325': ('B223', 'B42'),
#     'B326': ('B233', 'B52'),
#     'B327': ('B243', 'B62'),
#     'B328': ('B253', 'B72'),
#     'B329': ('B263', 'B82'),
#     'B331': ('B186', 'B4'),
#     'B332': ('B196', 'B14'),
#     'B333': ('B206', 'B24'),
#     'B334': ('B216', 'B34'),
#     'B335': ('B226', 'B44'),
#     'B336': ('B236', 'B54'),
#     'B337': ('B246', 'B64'),
#     'B338': ('B256', 'B74'),
#     'B339': ('B266', 'B84'),
#     'B341': ('B187', 'B6'),
#     'B342': ('B197', 'B16'),
#     'B343': ('B207', 'B26'),
#     'B344': ('B217', 'B36'),
#     'B345': ('B227', 'B46'),
#     'B346': ('B237', 'B56'),
#     'B347': ('B247', 'B66'),
#     'B348': ('B257', 'B76'),
#     'B349': ('B267', 'B86'),
#     'B351': ('B188', '(B4-B6)'),
#     'B352': ('B198', '(B14-B16)'),
#     'B353': ('B208', '(B24-B26)'),
#     'B354': ('B218', '(B34-B36)'),
#     'B355': ('B228', '(B44-B46)'),
#     'B356': ('B238', '(B54-B56)'),
#     'B357': ('B248', '(B64-B66)'),
#     'B358': ('B258', '(B74-B76)'),
#     'B359': ('B268', '(B84-B86)')
# }

# # Belirtilen şartlara göre sütunları oluştur
# for yeni_sutun, (bolunen_sutun, bolen_sutun) in sartlar.items():
#     if '(' in bolen_sutun:
#         # Parantezli işlemler için doğrudan hesaplama yap
#         if '-' in bolen_sutun:
#             # Çıkarma işlemleri için
#             bolen_sutun_adi = bolen_sutun.replace('(', '').replace(')', '').split('-')
#             df[yeni_sutun] = df[bolunen_sutun] / (df[bolen_sutun_adi[0]] - df[bolen_sutun_adi[1]])
#         else:
#             # Toplama işlemleri için
#             bolen_sutun_adi = bolen_sutun.replace('(', '').replace(')', '').split('+')
#             df[yeni_sutun] = df[bolunen_sutun] / (df[bolen_sutun_adi[0]] + df[bolen_sutun_adi[1]])
#     else:
#         df = yeni_sutun_olustur(df, yeni_sutun, bolunen_sutun, bolen_sutun)


# # B290 sütununu özel hesaplamaya göre oluştur
# df['B290'] = (df['B184'] + df['B194'] + df['B204'] + df['B214'] + df['B224'] + df['B234'] + df['B244'] + df['B254'] + df['B264']) / \
#              (df['B4'] + df['B14'] + df['B24'] + df['B34'] + df['B44'] + df['B54'] + df['B64'] + df['B74'] + df['B84'])

# # B300 sütununu özel hesaplamaya göre oluştur
# df['B300'] = (df['B185'] + df['B195'] + df['B205'] + df['B215'] + df['B225'] + df['B235'] + df['B245'] + df['B255'] + df['B265']) / \
#              (df['B5'] + df['B15'] + df['B25'] + df['B35'] + df['B45'] + df['B55'] + df['B65'] + df['B75'] + df['B85'])

# # B310 sütununu özel hesaplamaya göre oluştur
# df['B310'] = (df['B189'] + df['B199'] + df['B209'] + df['B219'] + df['B229'] + df['B239'] + df['B249'] + df['B259'] + df['B269']) / \
#              (df['B9'] + df['B19'] + df['B29'] + df['B39'] + df['B49'] + df['B59'] + df['B69'] + df['B79'] + df['B89'])

# # B320 sütununu özel hesaplamaya göre oluştur
# df['B320'] = (df['B200'] + df['B210'] + df['B220'] + df['B230'] + df['B240'] + df['B250'] + df['B260'] + df['B270']) / \
#              (df['B10'] + df['B20'] + df['B30'] + df['B40'] + df['B50'] + df['B60'] + df['B70'] + df['B80'] + df['B90'])

# # B330 sütununu özel hesaplamaya göre oluştur
# df['B330'] = (df['B183'] + df['B193'] + df['B203'] + df['B213'] + df['B223'] + df['B233'] + df['B243'] + df['B253'] + df['B263']) / \
#              (df['B2'] + df['B12'] + df['B22'] + df['B32'] + df['B42'] + df['B52'] + df['B62'] + df['B72'] + df['B82'])

# # B340 sütununu özel hesaplamaya göre oluştur
# df['B340'] = (df['B186'] + df['B196'] + df['B206'] + df['B216'] + df['B226'] + df['B236'] + df['B246'] + df['B256'] + df['B266']) / \
#              (df['B4'] + df['B14'] + df['B24'] + df['B34'] + df['B44'] + df['B54'] + df['B64'] + df['B74'] + df['B84'])

# # B350 sütununu özel hesaplamaya göre oluştur
# df['B350'] = (df['B187'] + df['B197'] + df['B207'] + df['B217'] + df['B227'] + df['B237'] + df['B247'] + df['B257'] + df['B267']) / \
#              (df['B6'] + df['B16'] + df['B26'] + df['B36'] + df['B46'] + df['B56'] + df['B66'] + df['B76'] + df['B86'])

# # B360 sütununu özel hesaplamaya göre oluştur
# df['B360'] = (df['B188'] + df['B198'] + df['B208'] + df['B218'] + df['B228'] + df['B238'] + df['B248'] + df['B258'] + df['B268']) / \
#              ((df['B4']-df['B6']) + (df['B14']-df['B16']) + (df['B24']-df['B26']) + (df['B34']-df['B36']) + (df['B44']-df['B46']) + (df['B54']-df['B56']) + (df['B64']-df['B66']) + (df['B74']-df['B76']) + (df['B84']-df['B86']))

# # Sonucu yeni bir Excel dosyasına kaydet
# df.to_excel('Kategori4_1sonuc.xlsx', index=False)

# print("Yeni sütunlar başarıyla oluşturuldu ve sonuc.xlsx dosyasına kaydedildi.")













# import pandas as pd

# # Excel dosyasını oku
# df = pd.read_excel('Kategori4_1sonuc.xlsx')

# # Yeni sütunlar oluşturma fonksiyonu
# def yeni_sutun_olustur(df, yeni_sutun_adi, bolunen_sutun, bolen_sutun):
#     with pd.option_context('mode.use_inf_as_na', True):
#         df[yeni_sutun_adi] = df[bolunen_sutun] / df[bolen_sutun]
#         df[yeni_sutun_adi].fillna(0, inplace=True)  # 0/0 durumunda 0 olarak kabul et
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

# # Belirtilen şartlara göre sütunları oluştur
# for yeni_sutun, (bolunen_sutun, bolen_sutun) in sartlar.items():
#     if '-' in bolen_sutun:
#         bolen_sutun_adi = bolen_sutun.split('-')
#         df[yeni_sutun] = df[bolunen_sutun] / (df[bolen_sutun_adi[0]] - df[bolen_sutun_adi[1]])
#     else:
#         df = yeni_sutun_olustur(df, yeni_sutun, bolunen_sutun, bolen_sutun)

# # Özel hesaplamalar
# df['B370'] = (df['B182'] + df['B192'] + df['B202'] + df['B212'] + df['B222'] + df['B232'] + df['B242'] + df['B252'] + df['B262']) / \
#              (df['B92'] + df['B102'] + df['B112'] + df['B122'] + df['B132'] + df['B142'] + df['B152'] + df['B162'] + df['B172'])

# df['B380'] = (df['B184'] + df['B194'] + df['B204'] + df['B214'] + df['B224'] + df['B234'] + df['B244'] + df['B254'] + df['B264']) / \
#              (df['B94'] + df['B104'] + df['B114'] + df['B124'] + df['B134'] + df['B144'] + df['B154'] + df['B164'] + df['B174'])

# df['B390'] = (df['B185'] + df['B195'] + df['B205'] + df['B215'] + df['B225'] + df['B235'] + df['B245'] + df['B255'] + df['B265']) / \
#              (df['B95'] + df['B105'] + df['B115'] + df['B125'] + df['B135'] + df['B145'] + df['B155'] + df['B165'] + df['B175'])

# df['B400'] = (df['B189'] + df['B199'] + df['B209'] + df['B219'] + df['B229'] + df['B239'] + df['B249'] + df['B259'] + df['B269']) / \
#              (df['B19'] + df['B109'] + df['B119'] + df['B129'] + df['B139'] + df['B149'] + df['B159'] + df['B169'] + df['B179'])

# # Sonucu yeni bir Excel dosyasına kaydet
# df.to_excel('Kategori5_1sonuc.xlsx', index=False)

# print("Yeni sütunlar başarıyla oluşturuldu ve sonuc.xlsx dosyasına kaydedildi.")











# import pandas as pd
# from tqdm import tqdm

# # Excel dosyasını oku
# df = pd.read_excel('Kategori5_1sonuc.xlsx')

# # Yeni sütunlar oluşturma fonksiyonu
# def yeni_sutun_olustur(df, yeni_sutun_adi, bolunen_sutun, bolen_sutun):
#     with pd.option_context('mode.use_inf_as_na', True):
#         df[yeni_sutun_adi] = df[bolunen_sutun] / df[bolen_sutun]
#         df[yeni_sutun_adi].fillna(0, inplace=True)  # 0/0 durumunda 0 olarak kabul et
#     return df

# # Belirtilen şartlara göre sütunları oluşturma
# sartlar = {
#     'B401': ('B190', 'B100'),
#     'B402': ('B200', 'B110'),
#     'B403': ('B210', 'B120'),
#     'B404': ('B220', 'B130'),
#     'B405': ('B230', 'B140'),
#     'B406': ('B240', 'B150'),
#     'B407': ('B250', 'B160'),
#     'B408': ('B260', 'B170'),
#     'B409': ('B270', 'B180'),
#     'B411': ('B183', 'B92'),
#     'B412': ('B193', 'B102'),
#     'B413': ('B203', 'B112'),
#     'B414': ('B213', 'B122'),
#     'B415': ('B223', 'B132'),
#     'B416': ('B233', 'B142'),
#     'B417': ('B243', 'B152'),
#     'B418': ('B253', 'B162'),
#     'B419': ('B263', 'B172'),
#     'B421': ('B186', 'B94'),
#     'B422': ('B196', 'B104'),
#     'B423': ('B206', 'B114'),
#     'B424': ('B216', 'B124'),
#     'B425': ('B226', 'B134'),
#     'B426': ('B236', 'B144'),
#     'B427': ('B246', 'B154'),
#     'B428': ('B256', 'B164'),
#     'B429': ('B266', 'B174'),
#     'B431': ('B187', 'B96'),
#     'B432': ('B197', 'B106'),
#     'B433': ('B207', 'B116'),
#     'B434': ('B217', 'B126'),
#     'B435': ('B227', 'B136'),
#     'B436': ('B237', 'B146'),
#     'B437': ('B247', 'B156'),
#     'B438': ('B257', 'B166'),
#     'B439': ('B267', 'B176'),
#     'B441': ('B188', 'B94-B96'),
#     'B442': ('B198', 'B104-B106'),
#     'B443': ('B208', 'B114-B116'),
#     'B444': ('B218', 'B124-B126'),
#     'B445': ('B228', 'B134-B136'),
#     'B446': ('B238', 'B144-B146'),
#     'B447': ('B248', 'B154-B156'),
#     'B448': ('B258', 'B164-B166'),
#     'B449': ('B268', 'B174-B176'),
#     'B451': ('B2', 'B92'),
#     'B452': ('B12', 'B102'),
#     'B453': ('B22', 'B112'),
#     'B454': ('B32', 'B122'),
#     'B455': ('B42', 'B132'),
#     'B456': ('B52', 'B142'),
#     'B457': ('B62', 'B152'),
#     'B458': ('B72', 'B162'),
#     'B459': ('B82', 'B172'),
#     'B461': ('B3', 'B93'),
#     'B462': ('B13', 'B103'),
#     'B463': ('B23', 'B113'),
#     'B464': ('B33', 'B123'),
#     'B465': ('B43', 'B133'),
#     'B466': ('B53', 'B143'),
#     'B467': ('B63', 'B153'),
#     'B468': ('B73', 'B163'),
#     'B469': ('B83', 'B173'),
#     'B471': ('B4', 'B94'),
#     'B472': ('B14', 'B104'),
#     'B473': ('B24', 'B114'),
#     'B474': ('B34', 'B124'),
#     'B475': ('B44', 'B134'),
#     'B476': ('B54', 'B144'),
#     'B477': ('B64', 'B154'),
#     'B478': ('B74', 'B164'),
#     'B479': ('B84', 'B174'),
#     'B481': ('B5', 'B95'),
#     'B482': ('B15', 'B105'),
#     'B483': ('B25', 'B115'),
#     'B484': ('B35', 'B125'),
#     'B485': ('B45', 'B135'),
#     'B486': ('B55', 'B145'),
#     'B487': ('B65', 'B155'),
#     'B488': ('B75', 'B165'),
#     'B489': ('B85', 'B175'),
#     'B491': ('B6', 'B96'),
#     'B492': ('B16', 'B106'),
#     'B493': ('B26', 'B116'),
#     'B494': ('B36', 'B126'),
#     'B495': ('B46', 'B136'),
#     'B496': ('B56', 'B146'),
#     'B497': ('B66', 'B156'),
#     'B498': ('B76', 'B166'),
#     'B499': ('B86', 'B176'),
#     'B501': ('B7', 'B97'),
#     'B502': ('B17', 'B107'),
#     'B503': ('B27', 'B117'),
#     'B504': ('B37', 'B127'),
#     'B505': ('B47', 'B137'),
#     'B506': ('B57', 'B147'),
#     'B507': ('B67', 'B157'),
#     'B508': ('B77', 'B167'),
#     'B509': ('B87', 'B177'),
#     'B511': ('B8', 'B98'),
#     'B512': ('B18', 'B108'),
#     'B513': ('B28', 'B118'),
#     'B514': ('B38', 'B128'),
#     'B515': ('B48', 'B138'),
#     'B516': ('B58', 'B148'),
#     'B517': ('B68', 'B158'),
#     'B518': ('B78', 'B168'),
#     'B519': ('B88', 'B178'),
#     'B521': ('B9', 'B99'),
#     'B522': ('B19', 'B109'),
#     'B523': ('B29', 'B119'),
#     'B524': ('B39', 'B129'),
#     'B525': ('B49', 'B139'),
#     'B526': ('B59', 'B149'),
#     'B527': ('B69', 'B159'),
#     'B528': ('B79', 'B169'),
#     'B529': ('B89', 'B179'),
#     'B531': ('B10', 'B100'),
#     'B532': ('B20', 'B110'),
#     'B533': ('B30', 'B120'),
#     'B534': ('B40', 'B130'),
#     'B535': ('B50', 'B140'),
#     'B536': ('B60', 'B150'),
#     'B537': ('B70', 'B160'),
#     'B538': ('B80', 'B170'),
#     'B539': ('B90', 'B180')
# }

# # Yeni sütunları bir veri çerçevesine ekle
# new_columns = {}

# for yeni_sutun, (bolunen_sutun, bolen_sutun) in tqdm(sartlar.items(), desc="Sütunları hesaplıyor"):
#     if '-' in bolen_sutun:
#         bolen_sutun_adi = bolen_sutun.split('-')
#         new_columns[yeni_sutun] = df[bolunen_sutun] / (df[bolen_sutun_adi[0]] - df[bolen_sutun_adi[1]])
#     else:
#         new_columns[yeni_sutun] = df[bolunen_sutun] / df[bolen_sutun]

# # Özel hesaplamalar
# new_columns['B410'] = (df['B200'] + df['B210'] + df['B220'] + df['B230'] + df['B240'] + df['B250'] + df['B260'] + df['B270']) / \
#                       (df['B100'] + df['B110'] + df['B120'] + df['B130'] + df['B140'] + df['B150'] + df['B160'] + df['B170'] + df['B180'])

# new_columns['B420'] = (df['B183'] + df['B193'] + df['B203'] + df['B213'] + df['B223'] + df['B233'] + df['B243'] + df['B253'] + df['B263']) / \
#                       (df['B92'] + df['B102'] + df['B112'] + df['B122'] + df['B132'] + df['B142'] + df['B152'] + df['B162'] + df['B172'])

# new_columns['B430'] = (df['B186'] + df['B196'] + df['B206'] + df['B216'] + df['B226'] + df['B236'] + df['B246'] + df['B256'] + df['B266']) / \
#                       (df['B94'] + df['B104'] + df['B114'] + df['B124'] + df['B134'] + df['B144'] + df['B154'] + df['B164'] + df['B174'])

# new_columns['B440'] = (df['B187'] + df['B197'] + df['B207'] + df['B217'] + df['B227'] + df['B237'] + df['B247'] + df['B257'] + df['B267']) / \
#                       (df['B96'] + df['B106'] + df['B116'] + df['B126'] + df['B136'] + df['B146'] + df['B156'] + df['B166'] + df['B176'])

# new_columns['B450'] = (df['B188'] + df['B198'] + df['B208'] + df['B218'] + df['B228'] + df['B238'] + df['B248'] + df['B258'] + df['B268']) / \
#                       ((df['B94']-df['B96']) + (df['B104']-df['B106']) + (df['B114']-df['B116']) + (df['B124']-df['B126']) + (df['B134']-df['B136']) + (df['B144']-df['B146']) + (df['B154']-df['B156']) + (df['B164']-df['B166']) + (df['B174']-df['B176']))

# new_columns['B460'] = (df['B2'] + df['B12'] + df['B22'] + df['B32'] + df['B42'] + df['B52'] + df['B62'] + df['B72'] + df['B82']) - \
#                       (df['B92'] + df['B102'] + df['B112'] + df['B122'] + df['B132'] + df['B142'] + df['B152'] + df['B162'] + df['B172'])

# new_columns['B470'] = (df['B3'] + df['B13'] + df['B23'] + df['B33'] + df['B43'] + df['B53'] + df['B63'] + df['B73'] + df['B83']) - \
#                       (df['B93'] + df['B103'] + df['B113'] + df['B123'] + df['B133'] + df['B143'] + df['B153'] + df['B163'] + df['B173'])

# new_columns['B480'] = (df['B4'] + df['B14'] + df['B24'] + df['B34'] + df['B44'] + df['B54'] + df['B64'] + df['B74'] + df['B84']) - \
#                       (df['B94'] + df['B104'] + df['B114'] + df['B124'] + df['B134'] + df['B144'] + df['B154'] + df['B164'] + df['B174'])

# new_columns['B490'] = (df['B5'] + df['B15'] + df['B25'] + df['B35'] + df['B45'] + df['B55'] + df['B65'] + df['B75'] + df['B85']) - \
#                       (df['B95'] + df['B105'] + df['B115'] + df['B125'] + df['B135'] + df['B145'] + df['B155'] + df['B165'] + df['B175'])

# new_columns['B500'] = (df['B6'] + df['B16'] + df['B26'] + df['B36'] + df['B46'] + df['B56'] + df['B66'] + df['B76'] + df['B86']) - \
#                       (df['B96'] + df['B106'] + df['B116'] + df['B126'] + df['B136'] + df['B146'] + df['B156'] + df['B166'] + df['B176'])

# new_columns['B510'] = (df['B7'] + df['B17'] + df['B27'] + df['B37'] + df['B47'] + df['B57'] + df['B67'] + df['B77'] + df['B87']) - \
#                       (df['B97'] + df['B107'] + df['B117'] + df['B127'] + df['B137'] + df['B147'] + df['B157'] + df['B167'] + df['B177'])

# new_columns['B520'] = (df['B8'] + df['B18'] + df['B28'] + df['B38'] + df['B48'] + df['B58'] + df['B68'] + df['B78'] + df['B88']) - \
#                       (df['B98'] + df['B108'] + df['B118'] + df['B128'] + df['B138'] + df['B148'] + df['B158'] + df['B168'] + df['B178'])

# new_columns['B530'] = (df['B9'] + df['B19'] + df['B29'] + df['B39'] + df['B49'] + df['B59'] + df['B69'] + df['B79'] + df['B89']) - \
#                       (df['B99'] + df['B109'] + df['B119'] + df['B129'] + df['B139'] + df['B149'] + df['B159'] + df['B169'] + df['B179'])

# new_columns['B540'] = (df['B10'] + df['B20'] + df['B30'] + df['B40'] + df['B50'] + df['B60'] + df['B70'] + df['B80'] + df['B90']) - \
#                       (df['B100'] + df['B110'] + df['B120'] + df['B130'] + df['B140'] + df['B150'] + df['B160'] + df['B170'] + df['B180'])

# # Yeni sütunları DataFrame'e ekle
# new_columns_df = pd.DataFrame(new_columns)
# df = pd.concat([df, new_columns_df], axis=1)

# # Sonucu yeni bir Excel dosyasına kaydet
# with pd.ExcelWriter('Kategori6_1sonuc.xlsx', engine='xlsxwriter') as writer:
#     writer.book.use_zip64()
#     df.to_excel(writer, index=False)

# print("Yeni sütunlar başarıyla oluşturuldu ve sonuc.xlsx dosyasına kaydedildi.")
















# import pandas as pd
# from tqdm import tqdm

# # Excel dosyasını oku
# df = pd.read_excel('Kategori6_1sonuc.xlsx')

# # Yeni sütunlar oluşturma fonksiyonu
# def yeni_sutun_olustur(df, yeni_sutun_adi, bolunen_sutun, bolen_sutun):
#     with pd.option_context('mode.use_inf_as_na', True):
#         df[yeni_sutun_adi] = df[bolunen_sutun] - df[bolen_sutun]
#         df[yeni_sutun_adi].fillna(0, inplace=True)  # 0/0 durumunda 0 olarak kabul et
#     return df

# # Belirtilen şartlara göre sütunları oluşturma
# sartlar = {
#     'B541': ('B271', 'B361'),
#     'B542': ('B272', 'B362'),
#     'B543': ('B273', 'B363'),
#     'B544': ('B274', 'B364'),
#     'B545': ('B275', 'B365'),
#     'B546': ('B276', 'B366'),
#     'B547': ('B277', 'B367'),
#     'B548': ('B278', 'B368'),
#     'B549': ('B279', 'B369'),
#     'B550': ('B280', 'B370'),
#     'B551': ('B281', 'B371'),
#     'B552': ('B282', 'B372'),
#     'B553': ('B283', 'B373'),
#     'B554': ('B284', 'B374'),
#     'B555': ('B285', 'B375'),
#     'B556': ('B286', 'B376'),
#     'B557': ('B287', 'B377'),
#     'B558': ('B288', 'B378'),
#     'B559': ('B289', 'B379'),
#     'B560': ('B290', 'B380'),
#     'B561': ('B291', 'B381'),
#     'B562': ('B292', 'B382'),
#     'B563': ('B293', 'B383'),
#     'B564': ('B294', 'B384'),
#     'B565': ('B295', 'B385'),
#     'B566': ('B296', 'B386'),
#     'B567': ('B297', 'B387'),
#     'B568': ('B298', 'B388'),
#     'B569': ('B299', 'B389'),
#     'B570': ('B300', 'B390'),
#     'B571': ('B301', 'B391'),
#     'B572': ('B302', 'B392'),
#     'B573': ('B303', 'B393'),
#     'B574': ('B304', 'B394'),
#     'B575': ('B305', 'B395'),
#     'B576': ('B306', 'B396'),
#     'B577': ('B307', 'B397'),
#     'B578': ('B308', 'B398'),
#     'B579': ('B309', 'B399'),
#     'B580': ('B310', 'B400'),
#     'B581': ('B311', 'B401'),
#     'B582': ('B312', 'B402'),
#     'B583': ('B313', 'B403'),
#     'B584': ('B314', 'B404'),
#     'B585': ('B315', 'B405'),
#     'B586': ('B316', 'B406'),
#     'B587': ('B317', 'B407'),
#     'B588': ('B318', 'B408'),
#     'B589': ('B319', 'B409'),
#     'B590': ('B320', 'B410'),
#     'B591': ('B321', 'B411'),
#     'B592': ('B322', 'B412'),
#     'B593': ('B323', 'B413'),
#     'B594': ('B324', 'B414'),
#     'B595': ('B325', 'B415'),
#     'B596': ('B326', 'B416'),
#     'B597': ('B327', 'B417'),
#     'B598': ('B328', 'B418'),
#     'B599': ('B329', 'B419'),
#     'B600': ('B330', 'B420'),
#     'B601': ('B331', 'B421'),
#     'B602': ('B332', 'B422'),
#     'B603': ('B333', 'B423'),
#     'B604': ('B334', 'B424'),
#     'B605': ('B335', 'B425'),
#     'B606': ('B336', 'B426'),
#     'B607': ('B337', 'B427'),
#     'B608': ('B338', 'B428'),
#     'B609': ('B339', 'B429'),
#     'B610': ('B340', 'B430'),
#     'B611': ('B341', 'B431'),
#     'B612': ('B342', 'B432'),
#     'B613': ('B343', 'B433'),
#     'B614': ('B344', 'B434'),
#     'B615': ('B345', 'B435'),
#     'B616': ('B346', 'B436'),
#     'B617': ('B347', 'B437'),
#     'B618': ('B348', 'B438'),
#     'B619': ('B349', 'B439'),
#     'B620': ('B350', 'B440')
# }

# # Yeni sütunları bir veri çerçevesine ekle
# new_columns = {}

# for yeni_sutun, (bolunen_sutun, bolen_sutun) in tqdm(sartlar.items(), desc="Sütunları hesaplıyor"):
#     new_columns[yeni_sutun] = df[bolunen_sutun] - df[bolen_sutun]

# # Yeni sütunları DataFrame'e ekle
# new_columns_df = pd.DataFrame(new_columns)
# df = pd.concat([df, new_columns_df], axis=1)

# # Sonucu yeni bir Excel dosyasına kaydet
# with pd.ExcelWriter('Kategori7_1sonuc.xlsx', engine='xlsxwriter') as writer:
#     writer.book.use_zip64()
#     df.to_excel(writer, index=False)

# print("Yeni sütunlar başarıyla oluşturuldu ve sonuc.xlsx dosyasına kaydedildi.")













# import pandas as pd
# from tqdm import tqdm

# # Excel dosyasını oku
# df = pd.read_excel('Kategori7_1sonuc.xlsx')

# # Kategori 6 için sütunlar
# sartlar_kategori_6 = {
#     'B621': ('B351', 'B441'),
#     'B622': ('B352', 'B442'),
#     'B623': ('B353', 'B443'),
#     'B624': ('B354', 'B444'),
#     'B625': ('B355', 'B445'),
#     'B626': ('B356', 'B446'),
#     'B627': ('B357', 'B447'),
#     'B628': ('B358', 'B448'),
#     'B629': ('B359', 'B449'),
#     'B630': ('B360', 'B450')
# }

# # Kategori 8 için sütunlar
# sartlar_kategori_8_modul_64 = {
#     'B631': ('B182', 'B2', 'B92'),
#     'B632': ('B192', 'B12', 'B102'),
#     'B633': ('B202', 'B22', 'B112'),
#     'B634': ('B212', 'B32', 'B122'),
#     'B635': ('B222', 'B42', 'B132'),
#     'B636': ('B232', 'B52', 'B142'),
#     'B637': ('B242', 'B62', 'B152'),
#     'B638': ('B252', 'B72', 'B162'),
#     'B639': ('B262', 'B82', 'B172')
# }

# sartlar_kategori_8_modul_65 = {
#     'B641': ('B183', 'B3', 'B93'),
#     'B642': ('B193', 'B13', 'B103'),
#     'B643': ('B203', 'B23', 'B113'),
#     'B644': ('B213', 'B33', 'B123'),
#     'B645': ('B223', 'B43', 'B133'),
#     'B646': ('B233', 'B53', 'B143'),
#     'B647': ('B243', 'B63', 'B153'),
#     'B648': ('B253', 'B73', 'B163'),
#     'B649': ('B263', 'B83', 'B173')
# }

# # Yeni sütunları bir veri çerçevesine ekle
# new_columns = {}

# # Kategori 6 sütunlarını hesapla
# for yeni_sutun, (bolunen_sutun, bolen_sutun) in tqdm(sartlar_kategori_6.items(), desc="Kategori 6 sütunlarını hesaplıyor"):
#     new_columns[yeni_sutun] = df[bolunen_sutun] - df[bolen_sutun]

# # Kategori 8 Modül 64 sütunlarını hesapla
# for yeni_sutun, (bolunen_sutun, takima, takimb) in tqdm(sartlar_kategori_8_modul_64.items(), desc="Kategori 8 Modül 64 sütunlarını hesaplıyor"):
#     new_columns[yeni_sutun] = df[bolunen_sutun] / ((df[takima] + df[takimb]) / 2)

# # Modül 64 son sütun hesaplaması
# new_columns['B640'] = (new_columns['B631'] + new_columns['B632'] + new_columns['B633'] + new_columns['B634'] + new_columns['B634'] +
#                        new_columns['B635'] + new_columns['B636'] + new_columns['B637'] + new_columns['B638'] + 
#                        new_columns['B639']) / 9

# # Kategori 8 Modül 65 sütunlarını hesapla
# for yeni_sutun, (bolunen_sutun, takima, takimb) in tqdm(sartlar_kategori_8_modul_65.items(), desc="Kategori 8 Modül 65 sütunlarını hesaplıyor"):
#     new_columns[yeni_sutun] = df[bolunen_sutun] / ((df[takima] + df[takimb]) / 2)

# # Modül 65 son sütun hesaplaması
# new_columns['B650'] = (new_columns['B641'] + new_columns['B642'] + new_columns['B643'] + new_columns['B644'] + new_columns['B644']+
#                        new_columns['B645'] + new_columns['B646'] + new_columns['B647'] + new_columns['B648'] + 
#                        new_columns['B649']) / 9

# # Yeni sütunları DataFrame'e ekle
# new_columns_df = pd.DataFrame(new_columns)
# df = pd.concat([df, new_columns_df], axis=1)

# # Sonucu yeni bir Excel dosyasına kaydet
# with pd.ExcelWriter('Kategori8_1sonuc.xlsx', engine='xlsxwriter') as writer:
#     writer.book.use_zip64()
#     df.to_excel(writer, index=False)

# print("Yeni sütunlar başarıyla oluşturuldu ve sonuc.xlsx dosyasına kaydedildi.")
















# import pandas as pd
# from tqdm import tqdm

# # Excel dosyasını oku
# df = pd.read_excel('Kategori8_1sonuc.xlsx')

# # Kategori 8 Modül 64 sütunlarını hesapla
# sartlar_kategori_8_modul_64 = {
#     'B651': ('B184', 'B4', 'B94'),
#     'B652': ('B194', 'B14', 'B104'),
#     'B653': ('B204', 'B24', 'B114'),
#     'B654': ('B214', 'B34', 'B124'),
#     'B655': ('B224', 'B44', 'B134'),
#     'B656': ('B234', 'B54', 'B144'),
#     'B657': ('B244', 'B64', 'B154'),
#     'B658': ('B254', 'B74', 'B164'),
#     'B659': ('B264', 'B84', 'B174')
# }

# sartlar_kategori_8_modul_65 = {
#     'B661': ('B185', 'B5', 'B95'),
#     'B662': ('B195', 'B15', 'B105'),
#     'B663': ('B205', 'B25', 'B115'),
#     'B664': ('B215', 'B35', 'B125'),
#     'B665': ('B225', 'B45', 'B135'),
#     'B666': ('B235', 'B55', 'B145'),
#     'B667': ('B245', 'B65', 'B155'),
#     'B668': ('B255', 'B75', 'B165'),
#     'B669': ('B265', 'B85', 'B175')
# }

# sartlar_kategori_8_modul_66 = {
#     'B671': ('B186', 'B6', 'B96'),
#     'B672': ('B196', 'B16', 'B106'),
#     'B673': ('B206', 'B26', 'B116'),
#     'B674': ('B216', 'B36', 'B126'),
#     'B675': ('B226', 'B46', 'B136'),
#     'B676': ('B236', 'B56', 'B146'),
#     'B677': ('B246', 'B66', 'B156'),
#     'B678': ('B256', 'B76', 'B166'),
#     'B679': ('B266', 'B86', 'B176')
# }

# sartlar_kategori_8_modul_67 = {
#     'B681': ('B187', 'B7', 'B97'),
#     'B682': ('B197', 'B17', 'B107'),
#     'B683': ('B207', 'B27', 'B117'),
#     'B684': ('B217', 'B37', 'B127'),
#     'B685': ('B227', 'B47', 'B137'),
#     'B686': ('B237', 'B57', 'B147'),
#     'B687': ('B247', 'B67', 'B157'),
#     'B688': ('B257', 'B77', 'B167'),
#     'B689': ('B267', 'B87', 'B177')
# }

# sartlar_kategori_8_modul_68 = {
#     'B691': ('B188', 'B8', 'B98'),
#     'B692': ('B198', 'B18', 'B108'),
#     'B693': ('B208', 'B28', 'B118'),
#     'B694': ('B218', 'B38', 'B128'),
#     'B695': ('B228', 'B48', 'B138'),
#     'B696': ('B238', 'B58', 'B148'),
#     'B697': ('B248', 'B68', 'B158'),
#     'B698': ('B258', 'B78', 'B168'),
#     'B699': ('B268', 'B88', 'B178')
# }

# sartlar_kategori_8_modul_69 = {
#     'B701': ('B189', 'B9', 'B99'),
#     'B702': ('B199', 'B19', 'B109'),
#     'B703': ('B209', 'B29', 'B119'),
#     'B704': ('B219', 'B39', 'B129'),
#     'B705': ('B229', 'B49', 'B139'),
#     'B706': ('B239', 'B59', 'B149'),
#     'B707': ('B249', 'B69', 'B159'),
#     'B708': ('B259', 'B79', 'B169'),
#     'B709': ('B269', 'B89', 'B179')
# }

# sartlar_kategori_8_modul_70 = {
#     'B711': ('B190', 'B10', 'B100'),
#     'B712': ('B200', 'B20', 'B110'),
#     'B713': ('B210', 'B30', 'B120'),
#     'B714': ('B220', 'B40', 'B130'),
#     'B715': ('B230', 'B50', 'B140'),
#     'B716': ('B240', 'B60', 'B150'),
#     'B717': ('B250', 'B70', 'B160'),
#     'B718': ('B260', 'B80', 'B170'),
#     'B719': ('B270', 'B90', 'B180')
# }

# # Yeni sütunları bir veri çerçevesine ekle
# new_columns = {}

# # Kategori 8 Modül 64 sütunlarını hesapla
# for yeni_sutun, (bolunen_sutun, takima, takimb) in tqdm(sartlar_kategori_8_modul_64.items(), desc="Kategori 8 Modül 64 sütunlarını hesaplıyor"):
#     new_columns[yeni_sutun] = df[bolunen_sutun] / ((df[takima] + df[takimb]) / 2)

# # Modül 64 son sütun hesaplaması
# new_columns['B660'] = (new_columns['B651'] + new_columns['B652'] + new_columns['B653'] + new_columns['B654'] + 
#                        new_columns['B655'] + new_columns['B656'] + new_columns['B657'] + new_columns['B658'] + 
#                        new_columns['B659']) / 9

# # Kategori 8 Modül 65 sütunlarını hesapla
# for yeni_sutun, (bolunen_sutun, takima, takimb) in tqdm(sartlar_kategori_8_modul_65.items(), desc="Kategori 8 Modül 65 sütunlarını hesaplıyor"):
#     new_columns[yeni_sutun] = df[bolunen_sutun] / ((df[takima] + df[takimb]) / 2)

# # Modül 65 son sütun hesaplaması
# new_columns['B670'] = (new_columns['B661'] + new_columns['B662'] + new_columns['B663'] + new_columns['B664'] + 
#                        new_columns['B665'] + new_columns['B666'] + new_columns['B667'] + new_columns['B668'] + 
#                        new_columns['B669']) / 9

# # Kategori 8 Modül 66 sütunlarını hesapla
# for yeni_sutun, (bolunen_sutun, takima, takimb) in tqdm(sartlar_kategori_8_modul_66.items(), desc="Kategori 8 Modül 66 sütunlarını hesaplıyor"):
#     new_columns[yeni_sutun] = df[bolunen_sutun] / ((df[takima] + df[takimb]) / 2)

# # Modül 66 son sütun hesaplaması
# new_columns['B680'] = (new_columns['B671'] + new_columns['B672'] + new_columns['B673'] + new_columns['B674'] + 
#                        new_columns['B675'] + new_columns['B676'] + new_columns['B677'] + new_columns['B678'] + 
#                        new_columns['B679']) / 9

# # Kategori 8 Modül 67 sütunlarını hesapla
# for yeni_sutun, (bolunen_sutun, takima, takimb) in tqdm(sartlar_kategori_8_modul_67.items(), desc="Kategori 8 Modül 67 sütunlarını hesaplıyor"):
#     new_columns[yeni_sutun] = df[bolunen_sutun] / ((df[takima] + df[takimb]) / 2)

# # Modül 67 son sütun hesaplaması
# new_columns['B690'] = (new_columns['B681'] + new_columns['B682'] + new_columns['B683'] + new_columns['B684'] + 
#                        new_columns['B685'] + new_columns['B686'] + new_columns['B687'] + new_columns['B688'] + 
#                        new_columns['B689']) / 9

# # Kategori 8 Modül 68 sütunlarını hesapla
# for yeni_sutun, (bolunen_sutun, takima, takimb) in tqdm(sartlar_kategori_8_modul_68.items(), desc="Kategori 8 Modül 68 sütunlarını hesaplıyor"):
#     new_columns[yeni_sutun] = df[bolunen_sutun] / ((df[takima] + df[takimb]) / 2)

# # Modül 68 son sütun hesaplaması
# new_columns['B700'] = (new_columns['B691'] + new_columns['B692'] + new_columns['B693'] + new_columns['B694'] + 
#                        new_columns['B695'] + new_columns['B696'] + new_columns['B697'] + new_columns['B698'] + 
#                        new_columns['B699']) / 9

# # Kategori 8 Modül 69 sütunlarını hesapla
# for yeni_sutun, (bolunen_sutun, takima, takimb) in tqdm(sartlar_kategori_8_modul_69.items(), desc="Kategori 8 Modül 69 sütunlarını hesaplıyor"):
#     new_columns[yeni_sutun] = df[bolunen_sutun] / ((df[takima] + df[takimb]) / 2)

# # Modül 69 son sütun hesaplaması
# new_columns['B710'] = (new_columns['B701'] + new_columns['B702'] + new_columns['B703'] + new_columns['B704'] + 
#                        new_columns['B705'] + new_columns['B706'] + new_columns['B707'] + new_columns['B708'] + 
#                        new_columns['B709']) / 9

# # Kategori 8 Modül 70 sütunlarını hesapla
# for yeni_sutun, (bolunen_sutun, takima, takimb) in tqdm(sartlar_kategori_8_modul_70.items(), desc="Kategori 8 Modül 70 sütunlarını hesaplıyor"):
#     new_columns[yeni_sutun] = df[bolunen_sutun] / ((df[takima] + df[takimb]) / 2)

# # Modül 70 son sütun hesaplaması
# new_columns['B720'] = (new_columns['B711'] + new_columns['B712'] + new_columns['B713'] + new_columns['B714'] + 
#                        new_columns['B715'] + new_columns['B716'] + new_columns['B717'] + new_columns['B718'] + 
#                        new_columns['B719']) / 9

# # Kategori 9 için sütunlar
# sartlar_kategori_9 = {
#     'B721': ('B271', 'B361'),
#     'B722': ('B272', 'B362'),
#     'B723': ('B273', 'B363'),
#     'B724': ('B274', 'B364'),
#     'B725': ('B275', 'B365'),
#     'B726': ('B276', 'B366'),
#     'B727': ('B277', 'B367'),
#     'B728': ('B278', 'B368'),
#     'B729': ('B279', 'B369'),
#     'B730': ('B280', 'B370'),
#     'B731': ('B281', 'B371'),
#     'B732': ('B282', 'B372'),
#     'B733': ('B283', 'B373'),
#     'B734': ('B284', 'B374'),
#     'B735': ('B285', 'B375'),
#     'B736': ('B286', 'B376'),
#     'B737': ('B287', 'B377'),
#     'B738': ('B288', 'B378'),
#     'B739': ('B289', 'B379'),
#     'B740': ('B290', 'B380'),
#     'B741': ('B291', 'B381'),
#     'B742': ('B292', 'B382'),
#     'B743': ('B293', 'B383'),
#     'B744': ('B294', 'B384'),
#     'B745': ('B295', 'B385'),
#     'B746': ('B296', 'B386'),
#     'B747': ('B297', 'B387'),
#     'B748': ('B298', 'B388'),
#     'B749': ('B299', 'B389'),
#     'B750': ('B300', 'B390'),
#     'B751': ('B301', 'B391'),
#     'B752': ('B302', 'B392'),
#     'B753': ('B303', 'B393'),
#     'B754': ('B304', 'B394'),
#     'B755': ('B305', 'B395'),
#     'B756': ('B306', 'B396'),
#     'B757': ('B307', 'B397'),
#     'B758': ('B308', 'B398'),
#     'B759': ('B309', 'B399'),
#     'B760': ('B310', 'B400'),
#     'B761': ('B311', 'B401'),
#     'B762': ('B312', 'B402'),
#     'B763': ('B313', 'B403'),
#     'B764': ('B314', 'B404'),
#     'B765': ('B315', 'B405'),
#     'B766': ('B316', 'B406'),
#     'B767': ('B317', 'B407'),
#     'B768': ('B318', 'B408'),
#     'B769': ('B319', 'B409'),
#     'B770': ('B320', 'B410'),
#     'B771': ('B321', 'B411'),
#     'B772': ('B322', 'B412'),
#     'B773': ('B323', 'B413'),
#     'B774': ('B324', 'B414'),
#     'B775': ('B325', 'B415'),
#     'B776': ('B326', 'B416'),
#     'B777': ('B327', 'B417'),
#     'B778': ('B328', 'B418'),
#     'B779': ('B329', 'B419'),
#     'B780': ('B330', 'B420'),
#     'B781': ('B331', 'B421'),
#     'B782': ('B332', 'B422'),
#     'B783': ('B333', 'B423'),
#     'B784': ('B334', 'B424'),
#     'B785': ('B335', 'B425'),
#     'B786': ('B336', 'B426'),
#     'B787': ('B337', 'B427'),
#     'B788': ('B338', 'B428'),
#     'B789': ('B339', 'B429'),
#     'B790': ('B340', 'B430'),
#     'B791': ('B341', 'B431'),
#     'B792': ('B342', 'B432'),
#     'B793': ('B343', 'B433'),
#     'B794': ('B344', 'B434'),
#     'B795': ('B345', 'B435'),
#     'B796': ('B346', 'B436'),
#     'B797': ('B347', 'B437'),
#     'B798': ('B348', 'B438'),
#     'B799': ('B349', 'B439'),
#     'B800': ('B350', 'B440'),
#     'B801': ('B351', 'B441'),
#     'B802': ('B352', 'B442'),
#     'B803': ('B353', 'B443'),
#     'B804': ('B354', 'B444'),
#     'B805': ('B355', 'B445'),
#     'B806': ('B356', 'B446'),
#     'B807': ('B357', 'B447'),
#     'B808': ('B358', 'B448'),
#     'B809': ('B359', 'B449'),
#     'B810': ('B360', 'B450')
# }

# # Kategori 9 sütunlarını hesapla
# for yeni_sutun, (bolunen_sutun, bolen_sutun) in tqdm(sartlar_kategori_9.items(), desc="Kategori 9 sütunlarını hesaplıyor"):
#     new_columns[yeni_sutun] = df[bolunen_sutun] - df[bolen_sutun]

# # Yeni sütunları DataFrame'e ekle
# new_columns_df = pd.DataFrame(new_columns)
# df = pd.concat([df, new_columns_df], axis=1)

# # Sonucu yeni bir Excel dosyasına kaydet
# with pd.ExcelWriter('son_kategori8_9.xlsx', engine='xlsxwriter') as writer:
#     writer.book.use_zip64()
#     df.to_excel(writer, index=False)

# print("Yeni sütunlar başarıyla oluşturuldu ve sonuc_kategori8_9.xlsx dosyasına kaydedildi.")


