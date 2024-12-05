import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    """
    Получает исторические данные об акциях для указанного тикера и временного периода.
    Возвращает DataFrame с данными.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    """
    Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.
    """
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    """
    Вычисляет и выводит среднюю цену закрытия акций за заданный период.
    """
    average_price = data['Close'].mean()
    print(f'Средняя цена закрытия акций за период: {average_price:.2f}')


def notify_if_strong_fluctuations(data, threshold):
    """
    Анализирует данные и уведомляет пользователя, если цена акций колебалась
    более чем на заданный процент за период
    """
    max_price = data['Close'].max()
    min_price = data['Close'].min()
    fluctuation = (max_price - min_price) / min_price * 100
    if fluctuation > threshold:
        print(f'Цена акций колебалась более чем на {threshold:.2f}% за период. '
              f'Колебание составило: {fluctuation:.2f}%')
    else:
        print(f'Цена акций колебалась менее чем на {threshold:.2f}% за период. '
              f'Колебание составило: {fluctuation:.2f}%')


def export_data_to_csv(data, filename):
    """
    Экспортирует данные в CSV-файл.
    """
    data.to_csv(filename, index=False)
    print(f"Данные сохранены в {filename}")
