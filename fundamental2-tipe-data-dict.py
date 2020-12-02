""""
    ini comment
    multiline
    Tipe Data Dictionary : Key -> Value
"""

kamus_ind_eng = {'anak': 'son', 'ibu': 'mom', 'ayah': 'dad', 'istri': 'wife'}
"""
    kamus_ind_eng = {}
    kamus_ind_eng['anak'] = 'son'
    kamus_ind_eng['ibu'] = 'mom'
    kamus_ind_eng['ayah'] = 'dad'
    kamus_ind_eng['istri'] = 'wife'
"""

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])
print(kamus_ind_eng['istri'])

print('Data ini dikirimkan oleh server Gojek, untuk memberikan info driver disekitar pemakai App')
data_gojek = {
    'tanggal': '2020-12-02',
    'driver_list': [
        {'nama': 'Eka', 'jarak': 10},
        {'nama': 'Dwi', 'jarak': 15},
        {'nama': 'Tri', 'jarak': 20},
        {'nama': 'Catur', 'jarak': 25}
    ]
}
print(data_gojek)
print(f"Driver disekitar sini adalah {data_gojek['driver_list']}")
print(f"Driver #1 {data_gojek['driver_list'][0]['nama']}")
print(f"Driver #1 {data_gojek['driver_list'][3]['nama']}")
print(f'Jarak Driver #1 {data_gojek["driver_list"][0]["jarak"]} meter')
