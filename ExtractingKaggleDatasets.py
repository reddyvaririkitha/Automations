from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile  # to unzip the dataset from kaggle

api = KaggleApi()
api.authenticate()

# active competitions
competition_categories = ['all', 'featured', 'research', 'recruitment', 'gettingStarted', 'masters', 'playground']

active_competitions = {}

for c in competition_categories:
    if c == 'all':
        continue
    else:
        active_competitions[c] = api.competitions_list(category=c)

for cat, comp in active_competitions.items():
    print(f'{cat} : {comp}\n')

# searching a specific competition
search_comp = 'titanic'
search_comp_list = api.competitions_list(search=search_comp)
print(f"competitions related to {search_comp} are:\n{search_comp_list}")

# fetching dataset
search_dataset = 'titanic'
datasets = api.competition_list_files(search_dataset)
print(f'Related datasets of {search_dataset} are: {datasets}')
# downloading the dataset
api.competition_download_files(search_dataset)

# unzipping the downloaded zip file
zf = ZipFile(f'{search_dataset}.zip')
zf.extractall(f'{search_dataset} data')  # save files in selected folder
zf.close()
