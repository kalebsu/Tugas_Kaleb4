list_nama = []
list_nim = []
list_tugas = []
list_uts =[]
list_uas = []
list_akhir = []

print("DAFTAR NILAI")
nama = input("Masukkan Nama : ")
nim = input("Masukkan NIM : ")
tugas = input("Masukkan Nilai Tugas : ")
uts = input("Masukkan Nilai UTS : ")
uas = input("Masukkan Nilai UAS : ")
akhir = (int(tugas)* .30) + (int(uts)* .35) + (int(uas)* .35)
print("Akhir:", akhir)

tambah='y', 't'
while(True):
    tambah=input("Tambah Data?(y/t):")
    if tambah=='y':
        nama = input("Masukkan Nama : ")
        nim = input("Masukkan NIM : ")
        tugas = input("Masukkan Nilai Tugas : ")
        uts = input("Masukkan Nilai UTS : ")
        uas = input("Masukkan Nilai UAS : ")
        akhir = (int(tugas)* .30) + (int(uts)* .35) + (int(uas)* .35)
        print("Akhir :", akhir)
    
    if tambah=='t':
        print("================================================================================================================")
        print("|                                DAFTAR NILAI TERSIMPAN                                                         |")
        print("================================================================================================================")
        print("|\tNo\t|\tNama\t|\tNIM\t|\tTugas\t|\tUTS\t|\tUAS\t|\tAKHIR\t|")
        print("================================================================================================================")
        print("|\t1\t|\tAri\t|\t1234\t|\t70\t|\t65\t|\t80\t|\t71.75\t|")
        print("|\t2\t|\tBambang\t|\t2345\t|\t65\t|\t80\t|\t90\t|\t79.0\t|")
        print("================================================================================================================")
