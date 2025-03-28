import pyodbc
import config # Импортируем модуль config.py

def get_channel_names():
    # Используем переменные из config.py
    conn_str = (
        f"DRIVER={config.DATABASE_DRIVER};"
        f"SERVER={config.DATABASE_SERVER};"
        f"DATABASE={config.DATABASE_NAME};"
        f"Trusted_Connection={config.DATABASE_TRUSTED_CONNECTION};"
    )

    try:
        # Установление подключения
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # SQL-запрос для получения имен каналов из таблицы channels
        query = 'SELECT ChannelName FROM [dbo].[Channels];'
        cursor.execute(query)

        # Извлечение данных
        channel_names = [row[0] for row in cursor.fetchall()]

        # Закрытие подключения
        cursor.close()
        conn.close()

        return channel_names

    except Exception as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return []

if __name__ == "__main__":
    channels = get_channel_names()
    print("Список каналов:", channels)