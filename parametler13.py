
import pandas as pd
from tqdm import tqdm

# Excel dosyasını oku
df = pd.read_excel('Kategori8_1sonuc.xlsx')

# Kategori 8 Modül 64 sütunlarını hesapla
sartlar_kategori_8_modul_64 = {
    'B651': ('B184', 'B4', 'B94'),
    'B652': ('B194', 'B14', 'B104'),
    'B653': ('B204', 'B24', 'B114'),
    'B654': ('B214', 'B34', 'B124'),
    'B655': ('B224', 'B44', 'B134'),
    'B656': ('B234', 'B54', 'B144'),
    'B657': ('B244', 'B64', 'B154'),
    'B658': ('B254', 'B74', 'B164'),
    'B659': ('B264', 'B84', 'B174')
}

sartlar_kategori_8_modul_65 = {
    'B661': ('B185', 'B5', 'B95'),
    'B662': ('B195', 'B15', 'B105'),
    'B663': ('B205', 'B25', 'B115'),
    'B664': ('B215', 'B35', 'B125'),
    'B665': ('B225', 'B45', 'B135'),
    'B666': ('B235', 'B55', 'B145'),
    'B667': ('B245', 'B65', 'B155'),
    'B668': ('B255', 'B75', 'B165'),
    'B669': ('B265', 'B85', 'B175')
}

sartlar_kategori_8_modul_66 = {
    'B671': ('B186', 'B6', 'B96'),
    'B672': ('B196', 'B16', 'B106'),
    'B673': ('B206', 'B26', 'B116'),
    'B674': ('B216', 'B36', 'B126'),
    'B675': ('B226', 'B46', 'B136'),
    'B676': ('B236', 'B56', 'B146'),
    'B677': ('B246', 'B66', 'B156'),
    'B678': ('B256', 'B76', 'B166'),
    'B679': ('B266', 'B86', 'B176')
}

sartlar_kategori_8_modul_67 = {
    'B681': ('B187', 'B7', 'B97'),
    'B682': ('B197', 'B17', 'B107'),
    'B683': ('B207', 'B27', 'B117'),
    'B684': ('B217', 'B37', 'B127'),
    'B685': ('B227', 'B47', 'B137'),
    'B686': ('B237', 'B57', 'B147'),
    'B687': ('B247', 'B67', 'B157'),
    'B688': ('B257', 'B77', 'B167'),
    'B689': ('B267', 'B87', 'B177')
}

sartlar_kategori_8_modul_68 = {
    'B691': ('B188', 'B8', 'B98'),
    'B692': ('B198', 'B18', 'B108'),
    'B693': ('B208', 'B28', 'B118'),
    'B694': ('B218', 'B38', 'B128'),
    'B695': ('B228', 'B48', 'B138'),
    'B696': ('B238', 'B58', 'B148'),
    'B697': ('B248', 'B68', 'B158'),
    'B698': ('B258', 'B78', 'B168'),
    'B699': ('B268', 'B88', 'B178')
}

sartlar_kategori_8_modul_69 = {
    'B701': ('B189', 'B9', 'B99'),
    'B702': ('B199', 'B19', 'B109'),
    'B703': ('B209', 'B29', 'B119'),
    'B704': ('B219', 'B39', 'B129'),
    'B705': ('B229', 'B49', 'B139'),
    'B706': ('B239', 'B59', 'B149'),
    'B707': ('B249', 'B69', 'B159'),
    'B708': ('B259', 'B79', 'B169'),
    'B709': ('B269', 'B89', 'B179')
}

sartlar_kategori_8_modul_70 = {
    'B711': ('B190', 'B10', 'B100'),
    'B712': ('B200', 'B20', 'B110'),
    'B713': ('B210', 'B30', 'B120'),
    'B714': ('B220', 'B40', 'B130'),
    'B715': ('B230', 'B50', 'B140'),
    'B716': ('B240', 'B60', 'B150'),
    'B717': ('B250', 'B70', 'B160'),
    'B718': ('B260', 'B80', 'B170'),
    'B719': ('B270', 'B90', 'B180')
}

# Yeni sütunları bir veri çerçevesine ekle
new_columns = {}

# Kategori 8 Modül 64 sütunlarını hesapla
for yeni_sutun, (bolunen_sutun, takima, takimb) in tqdm(sartlar_kategori_8_modul_64.items(), desc="Kategori 8 Modül 64 sütunlarını hesaplıyor"):
    new_columns[yeni_sutun] = df[bolunen_sutun] / ((df[takima] + df[takimb]) / 2)

# Modül 64 son sütun hesaplaması
new_columns['B660'] = (new_columns['B651'] + new_columns['B652'] + new_columns['B653'] + new_columns['B654'] + 
                       new_columns['B655'] + new_columns['B656'] + new_columns['B657'] + new_columns['B658'] + 
                       new_columns['B659']) / 9

# Kategori 8 Modül 65 sütunlarını hesapla
for yeni_sutun, (bolunen_sutun, takima, takimb) in tqdm(sartlar_kategori_8_modul_65.items(), desc="Kategori 8 Modül 65 sütunlarını hesaplıyor"):
    new_columns[yeni_sutun] = df[bolunen_sutun] / ((df[takima] + df[takimb]) / 2)

# Modül 65 son sütun hesaplaması
new_columns['B670'] = (new_columns['B661'] + new_columns['B662'] + new_columns['B663'] + new_columns['B664'] + 
                       new_columns['B665'] + new_columns['B666'] + new_columns['B667'] + new_columns['B668'] + 
                       new_columns['B669']) / 9

# Kategori 8 Modül 66 sütunlarını hesapla
for yeni_sutun, (bolunen_sutun, takima, takimb) in tqdm(sartlar_kategori_8_modul_66.items(), desc="Kategori 8 Modül 66 sütunlarını hesaplıyor"):
    new_columns[yeni_sutun] = df[bolunen_sutun] / ((df[takima] + df[takimb]) / 2)

# Modül 66 son sütun hesaplaması
new_columns['B680'] = (new_columns['B671'] + new_columns['B672'] + new_columns['B673'] + new_columns['B674'] + 
                       new_columns['B675'] + new_columns['B676'] + new_columns['B677'] + new_columns['B678'] + 
                       new_columns['B679']) / 9

# Kategori 8 Modül 67 sütunlarını hesapla
for yeni_sutun, (bolunen_sutun, takima, takimb) in tqdm(sartlar_kategori_8_modul_67.items(), desc="Kategori 8 Modül 67 sütunlarını hesaplıyor"):
    new_columns[yeni_sutun] = df[bolunen_sutun] / ((df[takima] + df[takimb]) / 2)

# Modül 67 son sütun hesaplaması
new_columns['B690'] = (new_columns['B681'] + new_columns['B682'] + new_columns['B683'] + new_columns['B684'] + 
                       new_columns['B685'] + new_columns['B686'] + new_columns['B687'] + new_columns['B688'] + 
                       new_columns['B689']) / 9

# Kategori 8 Modül 68 sütunlarını hesapla
for yeni_sutun, (bolunen_sutun, takima, takimb) in tqdm(sartlar_kategori_8_modul_68.items(), desc="Kategori 8 Modül 68 sütunlarını hesaplıyor"):
    new_columns[yeni_sutun] = df[bolunen_sutun] / ((df[takima] + df[takimb]) / 2)

# Modül 68 son sütun hesaplaması
new_columns['B700'] = (new_columns['B691'] + new_columns['B692'] + new_columns['B693'] + new_columns['B694'] + 
                       new_columns['B695'] + new_columns['B696'] + new_columns['B697'] + new_columns['B698'] + 
                       new_columns['B699']) / 9

# Kategori 8 Modül 69 sütunlarını hesapla
for yeni_sutun, (bolunen_sutun, takima, takimb) in tqdm(sartlar_kategori_8_modul_69.items(), desc="Kategori 8 Modül 69 sütunlarını hesaplıyor"):
    new_columns[yeni_sutun] = df[bolunen_sutun] / ((df[takima] + df[takimb]) / 2)

# Modül 69 son sütun hesaplaması
new_columns['B710'] = (new_columns['B701'] + new_columns['B702'] + new_columns['B703'] + new_columns['B704'] + 
                       new_columns['B705'] + new_columns['B706'] + new_columns['B707'] + new_columns['B708'] + 
                       new_columns['B709']) / 9

# Kategori 8 Modül 70 sütunlarını hesapla
for yeni_sutun, (bolunen_sutun, takima, takimb) in tqdm(sartlar_kategori_8_modul_70.items(), desc="Kategori 8 Modül 70 sütunlarını hesaplıyor"):
    new_columns[yeni_sutun] = df[bolunen_sutun] / ((df[takima] + df[takimb]) / 2)

# Modül 70 son sütun hesaplaması
new_columns['B720'] = (new_columns['B711'] + new_columns['B712'] + new_columns['B713'] + new_columns['B714'] + 
                       new_columns['B715'] + new_columns['B716'] + new_columns['B717'] + new_columns['B718'] + 
                       new_columns['B719']) / 9

# Kategori 9 için sütunlar
sartlar_kategori_9 = {
    'B721': ('B271', 'B361'),
    'B722': ('B272', 'B362'),
    'B723': ('B273', 'B363'),
    'B724': ('B274', 'B364'),
    'B725': ('B275', 'B365'),
    'B726': ('B276', 'B366'),
    'B727': ('B277', 'B367'),
    'B728': ('B278', 'B368'),
    'B729': ('B279', 'B369'),
    'B730': ('B280', 'B370'),
    'B731': ('B281', 'B371'),
    'B732': ('B282', 'B372'),
    'B733': ('B283', 'B373'),
    'B734': ('B284', 'B374'),
    'B735': ('B285', 'B375'),
    'B736': ('B286', 'B376'),
    'B737': ('B287', 'B377'),
    'B738': ('B288', 'B378'),
    'B739': ('B289', 'B379'),
    'B740': ('B290', 'B380'),
    'B741': ('B291', 'B381'),
    'B742': ('B292', 'B382'),
    'B743': ('B293', 'B383'),
    'B744': ('B294', 'B384'),
    'B745': ('B295', 'B385'),
    'B746': ('B296', 'B386'),
    'B747': ('B297', 'B387'),
    'B748': ('B298', 'B388'),
    'B749': ('B299', 'B389'),
    'B750': ('B300', 'B390'),
    'B751': ('B301', 'B391'),
    'B752': ('B302', 'B392'),
    'B753': ('B303', 'B393'),
    'B754': ('B304', 'B394'),
    'B755': ('B305', 'B395'),
    'B756': ('B306', 'B396'),
    'B757': ('B307', 'B397'),
    'B758': ('B308', 'B398'),
    'B759': ('B309', 'B399'),
    'B760': ('B310', 'B400'),
    'B761': ('B311', 'B401'),
    'B762': ('B312', 'B402'),
    'B763': ('B313', 'B403'),
    'B764': ('B314', 'B404'),
    'B765': ('B315', 'B405'),
    'B766': ('B316', 'B406'),
    'B767': ('B317', 'B407'),
    'B768': ('B318', 'B408'),
    'B769': ('B319', 'B409'),
    'B770': ('B320', 'B410'),
    'B771': ('B321', 'B411'),
    'B772': ('B322', 'B412'),
    'B773': ('B323', 'B413'),
    'B774': ('B324', 'B414'),
    'B775': ('B325', 'B415'),
    'B776': ('B326', 'B416'),
    'B777': ('B327', 'B417'),
    'B778': ('B328', 'B418'),
    'B779': ('B329', 'B419'),
    'B780': ('B330', 'B420'),
    'B781': ('B331', 'B421'),
    'B782': ('B332', 'B422'),
    'B783': ('B333', 'B423'),
    'B784': ('B334', 'B424'),
    'B785': ('B335', 'B425'),
    'B786': ('B336', 'B426'),
    'B787': ('B337', 'B427'),
    'B788': ('B338', 'B428'),
    'B789': ('B339', 'B429'),
    'B790': ('B340', 'B430'),
    'B791': ('B341', 'B431'),
    'B792': ('B342', 'B432'),
    'B793': ('B343', 'B433'),
    'B794': ('B344', 'B434'),
    'B795': ('B345', 'B435'),
    'B796': ('B346', 'B436'),
    'B797': ('B347', 'B437'),
    'B798': ('B348', 'B438'),
    'B799': ('B349', 'B439'),
    'B800': ('B350', 'B440'),
    'B801': ('B351', 'B441'),
    'B802': ('B352', 'B442'),
    'B803': ('B353', 'B443'),
    'B804': ('B354', 'B444'),
    'B805': ('B355', 'B445'),
    'B806': ('B356', 'B446'),
    'B807': ('B357', 'B447'),
    'B808': ('B358', 'B448'),
    'B809': ('B359', 'B449'),
    'B810': ('B360', 'B450')
}

# Kategori 9 sütunlarını hesapla
for yeni_sutun, (bolunen_sutun, bolen_sutun) in tqdm(sartlar_kategori_9.items(), desc="Kategori 9 sütunlarını hesaplıyor"):
    new_columns[yeni_sutun] = df[bolunen_sutun] - df[bolen_sutun]

# Yeni sütunları DataFrame'e ekle
new_columns_df = pd.DataFrame(new_columns)
df = pd.concat([df, new_columns_df], axis=1)

# Sonucu yeni bir Excel dosyasına kaydet
with pd.ExcelWriter('son_kategori8_9.xlsx', engine='xlsxwriter') as writer:
    writer.book.use_zip64()
    df.to_excel(writer, index=False)

print("Yeni sütunlar başarıyla oluşturuldu ve sonuc_kategori8_9.xlsx dosyasına kaydedildi.")


