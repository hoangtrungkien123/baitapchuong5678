#bai1.1
print("**  ** ****** **    **     *****")
print("**  ** **     **    **    **   **")
print("****** *****  **    **    **   **")
print("**  ** **     **    **    **   **")
print("**  ** ****** ***** *****  *****")

#bai1.2
x=10
y=5
tong=x+y
hieu=x-y
tich=x*y
thuong=x/y
print("tong cua 2 so la" ,tong)
print("hieu cua 2 so la",hieu)
print("tich cua 2 so la",tich)
print("thuong cua 2 so la",thuong)

#bai1.3
ten_hang="sua hop vinamilk"
so_luong=5
don_gia=25000
tien_phai_tra=so_luong*don_gia
print("Ten hang:",ten_hang)
print("So luong:",so_luong)
print("Don gia:",don_gia)
print("So tien phai tra:",tien_phai_tra)

#bai1.4
x=(5-3)//2
print(x)
y=8-(3*2)-(1+1)
print(y)

#bai1.5
So_luong=100
Don_gia=5000
Thanh_tien=So_luong*Don_gia
print("So tien phai thanh toan la:",Thanh_tien)

#1.6
alice_candies=121
bob_candies=77
carol_candies=109
to_smash=(alice_candies+bob_candies+carol_candies)%3
print("So keo phai dap la:",to_smash)

#1,8
s1="hello"
s2="Python"
s3="programming language"
index=s1.index()
print("Chieu dai chuoi ki tu s1 la",len(s1))
print("Chieu dai chuoi ki tu s2 la",len(s2))
print("Chieu dai chuoi ki tu s3 la",len(s3))
print(s2*2)
print("s4",s1[2,5])      

#1.9
import math
so_tien_gui=10000000
so_thang_gui=6
lai_suat_1_nam=7,6/100/12
tien_lai=so_tien_gui*so_thang_gui*lai_suat_1_nam
tong_so_tien=so_tien_gui*tien_lai
print("Lai suat 1 nam",lai_suat_1_nam)
print("So tien gui",so_tien_gui)
print("So thang gui",so_thang_gui)
print("Tien lai sau 1 nam la",tien_lai)
print("tien von va lai sau 1 nam la",tong_so_tien)

#1.7
c=float(input("nhap do C"))
f=(1,8*c)+32
print(c , "tuong ung voi", f ,"do F")