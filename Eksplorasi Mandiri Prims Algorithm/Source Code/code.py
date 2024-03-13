# Mendefinisikan graf sebagai kamus yang berisi daftar terhubung
graf = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

# Mencari sisi minimum dalam daftar sisi
def cari_sisi_minimum(sisi):
    sisi_minimum = None
    bobot_minimum = float('inf')
    for v, bobot in sisi.items():
        if bobot < bobot_minimum:
            sisi_minimum = v
            bobot_minimum = bobot
    return sisi_minimum, bobot_minimum

# Mencari pohon rentang minimum menggunakan algoritma Prim
def prim(graf):
    # Menginisialisasi sebuah himpunan kosong untuk menyimpan simpul-simpul dalam MST
    mst = set()

    # Memilih simpul pertama untuk memulai pohon
    simpul_awal = next(iter(graf))
    mst.add(simpul_awal)

    # Menginisialisasi kamus sisi yang akan dipertimbangkan
    sisi = graf[simpul_awal]

    # Iterasi melalui graf hingga semua simpul berada dalam MST
    while len(mst) < len(graf):
        # Mencari sisi minimum dalam kamus sisi
        sisi_minimum, bobot_minimum = cari_sisi_minimum(sisi)

        # Menambahkan simpul ke MST
        mst.add(sisi_minimum)

        # Menambahkan sisi yang terhubung ke simpul ke kamus sisi yang akan dipertimbangkan
        for v, bobot in graf[sisi_minimum].items():
            if v not in mst:
                sisi[v] = bobot

        # Menghapus sisi minimum dari kamus sisi yang akan dipertimbangkan
        del sisi[sisi_minimum]

    # Mengembalikan MST sebagai daftar
    return list(mst)

# Memanggil fungsi prim dengan graf
pohon_rentang_minimum = prim(graf)

# Menampilkan hasil ke layar
print("Pohon Rentang Minimum:", pohon_rentang_minimum)
