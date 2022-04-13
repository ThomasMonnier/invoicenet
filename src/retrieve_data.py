import pandas as pd
import json as js

def save_json(doc, filename):
    with open('train_data_v0/'+filename.split('.')[0]+'.json', 'w', encoding='utf-8') as fp:
        js.dump(doc, fp, ensure_ascii=False)

def create_json(row, features):
    features_dict = dict()
    for feature in features:
        if row[feature] != "None":
            features_dict[feature] = row[feature]
    return features_dict

if __name__=="__main__":
    # for train_data initial file
    # df = pd.read_csv('train_data.csv').fillna('None')
    # df['PDL_v1'] = df['PDL_v1'].map(lambda x: x.split('\n')[0])
    # features = ['provider_name', 'nom_copro', 'adresse_v1', 'PDL_v1', 'current_offer_v1', 'power_v1', 'conso_all', 'kw_unit_cost_all', 'gaz_elec', 'acheminement', 'compte_facturation', 'compte_commercial']
    df = pd.read_csv('train_data_v0.csv').fillna('None').astype(str)
    df['compte_facturation'] = df['compte_facturation'].str.split('.').str[0]
    df['conso_all'] = df['conso_all'].str.split('.').str[0]
    df['power'] = df['power'].str.split('.').str[0]
    features = ['provider_name', 'nom_copro', 'prospect_adress', 'PDL', 'current_offer', 'power', 'subscription_cost', 'last_period_all', 'conso_all', 'kw_unit_cost_all', 'amount_without_tva', 'tva', 'total_amount', 'to_pay', 'acheminement', 'compte_facturation', 'compte_commercial']
    for iter, row in df.iterrows():
        if "Elec" in row['gaz_elec']:
            if len(row['PDL']) < 14:
                df.at[iter, 'PDL'] = '0'+row['PDL']
            doc = create_json(row, features)
            filename = row["file_name"]
            save_json(doc, filename)