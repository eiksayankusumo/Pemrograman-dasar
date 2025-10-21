Nilai_anda = int(input("Masukkan Nilai Anda [0-100] : ")) 


if Nilai_anda >= 80 and Nilai_anda <= 100:
    predikat = "A"
elif Nilai_anda >= 70 and Nilai_anda < 79:
    predikat = "B"
elif Nilai_anda >= 60 and Nilai_anda < 69:
    predikat = "C"
elif Nilai_anda >= 31 and Nilai_anda < 59:
    predikat = "D"
else:
    if Nilai_anda >= 0 and Nilai_anda <= 30:
        predikat = "E"  

print("---------------------------------")
print("Nilai anda : "+str(Nilai_anda)) 
print(predikat)
