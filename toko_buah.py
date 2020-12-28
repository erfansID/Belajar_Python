# Pembeli ingin membeli 
# Saat uang tidak cukup, buat control flow untuk pinjam uang
# Berikan total hutang pada akhir program

buah = {'Apel':2000, 'Ceri':4000, 'Pisang':4500, 'Semangka':7000}
uang = 70000
utang = 0
is_ngutang = False

print('=== Selamat Datang di toko ===')
print('=== Selamat Berbelanja ===')
print('*** Kamu punya uang Rp. {} ***'.format(uang))

for i in buah:
    permintaan = input('Mau beli {} berapa biji? : '.format(i))
    print('Kamu akan membeli {} {} biji'.format(permintaan, i))

    uangku = int(permintaan)
    total = buah[i] * uangku
    print('Harga total pembelian : Rp. ', str(total))

    if uang >= total:
        print('Anda telah membeli', permintaan, i)
        uang -= total
    elif uang <= total:
        if not is_ngutang:
            bc = input('Uang anda habis, mau pinjam uang ? Ya/Tidak :')
            if bc == 'Ya':
                b = int(input('Rupiah :'))
                utang += b
                uang += b         
                is_ngutang = True 
    else:
        print('Uang anda tidak cukup')
        print('Anda tidak dapat membeli ', i, ' sebanyak itu')

    print('==========================')
    print('*** Sisa uang kamu Rp.',  str(uang), '***')

print('Uang anda tersisa Rp. ', str(uang))
