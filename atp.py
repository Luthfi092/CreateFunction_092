#input
suhu = float(input("inputkan besaran suhu.upper :"))
format_suhu = input("format suhu (c,f,k) :")
konversi_suhu = input("konversi suhu(c,f,k) :")
hasil = ""

#proses


#x = suhu
#y = fromat suhu
#z konversi suhu
def konversiSuhu(x, y, z) :
    global hasil
    #cek kondisi untuk celcius ke farenheit
    if format == 'c' and z == 'f' :
        f = (9/5) * x + 32
        hasil = f'{f}{z.upper()}'
    #cek kondisi untuk celcius ke kelvin
    if format == 'c' and z == 'k' :
        k = x + 273,15
        hasil = f'{k}{z.upper()}'
    if y == 'f' and z == 'c' :
        c = (x - 32) * (5/9)
        hasil = f'{c}{z.upper()}' 
    if y == 'f' and z == 'k' :
       k = (5/9) * x + 459.67
       hasil = f'{k}{z.upper()}'
    elif y == 'k' and z == 'c' :
       c =  x - 273,15
    elif y == 'f' and z == 'f' :
        f = (x - 273,15) * (9/5) + 32
        hasil = f'{f}{z.upper()}'
    else :
        hasil = "konversi nilai tidak valid"

if(format_suhu == z) :
    hasil = f'{suhu} {format_suhu}'
else :
    konversiSuhu(suhu, format_suhu, konversi_suhu)

    
   
#output
print(hasil)