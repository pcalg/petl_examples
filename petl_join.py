import petl as etl

def conv_game_type(game_type):
    mapping = {"A": "Action", "R": "RPG", "S": "Simulation"}

    return mapping[game_type]

def convert_date(dt):
    dt_parts = dt.split('-')
    return f"{dt_parts[2]}{dt_parts[1]}{dt_parts[0]}"


# read in the data files
table_scores = etl.fromcsv('inputfiles\players.csv')
table_games = etl.fromcsv('inputfiles\games.csv')

table_join = etl.join(table_scores, table_games, key='game_id')

table_output = (table_join
                .convert({'name': 'upper', 'score': int, 'amount': int, 'loggedin': convert_date, 'game_type': conv_game_type})
                .addfield('totalscore', lambda row: row.score * row.amount)
                .cut('name', 'game_name', 'totalscore', 'loggedin', 'game_type')
                .rename({'loggedin': 'date_logged_in', 'totalscore': 'total_score'})
                )

etl.tocsv(table_output, 'outputfiles\game_scores.csv', delimiter="|")
