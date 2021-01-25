import datetime
import yfinance as yf
import plotly.graph_objects as go

current_time = datetime.datetime.now()

total_stock_values = []
stock_names = []

class Stock_Portfolio():
    def get_stock_value(interval = '15m'):
        global num_stocks
        num_stocks = int(input("hey how many stocks do you have?? "))
        for i in range(num_stocks):
            stock_name = input("Stock Symbol: ")
            stock_names.append(stock_name)

            data = yf.download(tickers = stock_name, period= '1d', interval = interval)
            now_value = data['Open'][-1]

            num_shares = input('how many shares do you have?? ')
            total_val = now_value * float(num_shares)

            total_val = float('%.2f' % (total_val))
            total_stock_values.append(total_val)

            print("Value of  " + str(stock_name) + " is " + str(now_value))
            print("Total Value of shares : " + str(total_val))
    def create_pie_chart():
        sum = 0
        labels = stock_names
        values = total_stock_values
        for i in range(len(total_stock_values)):
            sum += total_stock_values[i]
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent', insidetextorientation='radial')])
        fig.update_layout(title_text = "Stock Portfolio: $" + str(float('%.2f' % (sum))))

        fig.show()

        print(current_time.strftime('%Y-%m-%d'))
        print(total_stock_values)
        print(stock_names)
    if __name__ == "__main__":
        get_stock_value()
        create_pie_chart()
