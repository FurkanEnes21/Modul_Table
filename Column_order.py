import pandas as pd

# Define the desired order of columns
column_order = [
    "Lig ID",
    "Lig Tipi",
    "Game Week",
    "Match Played",
    "Team Name",
    "Goal Count",
    "Cumulative Goal Count",
    "Total Cumulative Goal Count Ratio",
    "Goal Defeated",
    "Cumulative Goal Defeated",
    "Total Cumulative Goal Defetead Ratio",
    "Average",
    "Cumulative Average",
    "Win",
    "Cumulative Win",
    "Draw",
    "Cumulative Draw",
    "Loss",
    "Cumulative Loss",
    "Point",
    "Cumulative Point",
    "Cumulative Point Ratio",
    "All Team Total Goal",
    "Rank",
    "Rank Diff",
    "Total Rank Diff",
    "Goal Timing"
]

# List of file paths
file_paths = [
    "Mod1.xlsx", "Mod2.xlsx", "Mod3.xlsx",
    "Mod4.xlsx", "Mod5.xlsx", "Mod6.xlsx",
    "Mod7.xlsx", "Mod8.xlsx", "Mod9.xlsx"
]

# Process each file individually
for file_path in file_paths:
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Reorder the columns based on what is available
    available_columns = [col for col in column_order if col in df.columns]
    df = df[available_columns]
    
    # Save the reordered DataFrame to the same Excel file
    df.to_excel(file_path, index=False)

print("Columns reordered and saved successfully for all files!")
