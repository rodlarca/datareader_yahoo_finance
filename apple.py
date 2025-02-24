import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#companies = ['AAPL', 'MSFT', 'GE', 'NVDA']
#companies = ['NVDA']
#companies = ['PLTR', 'ROKU', 'SNOW', 'NFLX', 'MELI', 'GOOGL', 'AWS']
companies = ["MSFT", "AMZN", "GOOGL"]

shares_multiple_df = yf.download(companies, start='2021-11-01', end='2025-02-22', group_by='ticker', auto_adjust=False)

shares_multiple_df = shares_multiple_df.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index()

def plot_timeseries_df(df, attrib, ticker_loc=1, title='Timeseries', legend=''):
    fig = plt.figure(figsize=(15, 7))
    
    for company in companies:
        company_data = df[df['Ticker'] == company]
        plt.plot(company_data['Date'], company_data[attrib], '-', label=company)

    plt.xticks(rotation=90)
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(ticker_loc))
    plt.title(title)
    plt.legend()
    plt.show()

plot_timeseries_df(shares_multiple_df, "Close", ticker_loc=15, title="Close Price", legend=companies)