from random import randint
ans = randint(1, 100)
skor = 100
jwb = 'K'
print()

while(jwb != ans):
  if(jwb == 'K'):
    print("============== Permainan Tebak Bilangan ==============")
    print()
    print("Komputer telah memilih bilangan bulat dari 1 sampai 100 secara acak. Sekarang tugas kamu adalah menebaknya!")
    print()
    print("======================================================")
    print()
  elif(jwb < ans):
    print("Bilangan tebakan kamu terlalu kecil!")
    skor -= 2
  elif(jwb > ans):
    print("Bilangan tebakan kamu terlalu besar!")
    skor -= 2
  
  jwb = int(input("Masukkan angka tebakan kamu : "))
  print()

print("Selamat! Tebakan kamu benar!")
print("Skor kamu : "+str(skor))
