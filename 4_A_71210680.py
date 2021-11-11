print("=====MASUKAN JUMLAH MAKANAN YANG DIPESAN=====\n")
i_b = int(input("IKAN BAKAR      RP 25.000,00    : "))
e_d = int(input("ES DOGER      RP 6.000,00    : "))
r_c = int(input("RUJAK CINGUR      RP 8.000,00    : "))

total_i_b = i_b * 25000
total_e_d = e_d * 6000
total_r_c = r_c * 8000
total_b = total_i_b + total_e_d + total_r_c

print("=====TOTAL=====\n")
print("TOTAL IKAN BAKAR     : Rp ", total_i_b, "\n")
print("TOTAL ES DOGER     : Rp ", total_e_d, "\n")
print("TOTAL RUJAK CINGUR     : Rp ", total_r_c, "\n")
print("Jumlah total biaya yang harus dibayar adalah Rp ", total_b)