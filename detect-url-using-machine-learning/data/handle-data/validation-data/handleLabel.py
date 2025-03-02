# fix some miscoded urls
import pandas as pd
import os

def handleLable():
    current_directory = os.getcwd()
    # print(current_directory)
    # get current file data
    maclicious_path = os.path.join(current_directory, 'data/raw/malicious_phish.csv' )
    urlset_path = os.path.join(current_directory, 'data/raw/urlset.csv' )

    # Read the CSV file
    maclicious = pd.read_csv(maclicious_path)
    urlset = pd.read_csv(urlset_path,  encoding='latin-1', on_bad_lines='skip')

    # print(maclicious.describe())
    # print(urlset.head(5))

    # Just get the 'type' column from urlset and combine based on the 'url' column
    merged_df = pd.merge(maclicious, urlset[['url', 'label']], on='url', how='left')

    # Update type value based on label
    merged_df['type'] = merged_df.apply(lambda x: 'benign' if x['label'] == 0 else x['type'], axis=1)

    # Drop the 'label' column
    merged_df.drop('label', axis=1, inplace=True)

    # check douplicate rows
    num_duplicates = merged_df.duplicated().sum()
    print("Number of duplicate rows:", num_duplicates)
    # Remove duplicates (optional)
    merged_df.drop_duplicates(keep='first', inplace=True) 
    num_duplicates = merged_df.duplicated().sum()
    print("Number of duplicate rows:", num_duplicates.sum()) 
    # #export new file
    new_path = os.path.join(current_directory, 'data/processed/new-dataset.csv')
    merged_df.to_csv(new_path, index=False)
    
if __name__ == "__main__": 
    handleLable()  
