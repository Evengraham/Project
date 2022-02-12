list_karyawan = [
    ['Andi', 22, 17012,'Design', 15000000],
    ['Budi', 23, 16015,'IT', 12500000],
    ['Cindi', 23, 15020, 'Sales', 14000000]
]

cart = []


while True:
    Daftar_karyawan = input('''
        ===============Daftar Data Karyawan Perusahaan===============

        List Menu:
        1. Laporan data karyawan
        2. Menambahkan data karyawan
        3. Menghapus data karyawan
        4. Mengubah data karyawan
        5. Exit

        Masukkan angka menu yang ingin dijalankan: ''')

    if(Daftar_karyawan == '1'):

        print('Laporan_karyawan\n')
        print('Index\t| Nama  \t| Umur\t| No ID\t| Jobdesk      \t| Gaji')
        
        for i in range(len(list_karyawan)):
            print(f'{i}\t| {list_karyawan[i][0]}  \t| {list_karyawan[i][1]}\t| {list_karyawan[i][2]}\t| {list_karyawan[i][3]}       \t| {list_karyawan[i][4]}')
    
    
    elif(Daftar_karyawan == '2'):

        Nama = input('Masukkan nama anda: ')
        Umur = int(input('Masukkan umur anda: '))
        No_ID = int(input('Masukkan No ID karyawan anda: '))
        Jobdesk = input('Masukan Jobdesk anda: ')
        Gaji = int(input('Masukan Gaji anda: '))
        
        list_karyawan.append([Nama, Umur, No_ID, Jobdesk, Gaji])
        
        print('Laporan_karyawan\n')
        print('Index\t| Nama  \t| Umur\t| No ID\t| Jobdesk      \t| Gaji')
        
        for i in range(len(list_karyawan)):
            print(f'{i}\t| {list_karyawan[i][0]}  \t| {list_karyawan[i][1]}\t| {list_karyawan[i][2]}\t| {list_karyawan[i][3]}       \t| {list_karyawan[i][4]}')

    elif(Daftar_karyawan == '3'):

        print('Laporan_karyawan\n')
        print('Index\t| Nama  \t| Umur\t| No ID\t| Jobdesk      \t| Gaji')
        
        for i in range(len(list_karyawan)):
            print(f'{i}\t| {list_karyawan[i][0]}  \t| {list_karyawan[i][1]}\t| {list_karyawan[i][2]}\t| {list_karyawan[i][3]}       \t| {list_karyawan[i][4]}')

        index_karyawan = int(input('Masukkan index data karyawan yang ingin dihapus: '))
        
        del list_karyawan[index_karyawan]

        print('Laporan_karyawan\n')
        print('Index\t| Nama  \t| Umur\t| No ID\t| Jobdesk      \t| Gaji')
        
        for i in range(len(list_karyawan)):
            print(f'{i}\t| {list_karyawan[i][0]}  \t| {list_karyawan[i][1]}\t| {list_karyawan[i][2]}\t| {list_karyawan[i][3]}       \t| {list_karyawan[i][4]}')

    elif(Daftar_karyawan == '4'):

        print('Laporan Karyawan\n')
        print('Index\t| Nama  \t| Umur\t| No ID\t| Jobdesk      \t| Gaji')

        for i in range(len(list_karyawan)):
            print(f'{i}\t| {list_karyawan[i][0]}  \t| {list_karyawan[i][1]}\t| {list_karyawan[i][2]}\t| {list_karyawan[i][3]}       \t| {list_karyawan[i][4]}')
    
        index_karyawan = int(input('Masukkan index data karyawan yang ingin di update: '))
        
        Nama = input('Masukkan nama anda: ')
        Umur = int(input('Masukkan umur anda: '))
        No_ID = int(input('Masukkan No ID karyawan anda: '))
        Jobdesk = input('Masukan Jobdesk anda: ')
        Gaji = int(input('Masukan Gaji anda: '))
        
        list_karyawan[index_karyawan]=[Nama,Umur,No_ID,Jobdesk,Gaji]
        
        print('Laporan Karyawan\n')
        print('Index\t| Nama  \t| Umur\t| No ID\t| Jobdesk      \t| Gaji')

        for i in range(len(list_karyawan)):
            print(f'{i}\t| {list_karyawan[i][0]}  \t| {list_karyawan[i][1]}\t| {list_karyawan[i][2]}\t| {list_karyawan[i][3]}       \t| {list_karyawan[i][4]}')
    else:
        break
print('==========Terima Kasih, Selamat beraktivitas==========')