import pandas as pd
import json as js
import argparse

def save_json(doc, filename):
    with open('train_data/'+filename.split('.')[0]+'.json', 'w', encoding='utf-8') as fp:
        js.dump(doc, fp, ensure_ascii=False)

def create_json(row, features):
    features_dict = dict()
    for feature in features:
        if row[feature] != "None":
            features_dict[feature] = row[feature]
    return features_dict

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-csv', type=str, help="CSV file containing the URLs of the files")
    parser.add_argument('-features', type=list, help="List of features that we want the model to be trained on")

    args = parser.parse_args()

    df = pd.read_csv(args.csv).fillna('None').astype(str)
    df['compte_facturation'] = df['compte_facturation'].str.split('.').str[0]
    df['conso_all'] = df['conso_all'].str.split('.').str[0]
    df['power'] = df['power'].str.split('.').str[0]
    features = ['provider_name', 'nom_copro', 'prospect_adress', 'PDL', 'current_offer', 'power', 'subscription_cost', 'last_period_all', 'conso_all', 'kw_unit_cost_all', 'amount_without_tva', 'tva', 'total_amount', 'to_pay', 'acheminement', 'compte_facturation', 'compte_commercial']
    # features = args.features 
    for iter, row in df.iterrows():
        if "Elec" in row['gaz_elec']:
            if len(row['PDL']) < 14:
                df.at[iter, 'PDL'] = '0'+row['PDL']
            doc = create_json(row, features)
            filename = row["file_name"]
            save_json(doc, filename)