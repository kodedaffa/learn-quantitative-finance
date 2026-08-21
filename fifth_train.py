asset={
	"stock": [320, 325, 323, 330, 328, 335, 340, 338]
}

#statistic
def assets_statistic(prices):
	return{
		"rangePrice": len(prices),
		"minPrice": min(prices),
		"minPrice": max(prices),
		"meanPrice": sum(prices)/len(prices)
	}

#daily change
def daily_change(prices):
	changes=[]
	for price in prices:
		gap= prices[price+1] - prices[prices]
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
  return days_positive, days_negative

# result= {}
# for price in prices:
# 	asset
# print(asset["stock"])