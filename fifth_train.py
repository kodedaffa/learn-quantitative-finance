asset={
	"stock": [320, 325, 323, 330, 328, 335, 340, 338]
}

#statistic
def assets_statistic(prices):
	rangePrice= len(prices)
	minPrice= min(prices)
	maxPrice= max(prices)
	meanPrice= round(sum(prices)/len(prices),2)
	return rangePrice, minPrice, maxPrice, meanPrice

#daily change
def daily_change(prices):
	changes=[]
	for price in range(len(prices)-1):
		first_price = prices[price]
		second_price = prices[price+1]
		gap= second_price - first_price
		changes.append(gap)
	return changes
	
#daily return
def daily_return(gaps, prices):
	rates=[]
	for gap, price in zip(gaps[:7], prices[:7]):
		rates.append(round((gap/price)*100, 2))
	return rates

#Classified return
def return_classification(rates):
	upper = max(rates)
	lower = min(rates)
	meanRates = sum(rates)/len(rates)
	return upper, lower, meanRates

#simple volatility
def simple_volatility(changes):
	absolute_changes= [abs(change) for change in changes]
	abs_change = max(absolute_changes)
	return abs_change

#rate return
def filter_return(rates):
	days_positive=[]
	days_negative=[]
	for rate in rates:
		if rate > 0:
			days_positive.append(rate)
		else:
			days_negative.append(rate)
	ratio_return= round((len(days_positive)/len(rates))*100, 2)
	return days_positive, days_negative, ratio_return

#assesment asset
def assesment_asset(rates, positive_ratio):
	mean_return= round(sum(rates)/len(rates), 2)
	if mean_return > 1 and positive_ratio > 70:
		value = "Excellent"
	elif mean_return < 1 and positive_ratio > 70 or mean_return > 1 and positive_ratio < 70:
		value = "Good"
	else:
		value = "Fair"
	return value

#main program
report= {}
for prices in asset.values():
	stats = assets_statistic(prices)
	change = daily_change(prices)
	rate = daily_return(change, prices)
	classification = return_classification(rate)
	abs_value = simple_volatility(change)
	positive, negative, ratio_return = filter_return(rate)
	assesment = assesment_asset(rate, ratio_return)
	report.update({
    "statistic": stats,
    "changes": change,
    "return": rate,
    "limit": classification,
    "absolute": abs_value,
    "positive": positive,
    "negative": negative,
    "winrate": ratio_return,
    "assesment": assesment
    }
	)

#output
print("<"+"="*10+" Analysis Report "+"="*10+">")
print("# Descriptive Statistic")
print("1. Asset Price Frequency:", report["statistic"][0])
print("2. Lowest Asset Price:", report["statistic"][1])
print("3. Highest Asset Price:", report["statistic"][2])
print("4. Average Asset Price:", report["statistic"][3])
print("# Daily Change")
for i, data in enumerate(report["changes"], start=1):
	print(f"Price Change no. {i}: {data}")
print("# Daily Return")
for i, data in enumerate(report["return"], start=1):
	print(f"Percentage Change in Price no. {i}: {data}%")
print("# Classification Percentage Price")
print("1. Lowest Asset Price:", report["limit"][0],"%")
print("2. Highest Asset Price:", report["limit"][1],"%")
print("3. Average Asset Price:", report["limit"][2],"%")
print("# Simple Volatility")
print("1. Simple Volatility of Asset Price Changes:", report["absolute"])
print("# Filter Percentage Price")
print("1. Positive Change in Asset Prices: "+", ".join(f"{data}%" for data in report["positive"]))
print("2. Negative Change in Asset Prices: "+", ".join(f"{data}%" for data in report["negative"]))
print("3. The Ratio of the Positive Percentage Change in Asset Prices:", report["winrate"],"%")
print("# Assesment Asset")
print("1. Overall Assesment of Asset Performance:", report["assesment"])