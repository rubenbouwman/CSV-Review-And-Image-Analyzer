import pandas as pd

bol_df = pd.read_csv('CSV files/Bol-product-reviews.csv')
color_df = pd.read_csv('Output/color_analysis.csv')

bol_df['img'] = bol_df['img'].str.split('/').str[-1]
color_df = color_df.rename(columns={'Filename': 'img'})

def mergFiles(file1, file2):
    path = 'Output/merged_analysis_data.csv'

    print('Merging...')
    merged_df = pd.merge(file1, file2, on='img')
    merged_df.to_csv(path, index=False)
    print('Finished merging!')
    print('Saved file to: ' + path)

# -------------------- run --------------------
mergFiles(bol_df, color_df)