import pandas as pd

# Lees het CSV-bestand in een pandas dataframe
df = pd.read_csv('Output/merged_analysis_data.csv')

# Maak een lege dictionary om de woordentellingen bij te houden
word_counts = {}

# Loop door elke rij in de dataframe en tel de woorden in de "body"-kolom
for index, row in df.iterrows():
    body = row['body']
    # splits de tekst in woorden
    words = body.split()
    # tel elk woord in de dictionary
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

# Converteer de dictionary naar een dataframe en sorteer de woorden van meest naar minst voorkomend
word_counts_df = pd.DataFrame.from_dict(word_counts, orient='index', columns=['count'])
word_counts_df = word_counts_df.sort_values(by='count', ascending=False)

# Sla het resultaat op in een nieuw CSV-bestand
word_counts_df.to_csv('Output/word_counts.csv')