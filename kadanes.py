from alpha_vantage.timeseries import TimeSeries

# API anahtarını buraya ekleyin
api_key = '5487CLEN5VSSA73O'

def fetch_stock_data(ticker):
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, meta_data = ts.get_daily(symbol=ticker, outputsize='compact')
    return list(data['4. close'])  # Kapanış fiyatları

def max_profit(prices):
    if not prices or len(prices) < 2:
        return 0, None, None  

    max_profit = 0
    min_price = prices[0]
    buy_day = sell_day = 0
    temp_buy_day = 0

    for day in range(1, len(prices)):
        if prices[day] < min_price:
            min_price = prices[day]
            temp_buy_day = day  

        current_profit = prices[day] - min_price
        
        if current_profit > max_profit:
            max_profit = current_profit
            buy_day = temp_buy_day
            sell_day = day  

    return max_profit, buy_day, sell_day

# Örnek: Apple (AAPL) hissesinin kapanış fiyatlarını al
stock_prices = fetch_stock_data("AAPL")

if stock_prices:
    profit, buy, sell = max_profit(stock_prices)
    if profit > 0:
        print(f"En iyi alım günü: {buy}, fiyat: {stock_prices[buy]}")
        print(f"En iyi satış günü: {sell}, fiyat: {stock_prices[sell]}")
        print(f"Maksimum kâr: {profit}")
    else:
        print("Kâr elde edilecek bir işlem bulunamadı.")
else:
    print("Hisse senedi verisi alınamadı.")
