import pandas as pd

# Excel dosyasını oku
df = pd.read_excel('Mod5.xlsx')

# Rank Diff sütunu oluştur
df['Rank Diff'] = 0
df['Total Rank Diff'] = 0

# Her bir Lig ID ve Takım için işlemleri gerçekleştir
for league_id in df['Lig ID'].unique():
    league_df = df[df['Lig ID'] == league_id]
    for team in league_df['Team Name'].unique():
        team_df = league_df[league_df['Team Name'] == team]
        team_df = team_df.sort_values(by='Game Week')
        previous_rank = None
        total_rank_diff = 0
        for i, row in team_df.iterrows():
            current_week = row['Game Week']
            current_rank = row['Rank']
            if current_week == 1:
                df.at[i, 'Rank Diff'] = 0
            elif previous_rank is not None:
                df.at[i, 'Rank Diff'] = previous_rank - current_rank
            else:
                df.at[i, 'Rank Diff'] = 0
            
            # Total Rank Diff hesapla
            total_rank_diff += df.at[i, 'Rank Diff']
            df.at[i, 'Total Rank Diff'] = total_rank_diff

            previous_rank = current_rank

# Sonuçları yeni bir Excel dosyasına yaz
df.to_excel('Mod5.xlsx', index=False)

