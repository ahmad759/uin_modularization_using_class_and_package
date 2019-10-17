nama = 'ahmad'

print(f'author = {nama}')

def hitung_luas (panjang,lebar):
    luas = panjang*lebar
    print (f'luas bangunan adalah {luas}m^2')
    return luas

luas = hitung_luas (5,15)

def hitung_tinggi (roof,floor):
    tinggi = roof-floor
    print (f'tinggi bangunan adalah {tinggi}m ')
    return tinggi

tinggi = hitung_tinggi (12,0)

def hitung_volume (luas,tinggi):
    volume = luas*tinggi
    print (f'volume bangunan adalah {volume}m^3')
    return volume

volume = hitung_volume (luas,tinggi)
