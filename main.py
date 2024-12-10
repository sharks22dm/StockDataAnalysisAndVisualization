import data_download as dd
import data_plotting as dplt


def main():
    """
    Основная функция, управляющая процессом загрузки, обработки данных и их визуализации.
    Запрашивает у пользователя ввод данных, вызывает функции загрузки и обработки данных,
    а затем передаёт результаты на визуализацию.
    """
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: "
          "AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), "
          "AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: "
          "1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    threshold = float(input("Введите порог колебания цены в процентах (например, '10'): "))

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Расчет и добавление RSI в таблицу
    dd.calculate_rsi(stock_data)

    # Расчет и добавление MACD в таблицу
    dd.calculate_macd(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)
    dplt.plot_rsi(stock_data, ticker)
    dplt.plot_macd(stock_data, ticker)

    # Средняя цена закрытия акций за период
    dd.calculate_and_display_average_price(stock_data)

    # Колебания цен за период
    dd.notify_if_strong_fluctuations(stock_data, threshold)

    # Экспорт данных в CSV файл
    dd.export_data_to_csv(stock_data, f"{ticker}_{period}_stock_data.csv")


if __name__ == "__main__":
    main()
