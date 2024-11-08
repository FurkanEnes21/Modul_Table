
import pandas as pd
from tqdm import tqdm

# Excel dosyasını oku
df = pd.read_excel('Kategori7_1sonuc.xlsx')

# Kategori 6 için sütunlar
sartlar_kategori_6 = {
    'B621': ('B351', 'B441'),
    'B622': ('B352', 'B442'),
    'B623': ('B353', 'B443'),
    'B624': ('B354', 'B444'),
    'B625': ('B355', 'B445'),
    'B626': ('B356', 'B446'),
    'B627': ('B357', 'B447'),
    'B628': ('B358', 'B448'),
    'B629': ('B359', 'B449'),
    'B630': ('B360', 'B450')
}

# Kategori 8 için sütunlar
sartlar_kategori_8_modul_64 = {
    'B631': ('B182', 'B2', 'B92'),
    'B632': ('B192', 'B12', 'B102'),
    'B633': ('B202', 'B22', 'B112'),
    'B634': ('B212', 'B32', 'B122'),
    'B635': ('B222', 'B42', 'B132'),
    'B636': ('B232', 'B52', 'B142'),
    'B637': ('B242', 'B62', 'B152'),
    'B638': ('B252', 'B72', 'B162'),
    'B639': ('B262', 'B82', 'B172')
}

sartlar_kategori_8_modul_65 = {
    'B641': ('B183', 'B3', 'B93'),
    'B642': ('B193', 'B13', 'B103'),
    'B643': ('B203', 'B23', 'B113'),
    'B644': ('B213', 'B33', 'B123'),
    'B645': ('B223', 'B43', 'B133'),
    'B646': ('B233', 'B53', 'B143'),
    'B647': ('B243', 'B63', 'B153'),
    'B648': ('B253', 'B73', 'B163'),
    'B649': ('B263', 'B83', 'B173')
}

# Yeni sütunları bir veri çerçevesine ekle
new_columns = {}

# Kategori 6 sütunlarını hesapla
for yeni_sutun, (bolunen_sutun, bolen_sutun) in tqdm(sartlar_kategori_6.items(), desc="Kategori 6 sütunlarını hesaplıyor"):
    new_columns[yeni_sutun] = df[bolunen_sutun] - df[bolen_sutun]

# Kategori 8 Modül 64 sütunlarını hesapla
for yeni_sutun, (bolunen_sutun, takima, takimb) in tqdm(sartlar_kategori_8_modul_64.items(), desc="Kategori 8 Modül 64 sütunlarını hesaplıyor"):
    new_columns[yeni_sutun] = df[bolunen_sutun] / ((df[takima] + df[takimb]) / 2)

# Modül 64 son sütun hesaplaması
new_columns['B640'] = (new_columns['B631'] + new_columns['B632'] + new_columns['B633'] + new_columns['B634'] + new_columns['B634'] +
                       new_columns['B635'] + new_columns['B636'] + new_columns['B637'] + new_columns['B638'] + 
                       new_columns['B639']) / 9

# Kategori 8 Modül 65 sütunlarını hesapla
for yeni_sutun, (bolunen_sutun, takima, takimb) in tqdm(sartlar_kategori_8_modul_65.items(), desc="Kategori 8 Modül 65 sütunlarını hesaplıyor"):
    new_columns[yeni_sutun] = df[bolunen_sutun] / ((df[takima] + df[takimb]) / 2)

# Modül 65 son sütun hesaplaması
new_columns['B650'] = (new_columns['B641'] + new_columns['B642'] + new_columns['B643'] + new_columns['B644'] + new_columns['B644']+
                       new_columns['B645'] + new_columns['B646'] + new_columns['B647'] + new_columns['B648'] + 
                       new_columns['B649']) / 9

# Yeni sütunları DataFrame'e ekle
new_columns_df = pd.DataFrame(new_columns)
df = pd.concat([df, new_columns_df], axis=1)

# Sonucu yeni bir Excel dosyasına kaydet
with pd.ExcelWriter('Kategori8_1sonuc.xlsx', engine='xlsxwriter') as writer:
    writer.book.use_zip64()
    df.to_excel(writer, index=False)

print("Yeni sütunlar başarıyla oluşturuldu ve sonuc.xlsx dosyasına kaydedildi.")
