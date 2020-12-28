# Pembeli ingin membeli 
# Saat uang tidak cukup, buat control flow untuk pinjam uang
# Berikan total hutang pada akhir program

buah = {'Apel':2000, 'Ceri':4000, 'Pisang':4500, 'Semangka':7000}
uang = 70000

print('=== Selamat Datang di toko ===')
print('=== Selamat Berbelanja ===')
print('*** Kamu punya uang Rp.',  str(uang), '***')

for i in buah:
    permintaan = input('Mau beli ' + i +  ' berapa biji? : ')
    print('Kamu akan membeli', permintaan, i, 'biji' )

    uangku = int(permintaan)
    total = buah[i] * uangku
    print('Harga total pembelian : Rp. ', str(total))

    if uang >= total:
        print('Anda telah membeli', permintaan, i)
        uang -= total
    elif uang <= total:
        bc = input('Uang anda habis, mau pinjam uang ? Ya/Tidak :')
        if bc == 'Ya':
            b = int(input('Rupiah :'))
            uang += b          
    else:
        print('Uang anda tidak cukup')
        print('Anda tidak dapat membeli ', i, ' sebanyak itu')

    print('==========================')
    print('*** Sisa uang kamu Rp.',  str(uang), '***')

print('Uang anda tersisa Rp. ', str(uang))
