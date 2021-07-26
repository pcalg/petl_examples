import pandas as pd

def conv_game_type(game_type):
    mapping = {"A": "Action", "R": "RPG", "S": "Simulation"}

    return mapping[game_type]

def convert_date(dt):
    dt_parts = dt.split('-')
    return f"{dt_parts[2]}{dt_parts[1]}{dt_parts[0]}"

# read in the data files
df_scores = pd.read_csv('inputfiles\players.csv')
df_games = pd.read_csv('inputfiles\games.csv')

# join the dataframes
df_join = pd.merge(df_scores, df_games, on='game_id')

# operations
df_join['name'] = df_join['name'].str.upper()
df_join['loggedin'] = df_join['loggedin'].apply(convert_date)
df_join['game_type'] = df_join['game_type'].apply(conv_game_type)
df_join['totalscore'] = df_join['score'] * df_join['amount']

df_join = df_join[['name', 'game_name', 'totalscore', 'loggedin', 'game_type']]
df_join = df_join.rename(columns={'loggedin': 'date_logged_in', 'totalscore': 'total_score'})

df_join.to_csv('outputfiles\game_scores2.csv', sep='|', index=False)
