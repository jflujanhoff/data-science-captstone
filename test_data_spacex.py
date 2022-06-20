import pandas as pd

spacex_df = pd.read_csv("spacex_launch_dash.csv")

print(spacex_df.head())

#launch_sites_df = spacex_df.groupby('Launch Site')['class'].mean()
launch_sites = spacex_df['Launch Site'].unique()
print(launch_sites)
print("----------")
launch_sites_df = spacex_df.groupby(['Launch Site', 'class']).size().reset_index(name='class count')
print(launch_sites_df)

launch_sites_list = []
all_sites_dict = {'label': 'All Launch Sites', 'value': 'All Launch Sites'}
launch_sites_list.append(all_sites_dict)

for site in launch_sites:
    launch_sites_list.append({'label': site, 'value': site})

print(launch_sites_list)