import numpy as np

prices = np.array([150, 153, 151, 156, 160, 158, 162, 165, 163, 168])
print("Prices:", prices)

#function to calculate statistics of asset prices
def stats_asset(prices):
    range_price = len(prices)
    min_price = np.min(prices)
    max_price = np.max(prices)
    mean_price = np.mean(prices)
    form_price = prices.shape
    return range_price, min_price, max_price, mean_price, form_price

#function to calculate daily change in prices
def daily_change(prices):
    changes = np.diff(prices)
    return changes

#function to calculate daily return based on daily changes and prices
def daily_return(changes, prices):
    rates = (changes / prices[:-1]) * 100
    return np.round(rates, 2)

#function to classify returns into positive and negative days, and calculate highest, lowest, and mean rates
def return_classification(rates):
    positive_days = rates[rates > 0]
    negative_days = rates[rates <= 0]
    highest = np.max(rates)
    lowest = np.min(rates)
    mean_rates = round(np.mean(rates), 2)
    return positive_days, negative_days, highest, lowest, mean_rates

#function to assess the asset based on mean return and positive ratio
def conditional_analysis(rates):
    conditional_one = rates[rates > 1]
    conditional_two = rates[rates < 0]
    conditional_three = rates[(rates >= 0) & (rates <= 1)]
    return conditional_one, conditional_two, conditional_three

#function to calculate simple volatility based on daily changes
def simple_volatility(changes):
    absolute_changes = np.abs(changes)
    abs_change = np.max(absolute_changes)
    return abs_change

#function to compare prices to the mean price
def compare_prices(prices, mean_price):
    above_mean = prices[prices > mean_price]
    below_mean = prices[prices < mean_price]
    equal_160 = prices[prices >= 160]
    return above_mean, equal_160, below_mean

#main program
report = {}
#program statstic
statistic = stats_asset(prices)
report['range'] = statistic[0]
report['min'] = statistic[1]
report['max'] = statistic[2]
report['mean'] = statistic[3]
report['shape'] = statistic[4]

#program change
change = daily_change(prices)
report['daily_change'] = change

#program return
rate = daily_return(change, prices)
report['daily_return'] = rate

#program classification
positive_days, negative_days, highest, lowest, mean_rates = return_classification(rate)
report['positive_days'] = positive_days
report['negative_days'] = negative_days
report['highest'] = highest
report['lowest'] = lowest
report['mean_rates'] = mean_rates

#program conditional
conditional_one, conditional_two, conditional_three = conditional_analysis(rate)
report['conditional_one'] = conditional_one
report['conditional_two'] = conditional_two
report['conditional_three'] = conditional_three

#program absolute
abs_value = simple_volatility(change)
report['simple_volatility'] = abs_value

#program compare prices
above_mean, equal_160, below_mean = compare_prices(prices, report['mean'])
report['above_mean'] = above_mean
report['equal_160'] = equal_160
report['below_mean'] = below_mean

#output
print("Highest Price:", report['max'])
print("Lowest Price:", report['min'])
print("Average Price:", report['mean'])
print("Price Range:", report['range'])
print("Price Shape:", report['shape'])
for i, data in enumerate(report['daily_change'], start=1):
    print(f"Daily Change no. {i}: {data}")
for i, data in enumerate(report['daily_return'], start=1):
    print(f"Daily Return no. {i}: {data}%")
print("Positive Days:", report['positive_days'])
print("Negative Days:", report['negative_days'])
print("Highest Return:", report['highest'], "%")
print("Lowest Return:", report['lowest'], "%")
print("Mean Return:", report['mean_rates'], "%")
print("Conditional One (Return > 1):", report['conditional_one'])
print("Conditional Two (Return < 0):", report['conditional_two'])
print("Conditional Three (0 <= Return <= 1):", report['conditional_three'])
print("Simple Volatility (Max Absolute Change):", report['simple_volatility'])
print("Prices Above Mean:", report['above_mean'])
print("Prices Below Mean:", report['below_mean'])
print("Prices Equal to 160:", report['equal_160'])