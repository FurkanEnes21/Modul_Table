import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import pandas as pd

# AES şifreleme için gerekli fonksiyonları tanımlayalım
def pad(s):
    return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

def aes_encrypt(plaintext, key):
    plaintext = pad(plaintext)
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(plaintext.encode())

# AES anahtarını (32 bayt = 256 bit) oluştur
aes_key = get_random_bytes(32)

# Benzersiz ID'leri oluştur
def create_unique_id(index):
    # ID'nin başlangıç kısmı
    id_start = 'S635'
    # Index'i baz alarak bir plaintext oluştur
    plaintext = f'{index}'.zfill(7)
    # AES-256 ile şifrele
    
    encrypted = aes_encrypt(plaintext, aes_key)
    
    # Şifreli metni hexadecimal formatına çevir
    hex_encrypted = encrypted.hex()
    # Hexadecimal çıktının ilk 7 karakterini al
    id_end = hex_encrypted[:7].upper()
    # ID'yi oluştur
    unique_id = f'{id_start}{id_end}'
    return unique_id

# Belirtilen klasördeki tüm CSV dosyalarına işlemi uygulama
folder_path = 'C:\\Users\\Dell\\Desktop\\0-90\\Data'

for idx, file_name in enumerate(os.listdir(folder_path), start=1):
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)
        
        # CSV dosyasını oku
        df = pd.read_csv(file_path)
        
        # Her satır için benzersiz bir ID oluştur ve atama yap
        
        df['ID'] = [create_unique_id(i) for i in range(1, len(df) + 1)]
        

        # Sonuçları aynı dosyaya kaydet
        df.to_csv(file_path, index=False)

        # Dosya ismi için benzersiz ID oluştur
        file_unique_id = create_unique_id(idx)

# Dosya ismini belirtilen formata dönüştür
# Örnek dosya adı formatı: argentina-primera-division-2024-to-2024-stats.csv
        new_file_name = file_name.replace('stats', f'{file_unique_id}-stats')
        print(new_file_name)
        new_file_path = os.path.join(folder_path, new_file_name)

# Dosyayı yeni isimle yeniden adlandır
        os.rename(file_path, new_file_path)

        
      

print("İşlem tamamlandı.")
