import matplotlib.pyplot as plt
import pandas as pd


def create_and_save_plot(data, ticker, period, start, end, filename=None):
    """
    Создаёт график, отображающий цены закрытия и скользящие средние.
    Предоставляет возможность сохранения графика в файл. Параметр filename опционален;
    если он не указан, имя файла генерируется автоматически.
    """
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        if start and end:
            filename = f"{ticker}_{start}_{end}_stock_price_chart.png"
        else:
            filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")


def plot_rsi(data, ticker, filename=None):
    """
    Создает график, отображающий индекс относительной силы (RSI).
    Предоставляет возможность сохранения графика в файл. Параметр filename опционален;
    если он не указан, имя файла генерируется автоматически.
    """
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['RSI'].values, label='RSI')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['RSI'], label='RSI')

    plt.title(f"{ticker} Индекс относительной силы (RSI) с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("%")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_RSI_chart.png"

    plt.savefig(filename)
    print(f"График RSI сохранен как {filename}")


def plot_macd(data, ticker, filename=None):
    """
    Создает график, отображающий MACD (Moving Average Convergence Divergence).
    Предоставляет возможность сохранения графика в файл. Параметр filename опционален;
    если он не указан, имя файла генерируется автоматически.
    """
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['MACD'].values, label='MACD')
            plt.plot(dates, data['Signal'].values, label='Signal')
            histogram = data['MACD'] - data['Signal']
            color = ['g' if val >= 0 else 'r' for val in histogram]
            plt.bar(dates, histogram, color=color, width=0.5, alpha=0.5, label='Histogram')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['MACD'], label='MACD')
        plt.plot(data['Date'], data['Signal'], label='Signal')
        histogram = data['MACD'] - data['Signal']
        color = ['g' if val >= 0 else 'r' for val in histogram]
        plt.bar(data['Date'], histogram, color=color, width=0.5, alpha=0.5, label='Histogram')

    plt.title(f"{ticker} MACD с течением времени")
    plt.xlabel("Дата")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_MACD_chart.png"

    plt.savefig(filename)
    print(f"График MACD сохранен как {filename}")
