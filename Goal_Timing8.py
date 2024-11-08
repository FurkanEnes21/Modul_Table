import openpyxl

# Üç dosya için dosya yollarını listeleyin
file_paths = [
    'Mod8.xlsx' ]

# Her dosya için işlemi tekrarlayın
for file_path in file_paths:
    # Excel dosyasını yükle
    workbook = openpyxl.load_workbook(file_path)
    
    # Tüm çalışma sayfalarını döngüye al
    for sheet in workbook.worksheets:
        # Z sütununa "Goal Timing" başlığını ekle
        sheet['AE1'] = "Goal Timing"
        # Z sütunundaki tüm hücrelere "0-90" değerini ekle
        for row in range(2, sheet.max_row + 1):
            sheet[f'AE{row}'] = "0-90"
    
    # Değişiklikleri kaydet
    workbook.save(file_path)

print("Goal Timing sütunu tüm dosyalara eklendi.")

