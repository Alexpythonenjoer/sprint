import os
import psycopg2

class DatabaseHandler:
    def init(self):
        self.host = os.getenv('FSTR_DB_HOST')
        self.port = os.getenv('FSTR_DB_PORT')
        self.user = os.getenv('FSTR_DB_LOGIN')
        self.password = os.getenv('FSTR_DB_PASS')
        self.conn = self.connect_to_db()

    def connect_to_db(self):
        try:
            conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password
            )
            return conn
        except Exception as e:
            print(f"Ошибка подключения к базе данных: {e}")
            return None

    def add_new_pass(self, pass_data):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute("""
                    INSERT INTO passes (name, location, status) 
                    VALUES (%s, %s, 'new')
                """, (pass_data['name'], pass_data['location']))
                self.conn.commit()
                print("Новый перевал успешно добавлен.")
            except Exception as e:
                print(f"Ошибка при добавлении нового перевала: {e}")
                self.conn.rollback()

# Пример использования:
if name == "main":
    db_handler = DatabaseHandler()
    new_pass = {
        'name': 'Название перевала',
        'location': 'Расположение перевала'
    }
    db_handler.add_new_pass(new_pass)