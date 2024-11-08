
import pandas as pd
from tqdm import tqdm

# Excel dosyasını oku
df = pd.read_excel('Kategori5_1sonuc.xlsx')

# Yeni sütunlar oluşturma fonksiyonu
def yeni_sutun_olustur(df, yeni_sutun_adi, bolunen_sutun, bolen_sutun):
    with pd.option_context('mode.use_inf_as_na', True):
        df[yeni_sutun_adi] = df[bolunen_sutun] / df[bolen_sutun]
        df[yeni_sutun_adi].fillna(0, inplace=True)  # 0/0 durumunda 0 olarak kabul et
    return df

# Belirtilen şartlara göre sütunları oluşturma
sartlar = {
    'B401': ('B190', 'B100'),
    'B402': ('B200', 'B110'),
    'B403': ('B210', 'B120'),
    'B404': ('B220', 'B130'),
    'B405': ('B230', 'B140'),
    'B406': ('B240', 'B150'),
    'B407': ('B250', 'B160'),
    'B408': ('B260', 'B170'),
    'B409': ('B270', 'B180'),
    'B411': ('B183', 'B92'),
    'B412': ('B193', 'B102'),
    'B413': ('B203', 'B112'),
    'B414': ('B213', 'B122'),
    'B415': ('B223', 'B132'),
    'B416': ('B233', 'B142'),
    'B417': ('B243', 'B152'),
    'B418': ('B253', 'B162'),
    'B419': ('B263', 'B172'),
    'B421': ('B186', 'B94'),
    'B422': ('B196', 'B104'),
    'B423': ('B206', 'B114'),
    'B424': ('B216', 'B124'),
    'B425': ('B226', 'B134'),
    'B426': ('B236', 'B144'),
    'B427': ('B246', 'B154'),
    'B428': ('B256', 'B164'),
    'B429': ('B266', 'B174'),
    'B431': ('B187', 'B96'),
    'B432': ('B197', 'B106'),
    'B433': ('B207', 'B116'),
    'B434': ('B217', 'B126'),
    'B435': ('B227', 'B136'),
    'B436': ('B237', 'B146'),
    'B437': ('B247', 'B156'),
    'B438': ('B257', 'B166'),
    'B439': ('B267', 'B176'),
    'B441': ('B188', 'B94-B96'),
    'B442': ('B198', 'B104-B106'),
    'B443': ('B208', 'B114-B116'),
    'B444': ('B218', 'B124-B126'),
    'B445': ('B228', 'B134-B136'),
    'B446': ('B238', 'B144-B146'),
    'B447': ('B248', 'B154-B156'),
    'B448': ('B258', 'B164-B166'),
    'B449': ('B268', 'B174-B176'),
    'B451': ('B2', 'B92'),
    'B452': ('B12', 'B102'),
    'B453': ('B22', 'B112'),
    'B454': ('B32', 'B122'),
    'B455': ('B42', 'B132'),
    'B456': ('B52', 'B142'),
    'B457': ('B62', 'B152'),
    'B458': ('B72', 'B162'),
    'B459': ('B82', 'B172'),
    'B461': ('B3', 'B93'),
    'B462': ('B13', 'B103'),
    'B463': ('B23', 'B113'),
    'B464': ('B33', 'B123'),
    'B465': ('B43', 'B133'),
    'B466': ('B53', 'B143'),
    'B467': ('B63', 'B153'),
    'B468': ('B73', 'B163'),
    'B469': ('B83', 'B173'),
    'B471': ('B4', 'B94'),
    'B472': ('B14', 'B104'),
    'B473': ('B24', 'B114'),
    'B474': ('B34', 'B124'),
    'B475': ('B44', 'B134'),
    'B476': ('B54', 'B144'),
    'B477': ('B64', 'B154'),
    'B478': ('B74', 'B164'),
    'B479': ('B84', 'B174'),
    'B481': ('B5', 'B95'),
    'B482': ('B15', 'B105'),
    'B483': ('B25', 'B115'),
    'B484': ('B35', 'B125'),
    'B485': ('B45', 'B135'),
    'B486': ('B55', 'B145'),
    'B487': ('B65', 'B155'),
    'B488': ('B75', 'B165'),
    'B489': ('B85', 'B175'),
    'B491': ('B6', 'B96'),
    'B492': ('B16', 'B106'),
    'B493': ('B26', 'B116'),
    'B494': ('B36', 'B126'),
    'B495': ('B46', 'B136'),
    'B496': ('B56', 'B146'),
    'B497': ('B66', 'B156'),
    'B498': ('B76', 'B166'),
    'B499': ('B86', 'B176'),
    'B501': ('B7', 'B97'),
    'B502': ('B17', 'B107'),
    'B503': ('B27', 'B117'),
    'B504': ('B37', 'B127'),
    'B505': ('B47', 'B137'),
    'B506': ('B57', 'B147'),
    'B507': ('B67', 'B157'),
    'B508': ('B77', 'B167'),
    'B509': ('B87', 'B177'),
    'B511': ('B8', 'B98'),
    'B512': ('B18', 'B108'),
    'B513': ('B28', 'B118'),
    'B514': ('B38', 'B128'),
    'B515': ('B48', 'B138'),
    'B516': ('B58', 'B148'),
    'B517': ('B68', 'B158'),
    'B518': ('B78', 'B168'),
    'B519': ('B88', 'B178'),
    'B521': ('B9', 'B99'),
    'B522': ('B19', 'B109'),
    'B523': ('B29', 'B119'),
    'B524': ('B39', 'B129'),
    'B525': ('B49', 'B139'),
    'B526': ('B59', 'B149'),
    'B527': ('B69', 'B159'),
    'B528': ('B79', 'B169'),
    'B529': ('B89', 'B179'),
    'B531': ('B10', 'B100'),
    'B532': ('B20', 'B110'),
    'B533': ('B30', 'B120'),
    'B534': ('B40', 'B130'),
    'B535': ('B50', 'B140'),
    'B536': ('B60', 'B150'),
    'B537': ('B70', 'B160'),
    'B538': ('B80', 'B170'),
    'B539': ('B90', 'B180')
}

# Yeni sütunları bir veri çerçevesine ekle
new_columns = {}

for yeni_sutun, (bolunen_sutun, bolen_sutun) in tqdm(sartlar.items(), desc="Sütunları hesaplıyor"):
    if '-' in bolen_sutun:
        bolen_sutun_adi = bolen_sutun.split('-')
        new_columns[yeni_sutun] = df[bolunen_sutun] / (df[bolen_sutun_adi[0]] - df[bolen_sutun_adi[1]])
    else:
        new_columns[yeni_sutun] = df[bolunen_sutun] / df[bolen_sutun]

# Özel hesaplamalar
new_columns['B410'] = (df['B200'] + df['B210'] + df['B220'] + df['B230'] + df['B240'] + df['B250'] + df['B260'] + df['B270']) / \
                      (df['B100'] + df['B110'] + df['B120'] + df['B130'] + df['B140'] + df['B150'] + df['B160'] + df['B170'] + df['B180'])

new_columns['B420'] = (df['B183'] + df['B193'] + df['B203'] + df['B213'] + df['B223'] + df['B233'] + df['B243'] + df['B253'] + df['B263']) / \
                      (df['B92'] + df['B102'] + df['B112'] + df['B122'] + df['B132'] + df['B142'] + df['B152'] + df['B162'] + df['B172'])

new_columns['B430'] = (df['B186'] + df['B196'] + df['B206'] + df['B216'] + df['B226'] + df['B236'] + df['B246'] + df['B256'] + df['B266']) / \
                      (df['B94'] + df['B104'] + df['B114'] + df['B124'] + df['B134'] + df['B144'] + df['B154'] + df['B164'] + df['B174'])

new_columns['B440'] = (df['B187'] + df['B197'] + df['B207'] + df['B217'] + df['B227'] + df['B237'] + df['B247'] + df['B257'] + df['B267']) / \
                      (df['B96'] + df['B106'] + df['B116'] + df['B126'] + df['B136'] + df['B146'] + df['B156'] + df['B166'] + df['B176'])

new_columns['B450'] = (df['B188'] + df['B198'] + df['B208'] + df['B218'] + df['B228'] + df['B238'] + df['B248'] + df['B258'] + df['B268']) / \
                      ((df['B94']-df['B96']) + (df['B104']-df['B106']) + (df['B114']-df['B116']) + (df['B124']-df['B126']) + (df['B134']-df['B136']) + (df['B144']-df['B146']) + (df['B154']-df['B156']) + (df['B164']-df['B166']) + (df['B174']-df['B176']))

new_columns['B460'] = (df['B2'] + df['B12'] + df['B22'] + df['B32'] + df['B42'] + df['B52'] + df['B62'] + df['B72'] + df['B82']) - \
                      (df['B92'] + df['B102'] + df['B112'] + df['B122'] + df['B132'] + df['B142'] + df['B152'] + df['B162'] + df['B172'])

new_columns['B470'] = (df['B3'] + df['B13'] + df['B23'] + df['B33'] + df['B43'] + df['B53'] + df['B63'] + df['B73'] + df['B83']) - \
                      (df['B93'] + df['B103'] + df['B113'] + df['B123'] + df['B133'] + df['B143'] + df['B153'] + df['B163'] + df['B173'])

new_columns['B480'] = (df['B4'] + df['B14'] + df['B24'] + df['B34'] + df['B44'] + df['B54'] + df['B64'] + df['B74'] + df['B84']) - \
                      (df['B94'] + df['B104'] + df['B114'] + df['B124'] + df['B134'] + df['B144'] + df['B154'] + df['B164'] + df['B174'])

new_columns['B490'] = (df['B5'] + df['B15'] + df['B25'] + df['B35'] + df['B45'] + df['B55'] + df['B65'] + df['B75'] + df['B85']) - \
                      (df['B95'] + df['B105'] + df['B115'] + df['B125'] + df['B135'] + df['B145'] + df['B155'] + df['B165'] + df['B175'])

new_columns['B500'] = (df['B6'] + df['B16'] + df['B26'] + df['B36'] + df['B46'] + df['B56'] + df['B66'] + df['B76'] + df['B86']) - \
                      (df['B96'] + df['B106'] + df['B116'] + df['B126'] + df['B136'] + df['B146'] + df['B156'] + df['B166'] + df['B176'])

new_columns['B510'] = (df['B7'] + df['B17'] + df['B27'] + df['B37'] + df['B47'] + df['B57'] + df['B67'] + df['B77'] + df['B87']) - \
                      (df['B97'] + df['B107'] + df['B117'] + df['B127'] + df['B137'] + df['B147'] + df['B157'] + df['B167'] + df['B177'])

new_columns['B520'] = (df['B8'] + df['B18'] + df['B28'] + df['B38'] + df['B48'] + df['B58'] + df['B68'] + df['B78'] + df['B88']) - \
                      (df['B98'] + df['B108'] + df['B118'] + df['B128'] + df['B138'] + df['B148'] + df['B158'] + df['B168'] + df['B178'])

new_columns['B530'] = (df['B9'] + df['B19'] + df['B29'] + df['B39'] + df['B49'] + df['B59'] + df['B69'] + df['B79'] + df['B89']) - \
                      (df['B99'] + df['B109'] + df['B119'] + df['B129'] + df['B139'] + df['B149'] + df['B159'] + df['B169'] + df['B179'])

new_columns['B540'] = (df['B10'] + df['B20'] + df['B30'] + df['B40'] + df['B50'] + df['B60'] + df['B70'] + df['B80'] + df['B90']) - \
                      (df['B100'] + df['B110'] + df['B120'] + df['B130'] + df['B140'] + df['B150'] + df['B160'] + df['B170'] + df['B180'])

# Yeni sütunları DataFrame'e ekle
new_columns_df = pd.DataFrame(new_columns)
df = pd.concat([df, new_columns_df], axis=1)

# Sonucu yeni bir Excel dosyasına kaydet
with pd.ExcelWriter('Kategori6_1sonuc.xlsx', engine='xlsxwriter') as writer:
    writer.book.use_zip64()
    df.to_excel(writer, index=False)

print("Yeni sütunlar başarıyla oluşturuldu ve sonuc.xlsx dosyasına kaydedildi.")

