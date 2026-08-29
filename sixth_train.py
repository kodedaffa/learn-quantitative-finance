import numpy as np

prices = np.array([150, 153, 151, 156, 160, 158, 162, 165, 163, 168])

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
statistic = stats_asset(prices)
change = daily_change(prices)
rate = daily_return(change, prices)
positive_days, negative_days, highest, lowest, mean_rates = return_classification(rate)
conditional_one, conditional_two, conditional_three = conditional_analysis(rate)
abs_value = simple_volatility(change)
above_mean, equal_160, below_mean = compare_prices(prices, statistic[3])
report.update({
    "statistic": statistic,
    "changes": change,
    "return": rate,
    "positive_days": positive_days,
    "negative_days": negative_days,
    "highest": highest,
    "lowest": lowest,
    "mean_rates": mean_rates,
    "conditional_one": conditional_one,
    "conditional_two": conditional_two,
    "conditional_three": conditional_three,
    "simple_volatility": abs_value,
    "above_mean": above_mean,
    "equal_160": equal_160,
    "below_mean": below_mean
})

#output
print("<" + "=" * 10 + " Analysis Report " + "=" * 10 + ">")
print("# Statistic of Asset Prices")
print("1. Asset Price Frequency:", report["statistic"][0])
print("2. Highest Price:", report["statistic"][2])
print("3. Lowest Price:", report["statistic"][1])
print("4. Average Price:", report["statistic"][3])
print("5. Price Range:", report["statistic"][0])
print("6. Price Shape:", report["statistic"][4])
print("# Change of Asset Prices")
for i, change in enumerate(report["changes"], start=1):
    print(f"Change Day no. {i}: {change}")
print("# Return of Asset Prices")
for i, return_val in enumerate(report["return"], start=1):
    print(f"Return Day no. {i}: {return_val}%")
print("# Positive and Negative Days")
print("1. Positive Days:"+", ".join(f"{day}%" for day in report["positive_days"]))
print("2. Negative Days:"+", ".join(f"{day}%" for day in report["negative_days"]))
print("3. Highest Return:", report["highest"], "%")  
print("4. Lowest Return:", report["lowest"], "%")
print("5. Mean Return:", report["mean_rates"], "%")
print("# Conditional Analysis")
print("1. Days with Return > 1%: "+", ".join(f"{day}%" for day in report["conditional_one"]))
print("2. Days with Return < 0%: "+", ".join(f"{day}%" for day in report["conditional_two"]))
print("3. Days with Return between 0% and 1%: "+", ".join(f"{day}%" for day in report["conditional_three"]))
print("# Simple Volatility")
print("1. Simple Volatility of Asset Price Changes:", report["simple_volatility"])
print("# Comparison to Mean Price")
print("1. Prices Above Mean Price:", report["above_mean"])
print("2. Prices Equal or Above 160:", report["equal_160"])
print("3. Prices Below Mean Price:", report["below_mean"])