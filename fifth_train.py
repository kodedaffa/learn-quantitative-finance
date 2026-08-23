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
  return days_positive, days_negative


result= {}
for prices in asset.values():
  #print(prices)
  stats = assets_statistic(prices)
  change = daily_change(prices)
  print("ini", stats[0])
  print(type(stats))
  print(type(stats[0]))
  print("ini", change[0])
  print(type(change))
  print(type(change[0]))
  result.update({
    "statistic": stats,
    "Changes": change
    }
  )

print(result)
print(result["statistic"])