a=2
b=30


daftar_bil= [i for i in range(int(a), int(b) +1 )]
print('Daftar bilangan: {}'.format(daftar_bil))
 
bil_genap = []
bil_ganjil = []
 
for bil in daftar_bil:
    if bil % 2 == 0:
        bil_genap.append(bil)
    else:
        bil_ganjil.append(bil)
 
print('genap: {}'.format(' '.join([str(bil) for bil in bil_genap])))
print('ganjil: {}'.format(' '.join([str(bil) for bil in bil_ganjil])))