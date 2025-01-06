import asyncio
from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import Channel
import pandas as pd
import re

# Установите свои API_ID и API_HASH
api_id = 23661681
api_hash = 'efaff6fc0d56bf04e214e63a455b438a'
client_session = 'anon'

# Список имен каналов без @
channel_usernames = [
    'dvizhenieru',
    'ggreat_of_development',
    # Добавьте другие каналы здесь
]

def remove_unwanted_characters(text):
    if text:
        pattern = re.compile(r'[^A-Za-zА-Яа-я0-9\s.,!?;:\'\"()-]')
        return pattern.sub('', text)
    return text

async def fetch_latest_messages(client, channel_username, limit=10):
    data = {'date': [], 'message': [], 'channel': []}
    
    try:
        entity = await client.get_entity(channel_username)
        
        if isinstance(entity, Channel):
            messages = await client(GetHistoryRequest(
                peer=entity,
                limit=limit,
                offset_date=None,
                offset_id=0,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0
            ))

            for message in messages.messages:
                if message.message:
                    message_text = remove_unwanted_characters(message.message)
                    data['date'].append(message.date)
                    data['message'].append(message_text)
                    data['channel'].append(entity.title)

            return pd.DataFrame(data)

    except Exception as e:
        print(f"Ошибка при получении сообщений из {channel_username}: {e}")

    return pd.DataFrame(data)

async def main():
    async with TelegramClient(client_session, api_id, api_hash) as client:
        print("Клиент подключён.")

        # Создаем задачи для всех каналов одновременно
        tasks = [fetch_latest_messages(client, channel_username, limit=10) for channel_username in channel_usernames]

        # Выполняем задачи и ждем их завершения
        results = await asyncio.gather(*tasks)

        # Объединяем результаты таблицы
        combined_df = pd.concat(results, ignore_index=True)

        print(combined_df)
        return combined_df

# Запуск асинхронной функции
if __name__ == "__main__":
    asyncio.run(main())