commodity_prices = [245,250,247,252,260,258,261,259,265,270]
commodity_changes_prices=[]

#Basic Information
def informationPrice(prices):
	rangePrices= len(commodity_prices)
	minPrices= min(commodity_prices)
	maxPrices= max(commodity_prices)
	meanPrices= sum(commodity_prices)/rangePrices
	return rangePrices, minPrices, maxPrices, meanPrices

length, minimum, maximum, mean= informationPrice(commodity_prices)
print(f"1. informasi harga komoditas terdiri dari: \n    A. Frekuensi harga yang tersedia: {length}\n    B. Harga terendah yang tersedia: {minimum}\n    C. Harga tertinggi yang tersedia: {maximum}\n    D. Harga rata-rata dari data yang tersedia: {mean}")

#Daily Change
def changesPrice(prices):
	for price in range(len(commodity_prices)-1):
		changes= commodity_prices[price+1]-commodity_prices[price]
		commodity_changes_prices.append(changes)
	return commodity_changes_prices

returnPrice= changesPrice(commodity_prices)
print(f"2. harga komoditas mengalami perubahan yang dimana:\n    A. Hari pertama dengan kedua memiliki nilai selisih yaitu {commodity_changes_prices[0]}\n    B. Hari kedua dengan ketiga memiliki nilai selisih yaitu {commodity_changes_prices[1]}\n    C. Hari ketiga dengan keempat memiliki nilai selisih yaitu {commodity_changes_prices[2]}\n    D. Hari keempat dengan kelima memiliki nilai selisih yaitu {commodity_changes_prices[3]}\n    E. Hari kelima dengan keenam memiliki nilai selisih yaitu {commodity_changes_prices[4]}\n    F. Hari keenam dengan ketujuh memiliki nilai selisih yaitu {commodity_changes_prices[5]}\n    G. Hari ketujuh dengan kedelapan memiliki nilai selisih yaitu {commodity_changes_prices[6]}\n    H. Hari kedelapan dengan kesembilan memiliki nilai selisih yaitu {commodity_changes_prices[7]}\n    I. Hari kesembilan dengan kesepuluh memiliki nilai selisih yaitu {commodity_changes_prices[8]}")

#Daily return
def percentageRate(differencePrice, prices):
	commodity_rate_prices= []
	for difference, price in zip(commodity_changes_prices[:9], commodity_prices[:9]):
		commodity_rate_prices.append(round((difference/price)*100, 2))
	return commodity_rate_prices
	
rateReturn= percentageRate(commodity_changes_prices, commodity_prices)

print(f"3. harga komoditas mengalami perubahan yang dimana:\n    A. Hari pertama dengan kedua memiliki persentase perubahan yaitu {rateReturn[0]}%\n    B. Hari kedua dengan ketiga memiliki persentase perubahan yaitu {rateReturn[1]}%\n    C. Hari ketiga dengan keempat memiliki persentase perubahan yaitu {rateReturn[2]}%\n    D. Hari keempat dengan kelima memiliki persentase perubahan yaitu {rateReturn[3]}%\n    E. Hari kelima dengan keenam memiliki persentase perubahan yaitu {rateReturn[4]}%\n    F. Hari keenam dengan ketujuh memiliki persentase perubahan yaitu {rateReturn[5]}%\n    G. Hari ketujuh dengan kedelapan memiliki persentase perubahan yaitu {rateReturn[6]}%\n    H. Hari kedelapan dengan kesembilan memiliki persentase perubahan yaitu {rateReturn[7]}%\n    I. Hari kesembilan dengan kesepuluh memiliki persentase perubahan yaitu {rateReturn[8]}%")

#Return Analysis
def limitRate(rate):
	upper = max(rateReturn)
	lower = min(rateReturn)
	return upper, lower

top, bottom = limitRate(rateReturn)
print(f"4. harga komoditas mengalami perubahan dalam kurun waktu 10 hari dengan persentase kenaikan terbesar\n    yaitu {top}% dan persentase penurunan terbesar yaitu {bottom}%")

#return frequency
def frequencyRate(rate):
	ratePositive=[]
	rateNegative=[]
	for rate in rateReturn:
		if rate > 0:
			ratePositive.append(rate)
		else:
			rateNegative.append(rate)
	return ratePositive, rateNegative

resultPositive, resultNegative= frequencyRate(rateReturn)
print(f"5.Dalam kurun waktu 10 hari, harga komoditas mengalami perubahan dengan rate positif sebanyak {len(resultPositive)} kali yang\n   terdiri {resultPositive[0]}%, {resultPositive[1]}%, {resultPositive[2]}%, {resultPositive[3]}%, {resultPositive[4]}%, {resultPositive[5]}% dan perubahan dengan rate negatif sebanyak {len(resultNegative)} kali yang\n   terdiri dari {resultNegative[0]}%, {resultNegative[1]}%, {resultNegative[2]}%")

#percentage rate positive
def percentagePositive(positive, rate):
	RatioRatePositive= round((len(resultPositive)/len(rateReturn))*100, 2)
	return RatioRatePositive

ratioPositive= percentagePositive(resultPositive, rateReturn)
print(f"6. Berdasarkan kurun waktu 10 hari, hari dengan kenaikan harga memiliki persentase sebesar {ratioPositive}%")