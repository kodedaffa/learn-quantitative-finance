stock_A = [125, 128, 130, 127, 131, 133, 132, 135]
stock_B = [210, 208, 205, 207, 209, 212, 214, 213]
stock_C = [80, 81, 83, 82, 84, 86, 89, 91]
group_stock= stock_A, stock_B, stock_C
group_name_stock= ["Saham A", "Saham B", "Saham C"]
group_rate= []
group_frequency= []
group_change=[]
group_ratio=[]
group_total=[]
group_min=[]
group_max=[]
group_mean=[]
group_high=[]
group_positive=[]
group_negative=[]
group_index= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#statistic stock
def stock_statistic(prices):
	rangePrices= len(prices)
	minPrices= min(prices)
	maxPrices= max(prices)
	meanPrices= round(sum(prices)/rangePrices, 2)
	return rangePrices, minPrices, maxPrices, meanPrices
	
#daily change
def stock_change(prices):
	stock_changes=[]
	for price in range(len(prices)-1):
		change= prices[price+1]-prices[price]
		stock_changes.append(change)
	return stock_changes
	
#daily return
def	stock_return(changes, prices):
	stock_rate=[]
	for change, price in zip(changes[:7], prices[:7]):
		stock_rate.append(round((change/price)*100, 2))
	return stock_rate

#return analysis
def return_analysis(rates):
	upper= max(rates)
	lower= min(rates)
	return upper, lower

#Simple Volatility
def simple_volatility(changes):
	absolute_value= [abs(change) for change in changes]
	upper= max(absolute_value)
	return upper

#consistency pt. 1
def consistency(rates):
	days_positive= []
	days_negative= []
	for rate in rates:
		if rate > 0:
			days_positive.append(rate)
		else:
			days_negative.append(rate)
	
	return days_positive, days_negative

#consistency pt. 2
def rate_consistent(positive, days):
	ratio_day_positive= round((len(positive)/len(days))*100, 2)
	return ratio_day_positive
	
#compare stock
def compare_stock(rates, volumes, changes):
	def compare_mean(rate):
		group_overall_mean=[]
		group_amount=[]
		for rate in rates:
			amount_rate= sum(rate)
			group_amount.append(amount_rate)
			group_overall_mean.append(round(sum(rate)/len(rate), 2))
		return group_overall_mean
	def compare_frequency(volume):
		group_overall_frequency=[]
		for volume in volumes:
			group_overall_frequency.append(volume)
		return group_overall_frequency
	def compare_change(change):
		group_overall_change=[]
		for change in changes:
			group_overall_change.append(change)
		return group_overall_change
	return compare_mean(rates), compare_frequency(volumes), compare_change(changes)

#challenge optional
def analysis_continue(raw_inp):
	for i in range(0, len(raw_inp), 2):
		inp_a= raw_inp[i]
		inp_b= raw_inp[i+1]
		if inp_a > 1 and inp_b > 60:

			strength= "strong"
		elif inp_a > 1 and inp_b < 60:
			strength= "moderate"
		else:
			strength= "weak"
	return strength
	

for i, stock in enumerate (group_stock, 1):
 	total, minimum, maximum, mean = stock_statistic(stock)
 	group_total.append(total)
 	group_min.append(minimum)
 	group_max.append(maximum)
 	group_mean.append(mean)
 	daily_change = stock_change(stock)
 	group_change.append(daily_change)
 	daily_return = stock_return(daily_change, stock)
 	group_rate.append(daily_return)
 	top, bottom = return_analysis(daily_return)
 	high = simple_volatility(daily_change)
 	group_high.append(high)
 	positive, negative= consistency(daily_change)
 	group_positive.append(positive)
 	group_negative.append(negative)
 	group_frequency.append(len(positive))
 	rate_positive = rate_consistent(positive, daily_change)
 	group_ratio.append(rate_positive)
 
meanReturn, volumeFrequency, highChange= compare_stock(group_rate, group_frequency, group_high)



raw_val=[]
for i, R in enumerate(zip(meanReturn, group_ratio)):
	raw_val.append(R)

resultVal= []
for x, val in enumerate (raw_val, 1):
	strengthAssesment= analysis_continue(val)
	resultVal.append(strengthAssesment)
	
#report information
print("<======== Information ========>")

print(f"1. Ada 3 saham dengan masing-masing memiliki {max(group_total)} harga")
print(f"2. 3 saham tersebut memiliki harga terendah yang apabila diurutkan menjadi seperti ini:\n    A. {group_name_stock[2]} memiliki harga terendah yaitu {group_min[2]}\n    B. {group_name_stock[0]} memiliki harga terendah yaitu {group_min[0]}\n    C. {group_name_stock[1]} memiliki harga terendah yaitu {group_min[1]}\n    Dengan demikian, saham dengan harga terendah yaitu {group_name_stock[2]}")
print(f"3. 3 saham tersebut memiliki harga tertinggi yang apabila diurutkan menjadi seperti ini:\n    A. {group_name_stock[2]} memiliki harga tertinggi yaitu {group_max[2]}\n    B. {group_name_stock[0]} memiliki harga tertinggi yaitu {group_max[0]}\n    C. {group_name_stock[1]} memiliki harga tertinggi yaitu {group_max[1]}\n    Dengan demikian, saham dengan harga tertinggi yaitu {group_name_stock[1]}")
print(f"4. 3 saham tersebut memiliki harga rata-rata yang apabila diurutkan menjadi seperti ini:\n    A. {group_name_stock[0]} memiliki harga rata-rata yaitu {group_mean[0]}\n    B. {group_name_stock[1]} memiliki harga rata-rata yaitu {group_mean[1]}\n    C. {group_name_stock[2]} memiliki harga rata-rata yaitu {group_mean[2]}")
print(f"5. 3 saham tersebut memiliki perubahan harga di setiap harinya yang dapat dilihat melalui:\n    A. {group_name_stock[0]} memiliki perubahan harga yaitu : {', '.join(map(str, group_change[0]))}\n    B. {group_name_stock[1]} memiliki perubahan harga yaitu {', '.join(map(str, group_change[1]))}\n    C. {group_name_stock[2]} memiliki perubahan harga yaitu {', '.join(map(str, group_change[2]))}")
print(f"6. 3 saham tersebut memiliki perubahan persentase harga di setiap harinya yang dapat dilihat melalui:\n    A. {group_name_stock[0]} memiliki perubahan persentase harga yaitu {', '.join(map(str, group_rate[0]))}\n    B. {group_name_stock[1]} memiliki perubahan persentase harga yaitu {', '.join(map(str, group_rate[1]))}\n    C. {group_name_stock[2]} memiliki perubahan persentase harga yaitu {', '.join(map(str, group_rate[2]))}")
print(f"7. 3 saham tersebut memiliki persentase harga terbesar, terendah dan rata-rata persentase pada yang dapat\n    dilihat melalui:\n    A. {group_name_stock[0]} memiliki persentase harga terbesar yaitu {max(group_rate[0])}%, persentase harga terendah yaitu {min(group_rate[0])}%, dan \n    rata-rata persentase harga {meanReturn[0]}%\n    B. {group_name_stock[1]} memiliki persentase harga terbesar yaitu {max(group_rate[1])}%, persentase harga terendah yaitu {min(group_rate[1])}%, dan \n    rata-rata persentase harga {meanReturn[1]}%\n    C. {group_name_stock[2]} memiliki persentase harga terbesar yaitu {max(group_rate[2])}%, persentase harga terendah yaitu {min(group_rate[2])}%, dan \n    rata-rata persentase harga {meanReturn[2]}%")
print(f"8. 3 saham tersebut memiliki volatilitas sederhana yang dapat dilihat melalui:\n    A. {group_name_stock[0]} memiliki volatilitas sederhana sebesar {group_high[0]}\n    B. {group_name_stock[1]} memiliki volatilitas sederhana sebesar {group_high[1]}\n    C. {group_name_stock[2]} memiliki volatilitas sederhana sebesar {group_high[2]}")
print(f"9. 3 saham tersebut memiliki jumlah hari yang mengalami peningkatan dan penurunan dengan persentase hari\n    yang mengalami peningkatan yang dapat dilihat melalui:\n    A. {group_name_stock[0]} memiliki jumlah hari yang mengalami peningkatan sebanyak {len(group_positive[0])} \n    hari dan penurunan sebanyak {len(group_negative[0])} hari dengan persentase hari yang mengalami peningkatan sebesar {group_ratio[0]}%\n    B. {group_name_stock[1]} memiliki jumlah hari yang mengalami peningkatan sebanyak {len(group_positive[1])} \n    hari dan penurunan sebanyak {len(group_negative[1])} hari dengan persentase hari yang mengalami peningkatan sebesar {group_ratio[1]}%\n    C. {group_name_stock[2]} memiliki jumlah hari yang mengalami peningkatan sebanyak {len(group_positive[2])} \n    hari dan penurunan sebanyak {len(group_negative[2])} hari dengan persentase hari yang mengalami peningkatan sebesar {group_ratio[2]}%")
for y, name, result in zip(group_index[9:12], group_name_stock[:3], resultVal[:3]):
	print(f"{y}. Berdasarkan laporan, {name} dinilai {result}")

#summary Information

print("<======== Summary Information ========>")

print(f"1. Frekuensi harga dari semua saham: {max(group_total)}")
print(f"2. Harga terendah dari semua saham:\n    A. {group_name_stock[2]}: {group_min[2]}\n    B. {group_name_stock[0]}: {group_min[0]}\n    C. {group_name_stock[1]}: {group_min[1]}")
print(f"3. Harga tertinggi dari semua saham:\n    A. {group_name_stock[2]}: {group_max[2]}\n    B. {group_name_stock[0]}: {group_max[0]}\n    C. {group_name_stock[1]}: {group_max[1]}")
print(f"4. Harga rata-rata dari semua saham:\n    A. {group_name_stock[0]}: {group_mean[0]}\n    B. {group_name_stock[1]}: {group_mean[1]}\n    C. {group_name_stock[2]}: {group_mean[2]}")
print(f"5. Perubahan harga dari semua saham:\n    A. {group_name_stock[0]}: {', '.join(map(str, group_change[0]))}\n    B. {group_name_stock[1]}: {', '.join(map(str, group_change[1]))}\n    C. {group_name_stock[2]}: {', '.join(map(str, group_change[2]))}")
print(f"6. Perubahan persentase harga dari semua saham:\n    A. {group_name_stock[0]}: {', '.join(map(str, group_rate[0]))}\n    B. {group_name_stock[1]}: {', '.join(map(str, group_rate[1]))}\n    C. {group_name_stock[2]}: {', '.join(map(str, group_rate[2]))}")
print(f"7. Persentase harga terbesar, terkecil, dan rata-rata dari semua saham:\n    A. {group_name_stock[0]}:\n         Terbesar: {max(group_rate[0])}%\n         Terkecil: {min(group_rate[0])}%\n         Rata-rata: {meanReturn[0]}%\n    B. {group_name_stock[1]}:\n         Terbesar: {max(group_rate[1])}%\n         Terkecil: {min(group_rate[1])}%\n         Rata-rata: {meanReturn[1]}%\n    C. {group_name_stock[2]}:\n         Terbesar: {max(group_rate[2])}%\n         Terkecil: {min(group_rate[2])}%\n         Rata-rata: {(meanReturn[2])}%")
print(f"8. Volatilitas sederhana dari semua saham:\n    A. {group_name_stock[0]}: {group_high[0]}\n    B. {group_name_stock[1]}: {group_high[1]}\n    C. {group_name_stock[2]}: {group_high[2]}")
print(f"9. Jumlah hari dengan peningkatan dan penurunan serta persentase hari peningkatan dari semua saham:\n    A. {group_name_stock[0]}:\n         Hari dengan peningkatan: {len(group_positive[0])}\n         Hari dengan penurunan: {len(group_negative[0])}\n         Persentase hari peningkatan: {group_ratio[0]}%\n    B. {group_name_stock[1]}:\n         Hari dengan peningkatan: {len(group_positive[1])}\n         Hari dengan penurunan: {len(group_negative[1])}\n         Persentase hari peningkatan: {group_ratio[1]}%\n    C. {group_name_stock[2]}:\n         Hari dengan peningkatan: {len(group_positive[2])}\n         Hari dengan penurunan: {len(group_negative[2])}\n         Persentase hari peningkatan: {group_ratio[2]}%")
print(f"10. Kekuatan dari semua saham:\n       A. {group_name_stock[0]}: {resultVal[0]}\n       B. {group_name_stock[1]}: {resultVal[1]}\n       C. {group_name_stock[2]}: {resultVal[2]}")