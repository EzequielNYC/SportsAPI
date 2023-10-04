import sqlite3

def insert_data_into_database(database_name, data, team):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    table_name = f"{team}_data"


    # check if row is in the database
    for index, row in data.iterrows():
        cursor.execute("""
            SELECT COUNT(*) FROM {table_name}
            WHERE date=? AND opponent=? AND result=?
            """.format(table_name=table_name), (
                    row['date'], row['opponent'], row['result']
                ))
        result = cursor.fetchone()

        # inserting new rows 
        if result[0] == 0:
            cursor.execute("""
                INSERT INTO {table_name} (date, opponent, result, {team}_score, opponent_score, location, total_wins, total_losses, divisional_wins, divisional_losses)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """.format(table_name=table_name, team=team), (
                row['date'], row['opponent'], row['result'], row['ny_score'], row['opponent_score'], row['location'],
                row['total_wins'], row['total_losses'], row['divisional_wins'], row['divisional_losses']
            ))

    connection.commit()
    connection.close()
