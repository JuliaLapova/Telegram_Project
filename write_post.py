import pyodbc

def get_channel_names():
    # Параметры подключения к базе данных
    conn_str = (
        r'DRIVER={SQL Server};'
        r'SERVER=localhost\SQLEXPRESS;'
        r'DATABASE=automatetg;'
        r'Trusted_Connection=yes;'
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