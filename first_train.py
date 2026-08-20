Scores = [78, 90, 56, 88, 95, 67, 45, 100, 82, 73]
siswa_lulus = []
siswa_tidak_lulus = []

volume_scores = len(Scores)
max_scores = max(Scores)
min_scores = min(Scores)
avg_scores = sum(Scores)/len(Scores)

print(f"1. Total volume nilai: {
  volume_scores
}")
print(f"2. Nilai skor tertinggi: {max_scores}")
print(f"3. Nilai skor terendah: {min_scores}")
print(f"4. Nilai skor rata-rata: {avg_scores}")

Scores.sort()
for S in Scores:
	if S >= 75:
		siswa_lulus.append(S)
		jumlah_siswa_lulus= len(siswa_lulus)
	else:
		siswa_tidak_lulus.append(S)
		jumlah_siswa_tidak_lulus= len(siswa_tidak_lulus)
		
print(f"5. jumlah siswa lulus: {jumlah_siswa_lulus}")
print(f"6. jumlah siswa tidak lulus: {jumlah_siswa_tidak_lulus}")
print(f"7. Nilai urut siswa menaik: {Scores}")

Scores.reverse()
print(f"8. Nilai urut siswa menurun: {Scores}")

print("9. Keterangan kelulusan siswa:")
Scores.reverse()
for S in Scores:
	if S >= 75:
		print(f"siswa dengan nilai {S} dinyatakan lulus")
	else:
		print(f"siswa dengan nilai {S} dinyatakan tidak lulus")