print('Tipe data list / array / daftar')
anak = ['Eka', 'Dwi', 'Tri', 'Catur']
print(anak)
anak.append('Limo')
print(anak)

print('\nSapa anak ke 2')
print(f'Hai {anak[1]}!')

print('\nSapa semua anak')
for nama_anak in anak:
    print(f'Hai {nama_anak}!')

print('\nSapa semua anak: cara ribet')
for i in range(0, len(anak)):
    print(f'{i+1}. Hai {anak[i]}!')