import pandas as pd

def show(df):
    """
    Add in the chain for debugging purposes.

    :param df: input dataframe
    :return: df
    """
    print(df.head())
    return df


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

df_join = (df_join
           .assign(name=lambda df: df['name'].str.upper()
                   , totalscore=lambda df: df['score'] * df['amount']
                   , game_type=lambda df: df['game_type'].apply(conv_game_type)
                   , loggedin=lambda df: df['loggedin'].apply(convert_date)
                   )
           .filter(['name', 'game_name', 'totalscore', 'loggedin', 'game_type'])
           .rename(columns={'loggedin': 'date_logged_in', 'totalscore': 'total_score'})
           .pipe(show)
           )

df_join.to_csv('outputfiles\game_scores3.csv', sep='|', index=False)
