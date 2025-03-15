from prometheus_client import start_http_server, Gauge
import psutil
import time

# Создаем метрику для загрузки CPU
cpu_usage = Gauge('cpu_usage_percent', 'Текущая загрузка CPU в процентах')

def collect_metrics():
    while True:
        # Получаем текущую загрузку CPU
        cpu_percent = psutil.cpu_percent(interval=1)
        # Устанавливаем значение метрики
        cpu_usage.set(cpu_percent)
        # Ждем 1 секунду перед следующим обновлением
        time.sleep(1)

if __name__ == '__main__':
    # Запускаем HTTP-сервер на порту 8080
    start_http_server(8080)
    print("Экспортёр метрик запущен на http://localhost:8080")
    # Запускаем сбор метрик
    collect_metrics()