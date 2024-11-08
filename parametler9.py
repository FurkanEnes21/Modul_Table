
import pandas as pd
from tqdm import tqdm

# Excel dosyasını oku
df = pd.read_excel('Kategori6_1sonuc.xlsx')

# Yeni sütunlar oluşturma fonksiyonu
def yeni_sutun_olustur(df, yeni_sutun_adi, bolunen_sutun, bolen_sutun):
    with pd.option_context('mode.use_inf_as_na', True):
        df[yeni_sutun_adi] = df[bolunen_sutun] - df[bolen_sutun]
        df[yeni_sutun_adi].fillna(0, inplace=True)  # 0/0 durumunda 0 olarak kabul et
    return df

# Belirtilen şartlara göre sütunları oluşturma
sartlar = {
    'B541': ('B271', 'B361'),
    'B542': ('B272', 'B362'),
    'B543': ('B273', 'B363'),
    'B544': ('B274', 'B364'),
    'B545': ('B275', 'B365'),
    'B546': ('B276', 'B366'),
    'B547': ('B277', 'B367'),
    'B548': ('B278', 'B368'),
    'B549': ('B279', 'B369'),
    'B550': ('B280', 'B370'),
    'B551': ('B281', 'B371'),
    'B552': ('B282', 'B372'),
    'B553': ('B283', 'B373'),
    'B554': ('B284', 'B374'),
    'B555': ('B285', 'B375'),
    'B556': ('B286', 'B376'),
    'B557': ('B287', 'B377'),
    'B558': ('B288', 'B378'),
    'B559': ('B289', 'B379'),
    'B560': ('B290', 'B380'),
    'B561': ('B291', 'B381'),
    'B562': ('B292', 'B382'),
    'B563': ('B293', 'B383'),
    'B564': ('B294', 'B384'),
    'B565': ('B295', 'B385'),
    'B566': ('B296', 'B386'),
    'B567': ('B297', 'B387'),
    'B568': ('B298', 'B388'),
    'B569': ('B299', 'B389'),
    'B570': ('B300', 'B390'),
    'B571': ('B301', 'B391'),
    'B572': ('B302', 'B392'),
    'B573': ('B303', 'B393'),
    'B574': ('B304', 'B394'),
    'B575': ('B305', 'B395'),
    'B576': ('B306', 'B396'),
    'B577': ('B307', 'B397'),
    'B578': ('B308', 'B398'),
    'B579': ('B309', 'B399'),
    'B580': ('B310', 'B400'),
    'B581': ('B311', 'B401'),
    'B582': ('B312', 'B402'),
    'B583': ('B313', 'B403'),
    'B584': ('B314', 'B404'),
    'B585': ('B315', 'B405'),
    'B586': ('B316', 'B406'),
    'B587': ('B317', 'B407'),
    'B588': ('B318', 'B408'),
    'B589': ('B319', 'B409'),
    'B590': ('B320', 'B410'),
    'B591': ('B321', 'B411'),
    'B592': ('B322', 'B412'),
    'B593': ('B323', 'B413'),
    'B594': ('B324', 'B414'),
    'B595': ('B325', 'B415'),
    'B596': ('B326', 'B416'),
    'B597': ('B327', 'B417'),
    'B598': ('B328', 'B418'),
    'B599': ('B329', 'B419'),
    'B600': ('B330', 'B420'),
    'B601': ('B331', 'B421'),
    'B602': ('B332', 'B422'),
    'B603': ('B333', 'B423'),
    'B604': ('B334', 'B424'),
    'B605': ('B335', 'B425'),
    'B606': ('B336', 'B426'),
    'B607': ('B337', 'B427'),
    'B608': ('B338', 'B428'),
    'B609': ('B339', 'B429'),
    'B610': ('B340', 'B430'),
    'B611': ('B341', 'B431'),
    'B612': ('B342', 'B432'),
    'B613': ('B343', 'B433'),
    'B614': ('B344', 'B434'),
    'B615': ('B345', 'B435'),
    'B616': ('B346', 'B436'),
    'B617': ('B347', 'B437'),
    'B618': ('B348', 'B438'),
    'B619': ('B349', 'B439'),
    'B620': ('B350', 'B440')
}

# Yeni sütunları bir veri çerçevesine ekle
new_columns = {}

for yeni_sutun, (bolunen_sutun, bolen_sutun) in tqdm(sartlar.items(), desc="Sütunları hesaplıyor"):
    new_columns[yeni_sutun] = df[bolunen_sutun] - df[bolen_sutun]

# Yeni sütunları DataFrame'e ekle
new_columns_df = pd.DataFrame(new_columns)
df = pd.concat([df, new_columns_df], axis=1)

# Sonucu yeni bir Excel dosyasına kaydet
with pd.ExcelWriter('Kategori7_1sonuc.xlsx', engine='xlsxwriter') as writer:
    writer.book.use_zip64()
    df.to_excel(writer, index=False)

print("Yeni sütunlar başarıyla oluşturuldu ve sonuc.xlsx dosyasına kaydedildi.")
