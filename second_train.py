prices = [100, 102, 101, 105, 110, 108]
prices_change = []
prices_return = []
return_positif = []
return_negatif = []

#informasi dasar
jumlahHarga = len(prices)
minHarga = min(prices)
maxHarga = max(prices)
meanHarga = sum(prices)/len(prices)

print(f"1.A. frekuensi harga: {jumlahHarga}")
print(f"1.B. harga terendah: {minHarga}")
print(f"1.C. harga tertinggi: {maxHarga}")
print(f"1.D. harga rata-rata: {meanHarga}")

#daily prices_change
for price in range(len(prices)-1):
	hasil= prices[price+1]-prices[price]
	prices_change.append(hasil)

print(f"2. Daftar perubahan harga dalam 6 hari: {prices_change}")

#daily prices_return
for i in range(5):
	persentase= round((prices_change[i]/prices[i])*100, 2)
	prices_return.append(persentase)

print(f"3. Daftar perubahan persentase return dalam 6 hari: {prices_return}")

#persentase terbesar
maxReturn = max(prices_return)
print(f"4. Persentase return terbesar dalam 6 hari: {maxReturn}")

#persentase terendah
minReturn= min(prices_return)
print(f"5. Persentase return terendah dalam 6 hari: {minReturn}")

#frekuensi positif dan negatif
for rate in prices_return:
	if rate >= 0:
		return_positif.append(rate)
		frekuensi_positif= len(return_positif)
	else:
		return_negatif.append(rate)
		frekuensi_negatif= len(return_negatif)

print(f"6. frekuensi return positif dalam 6 hari sebanyak {frekuensi_positif} kali")
print(f"7. frekuensi return negatif dalam 6 hari sebanyak {frekuensi_negatif} kali")

#persentase harian naik
hariKenaikan = (frekuensi_positif/len(prices_return))*100

print(f"8. frekuensi hari dengan kenaikan harga yaitu sebanyak {hariKenaikan}%")