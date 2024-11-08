
import pandas as pd

# Excel dosyasını oku
df = pd.read_excel('sonuc.xlsx')

# Yeni sütunlar oluşturma fonksiyonu
def yeni_sutun_olustur(df, yeni_sutun_adi, bolunen_sutun, bolen_sutun):
    df[yeni_sutun_adi] = df[bolunen_sutun] / df[bolen_sutun]
    return df

# Belirtilen şartlara göre sütunları oluşturma
sartlar = {
    'B281': ('B184', 'B4'),
    'B282': ('B194', 'B14'),
    'B283': ('B204', 'B24'),
    'B284': ('B214', 'B34'),
    'B285': ('B224', 'B44'),
    'B286': ('B234', 'B54'),
    'B287': ('B244', 'B64'),
    'B288': ('B254', 'B74'),
    'B289': ('B264', 'B84'),
    'B291': ('B185', 'B5'),
    'B292': ('B195', 'B15'),
    'B293': ('B205', 'B25'),
    'B294': ('B215', 'B35'),
    'B295': ('B225', 'B45'),
    'B296': ('B235', 'B55'),
    'B297': ('B245', 'B65'),
    'B298': ('B255', 'B75'),
    'B299': ('B265', 'B85'),
    'B301': ('B189', 'B9'),
    'B302': ('B199', 'B19'),
    'B303': ('B209', 'B29'),
    'B304': ('B219', 'B39'),
    'B305': ('B229', 'B49'),
    'B306': ('B239', 'B59'),
    'B307': ('B249', 'B69'),
    'B308': ('B259', 'B79'),
    'B309': ('B269', 'B89'),
    'B311': ('B190', 'B10'),
    'B312': ('B200', 'B20'),
    'B313': ('B210', 'B30'),
    'B314': ('B220', 'B40'),
    'B315': ('B230', 'B50'),
    'B316': ('B240', 'B60'),
    'B317': ('B250', 'B70'),
    'B318': ('B260', 'B80'),
    'B319': ('B270', 'B90'),
    'B321': ('B183', 'B2'),
    'B322': ('B193', 'B12'),
    'B323': ('B203', 'B22'),
    'B324': ('B213', 'B32'),
    'B325': ('B223', 'B42'),
    'B326': ('B233', 'B52'),
    'B327': ('B243', 'B62'),
    'B328': ('B253', 'B72'),
    'B329': ('B263', 'B82'),
    'B331': ('B186', 'B4'),
    'B332': ('B196', 'B14'),
    'B333': ('B206', 'B24'),
    'B334': ('B216', 'B34'),
    'B335': ('B226', 'B44'),
    'B336': ('B236', 'B54'),
    'B337': ('B246', 'B64'),
    'B338': ('B256', 'B74'),
    'B339': ('B266', 'B84'),
    'B341': ('B187', 'B6'),
    'B342': ('B197', 'B16'),
    'B343': ('B207', 'B26'),
    'B344': ('B217', 'B36'),
    'B345': ('B227', 'B46'),
    'B346': ('B237', 'B56'),
    'B347': ('B247', 'B66'),
    'B348': ('B257', 'B76'),
    'B349': ('B267', 'B86'),
    'B351': ('B188', '(B4-B6)'),
    'B352': ('B198', '(B14-B16)'),
    'B353': ('B208', '(B24-B26)'),
    'B354': ('B218', '(B34-B36)'),
    'B355': ('B228', '(B44-B46)'),
    'B356': ('B238', '(B54-B56)'),
    'B357': ('B248', '(B64-B66)'),
    'B358': ('B258', '(B74-B76)'),
    'B359': ('B268', '(B84-B86)')
}

# Belirtilen şartlara göre sütunları oluştur
for yeni_sutun, (bolunen_sutun, bolen_sutun) in sartlar.items():
    if '(' in bolen_sutun:
        # Parantezli işlemler için doğrudan hesaplama yap
        if '-' in bolen_sutun:
            # Çıkarma işlemleri için
            bolen_sutun_adi = bolen_sutun.replace('(', '').replace(')', '').split('-')
            df[yeni_sutun] = df[bolunen_sutun] / (df[bolen_sutun_adi[0]] - df[bolen_sutun_adi[1]])
        else:
            # Toplama işlemleri için
            bolen_sutun_adi = bolen_sutun.replace('(', '').replace(')', '').split('+')
            df[yeni_sutun] = df[bolunen_sutun] / (df[bolen_sutun_adi[0]] + df[bolen_sutun_adi[1]])
    else:
        df = yeni_sutun_olustur(df, yeni_sutun, bolunen_sutun, bolen_sutun)


# B290 sütununu özel hesaplamaya göre oluştur
df['B290'] = (df['B184'] + df['B194'] + df['B204'] + df['B214'] + df['B224'] + df['B234'] + df['B244'] + df['B254'] + df['B264']) / \
             (df['B4'] + df['B14'] + df['B24'] + df['B34'] + df['B44'] + df['B54'] + df['B64'] + df['B74'] + df['B84'])

# B300 sütununu özel hesaplamaya göre oluştur
df['B300'] = (df['B185'] + df['B195'] + df['B205'] + df['B215'] + df['B225'] + df['B235'] + df['B245'] + df['B255'] + df['B265']) / \
             (df['B5'] + df['B15'] + df['B25'] + df['B35'] + df['B45'] + df['B55'] + df['B65'] + df['B75'] + df['B85'])

# B310 sütununu özel hesaplamaya göre oluştur
df['B310'] = (df['B189'] + df['B199'] + df['B209'] + df['B219'] + df['B229'] + df['B239'] + df['B249'] + df['B259'] + df['B269']) / \
             (df['B9'] + df['B19'] + df['B29'] + df['B39'] + df['B49'] + df['B59'] + df['B69'] + df['B79'] + df['B89'])

# B320 sütununu özel hesaplamaya göre oluştur
df['B320'] = (df['B200'] + df['B210'] + df['B220'] + df['B230'] + df['B240'] + df['B250'] + df['B260'] + df['B270']) / \
             (df['B10'] + df['B20'] + df['B30'] + df['B40'] + df['B50'] + df['B60'] + df['B70'] + df['B80'] + df['B90'])

# B330 sütununu özel hesaplamaya göre oluştur
df['B330'] = (df['B183'] + df['B193'] + df['B203'] + df['B213'] + df['B223'] + df['B233'] + df['B243'] + df['B253'] + df['B263']) / \
             (df['B2'] + df['B12'] + df['B22'] + df['B32'] + df['B42'] + df['B52'] + df['B62'] + df['B72'] + df['B82'])

# B340 sütununu özel hesaplamaya göre oluştur
df['B340'] = (df['B186'] + df['B196'] + df['B206'] + df['B216'] + df['B226'] + df['B236'] + df['B246'] + df['B256'] + df['B266']) / \
             (df['B4'] + df['B14'] + df['B24'] + df['B34'] + df['B44'] + df['B54'] + df['B64'] + df['B74'] + df['B84'])

# B350 sütununu özel hesaplamaya göre oluştur
df['B350'] = (df['B187'] + df['B197'] + df['B207'] + df['B217'] + df['B227'] + df['B237'] + df['B247'] + df['B257'] + df['B267']) / \
             (df['B6'] + df['B16'] + df['B26'] + df['B36'] + df['B46'] + df['B56'] + df['B66'] + df['B76'] + df['B86'])

# B360 sütununu özel hesaplamaya göre oluştur
df['B360'] = (df['B188'] + df['B198'] + df['B208'] + df['B218'] + df['B228'] + df['B238'] + df['B248'] + df['B258'] + df['B268']) / \
             ((df['B4']-df['B6']) + (df['B14']-df['B16']) + (df['B24']-df['B26']) + (df['B34']-df['B36']) + (df['B44']-df['B46']) + (df['B54']-df['B56']) + (df['B64']-df['B66']) + (df['B74']-df['B76']) + (df['B84']-df['B86']))

# Sonucu yeni bir Excel dosyasına kaydet
df.to_excel('Kategori4_1sonuc.xlsx', index=False)

print("Yeni sütunlar başarıyla oluşturuldu ve sonuc.xlsx dosyasına kaydedildi.")
