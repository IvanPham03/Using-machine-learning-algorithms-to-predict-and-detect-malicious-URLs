# To extract 50,000 rows of data of the "malicious" type (including phishing, malware and defacement) 
# and 50,000 rows of "benign" from a dataset
import pandas as pd
import os

current_dir = os.getcwd()
def extract(data_path):
    data_path = os.path.join(current_dir, data_path)
    data = pd.read_csv(data_path)
    
    # Filter "malicious" rows
    malicious = data[data['type'].isin(['phishing', 'malware', 'defacement'])]
    
    # Filter "benign" rows
    benign = data[data['type'] == 'benign']
    
    # Randomly sample 50,000 rows from each type
    malicious_sample = malicious.sample(n=50000, random_state=42)
    benign_sample = benign.sample(n=50000, random_state=42)
    
    print("malicious_sample: ", malicious_sample.count)
    print("benign_sample: ", benign_sample.count)
    extract_data = pd.concat([malicious_sample, benign_sample])
    
    return extract_data

def main():
    data_path = 'data/processed/new-dataset.csv'
    extracted_data = extract(data_path)
    output_path = os.path.join(current_dir, 'data/processed/extracted_dataset.csv')
    extracted_data.to_csv(output_path, index=False)
    print(f'extract data saved to {output_path}')

if __name__ == '__main__':
    main()
