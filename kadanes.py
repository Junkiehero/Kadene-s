from alpha_vantage.timeseries import TimeSeries

# Enter the API key here
api_key = '5487CLEN5VSSA73O'

def fetch_stock_data(ticker):
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, meta_data = ts.get_daily(symbol=ticker, outputsize='compact')
    return list(data['4. close'])  # Closing prices

def max_profit(prices):
    if not prices or len(prices) < 2:
        return 0, None, None # If no prices or fewer than 2, no profit

    max_profit = 0
    min_price = prices[0]
    buy_day = sell_day = 0
    temp_buy_day = 0

    for day in range(1, len(prices)):
        if prices[day] < min_price:
            min_price = prices[day]
            temp_buy_day = day  # Update the day to buy

        current_profit = prices[day] - min_price
        
        if current_profit > max_profit:
            max_profit = current_profit
            buy_day = temp_buy_day
            sell_day = day  # Update the day to sell

    return max_profit, buy_day, sell_day

# Example: Fetch closing prices of Apple (AAPL) stock
stock_prices = fetch_stock_data("AAPL")

if stock_prices:
    profit, buy, sell = max_profit(stock_prices)
    if profit > 0:
        print(f"Best buy day: {buy}, fiyat: {stock_prices[buy]}")
        print(f"Best sell day: {sell}, fiyat: {stock_prices[sell]}")
        print(f"Maximum profit: {profit}")
    else:
        print("No profitable transaction found.")
else:
    print("Stock data could not be fetched.")
