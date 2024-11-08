# import os



# def run_scripts_in_order(script_names):
#     """
#     Verilen script isimlerini sırayla çalıştırır.
    
#     Parameters:
#     script_names (list of str): Çalıştırılacak script dosyalarının isimleri.
#     """
#     for script_name in script_names:
#         if os.path.exists(script_name):
            
#             try:
#                 print(f"Çalıştırılıyor: {script_name}")
#                 with open(script_name, 'r', encoding='utf-8') as file:
#                     script_content = file.read()
                    
#                     # Her çalıştırmadan önce local değişkenleri sıfırlıyoruz.
#                     local_scope = {}
#                     exec(script_content, globals(), local_scope)
#             except Exception as e:
#                 print(f"{script_name} çalıştırılırken bir hata oluştu: {e}")
#         else:
#             print(f"Dosya bulunamadı: {script_name}")

# # Örnek kullanım:
# script_list = [
#     # "clear.py",
#     # "Match_data.py",
#     "Id_atama.py",
#     "xlsx.py",
#     "Guncel_Ham_Tablo.py",
#     "Parse_LigID.py",
#     "Automate_Code1.py",
#     "Automate_Code2.py",
#     "Automate_Code3.py",
#     "Automate_Code4.py",
#     "Automate_Code5.py",
#     "Automate_Code6.py",
#     "Automate_Code7.py",
#     "Automate_Code8.py",
#     "Automate_Code9.py",
#     "Type.py",
#     "add_ID.py",
#     "oran.py",
#     "KATEGORI.py",
#     "esleme.py",
#     "esleme2.py"
# ]

# run_scripts_in_order(script_list)










import importlib
import os

def run_scripts_in_order(script_names):
    """
    Verilen script dosyalarını sırayla çalıştırır.
    
    Parameters:
    script_names (list of str): Çalıştırılacak script dosyalarının isimleri (uzantısız).
    """
    for script_name in script_names:
        try:
            print(f"Çalıştırılıyor: {script_name}")
            # Script'i modül olarak import et
            module = importlib.import_module(script_name)
            
            # Modül içindeki main() fonksiyonunu çalıştır
            if hasattr(module, 'main'):
                module.main()
            else:
                print(f"{script_name} dosyasında 'main' fonksiyonu bulunamadı.")
                
        except Exception as e:
            print(f"{script_name} çalıştırılırken bir hata oluştu: {e}")

# Örnek kullanım:
script_list = [
    # "clear.py",
    # "Match_data.py",
    # "Id_atama.py",
    # "xlsx.py",
    # "Guncel_Ham_Tablo.py",
    # "dakıka.py",
    # "Parse_LigID.py",
    # "Automate_Code1.py",
    # "Automate_Code2.py",
    # "Automate_Code3.py",
    # "Automate_Code4.py",
    # "Automate_Code5.py",
    # "Automate_Code6.py",
    # "Automate_Code7.py",
    # "Automate_Code8.py",
    # "Automate_Code9.py",
    # "Type.py",
    # "add_ıd.py",
    # "oran.py",
    # "KATEGORI.py",
    # "esleme.py",
    # "duzenleme.py",
    # "eslme2.py",
    "parametler.py",
   "parametler2.py",
    "parametler3.py",
    "parametler4.py",
    "parametler5.py",
   "parametler6.py",
   "parametler7.py",
   "parametler8.py",
   "parametler9.py",
   "parametler10.py",
   "parametler11.py",
   "parametler12.py",
   "parametler13.py",
   "parametler14.py"
]

run_scripts_in_order(script_list)




