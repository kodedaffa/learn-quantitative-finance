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
	return change
	
#daily return
def daily_return(gaps, prices):
	rates=[]
	for gap, price in zip(gaps[:7], prices[:7]):
		rates.append(round((gap/price)*100, 2))
	return rates

#

result= {}
for price in prices:
	asse
print(asset["stock"])