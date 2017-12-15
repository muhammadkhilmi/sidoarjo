#Program Aplikasi Kalkulasi Gaji
print("^^^^^^^^^^^^^^^^^^^^^^^^^")
print("Program Kalkulasi Gaji")
print("^^^^^^^^^^^^^^^^^^^^^^^^^")
print
print("Pilih jabatan")
print
print("1.Direktur")
print("2.Manager")
print("3.Karyawan")
print("4.OB")
print("5.Exit")
print("^^^^^^^^^^^^^^^^^^^^^^^^^")
pilih=int(input("Masukan pilihan anda : "))
print("^^^^^^^^^^^^^^^^^^^^^^^^^")
if pilih == 1:
	print("")
print("kalkulasi gaji direktur")
gaji=3000000
tunjangan=0.25*gaji
PPN=0.1*gaji
total(gaji+tunjangan)-PPN
print("==========================")
print("Gaji pokok :",gaji)
print("tunjangan:",tunjangan)
print("pajak penghasilan:",PPN)
print("___________________________")
print("Total Gaji Direktur :","RP",total)
print("==========================")

elif pilih ==2:
print("")
print("Kalkulasi gaji manager")
gaji=2000000
tunjangan=0.125*gaji
PPN=0.1*gaji
total=(gaji+tunjangan)-PPN
print("==========================")
print("Gaji pokok :",gaji)
print("tunjangan:",tunjangan)
print("pajak penghasilan:",PPN)
print("___________________________")
print("Total Gaji Manager :","RP",total)
print("==========================")
elif pilih ==3:
print("")
print("kalkulasi gaji karyawan")
gaji=1000000
tunjangan=0.16*gaji
PPN=0.1*gaji
total(gaji+tunjangan)-PPN
print("==========================")
print("Gaji pokok :",gaji)
print("tunjangan:",tunjangan)
print("pajak penghasilan:",PPN)
print("___________________________")
print("Total Gaji Karyawan :","RP",total)
print("==========================")
elif pilih ==4:
print("")
print("kalkulasi gaji OB")
gaji=800000
tunjangan=0.16*gaji
PPN=0.1*gaji
total(gaji+tunjangan)-PPN
print("==========================")
print("Gaji pokok :",gaji)
print("tunjangan:",tunjangan)
print("pajak penghasilan:",PPN)
print("___________________________")
print("Total Gaji OB :","RP",total)
print("==========================")
elif pilih ==5:
print("terima kasih telah menggunakan program kalkulasi gaji ini!:")
else:
print("nomor yang anda input,salah!")