import sqlite3

class ChampionshipModel:
    def __init__(self):
        self.db_path = "campeonato.sql"  # Nome do banco de dados
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def create_entry(self, table, **values):
        try:
            columns = ", ".join(values.keys())
            placeholders = ", ".join(["?"] * len(values))
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            self.cursor.execute(query, list(values.values()))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error creating entry in {table}: {e}")
            return False

    def read_entries(self, table):
        try:
            query = f"SELECT * FROM {table}"
            self.cursor.execute(query)
            entries = self.cursor.fetchall()
            return entries
        except Exception as e:
            print(f"Error reading entries from {table}: {e}")
            return []

    def update_entry(self, table, entry_id, **values):
        try:
            columns = ", ".join([f"{column} = ?" for column in values.keys()])
            query = f"UPDATE {table} SET {columns} WHERE id = ?"
            self.cursor.execute(query, list(values.values()) + [entry_id])
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error updating entry in {table}: {e}")
            return False

    def delete_entry(self, table, entry_id):
        try:
            query = f"DELETE FROM {table} WHERE id = ?"
            self.cursor.execute(query, (entry_id,))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error deleting entry from {table}: {e}")
            return False

    def close_connection(self):
        self.conn.close()
