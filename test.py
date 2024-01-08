def daftar_mahasiswa():
    data_mahasiswa = []

    while True:
        nama = input("Masukkan nama mahasiswa: ")

        if nama == "":
            print("Nama tidak boleh kosong!")
            continue

        npm = input("Masukkan npm mahasiswa: ")
        if npm == "":
            print("NPM tidak boleh kosong!")
            continue

        jurusan = input("Masukkan jurusan mahasiswa: ")
        if jurusan == "":
            print("Jurusan tidak boleh kosong!")
            continue

        mahasiswa = {"nama": nama, "npm": npm, "jurusan": jurusan}
        data_mahasiswa.append(mahasiswa)

        print("Mahasiswa berhasil didaftarkan.")

        kontin = input("Apakah Anda ingin mendaftarkan mahasiswa lain? (Y/N): ").upper()
        if kontin == "N":
            break

    return data_mahasiswa

def lihat_data_mahasiswa(data_mahasiswa):
    if len(data_mahasiswa) == 0:
        print("Belum ada mahasiswa yang terdaftar.")
    else:
        print("\nData Mahasiswa:")
        print("-----------------------------")
        for i in range(len(data_mahasiswa)):
            print(f"{i+1}. {data_mahasiswa[i]['nama']} - {data_mahasiswa[i]['npm']} - {data_mahasiswa[i]['jurusan']}")

def cari_mahasiswa(data_mahasiswa):
    npm_mahasiswa = input("Masukkan npm mahasiswa yang ingin Anda cari: ")

    mahasiswa_ditemukan = False
    for mahasiswa in data_mahasiswa:
        if mahasiswa["npm"] == npm_mahasiswa:
            print("\nData Mahasiswa:")
            print("-----------------------------")
            print(f"Nama: {mahasiswa['nama']}")
            print(f"NPM: {mahasiswa['npm']}")
            print(f"Jurusan: {mahasiswa['jurusan']}")
            mahasiswa_ditemukan = True
            break

    if not mahasiswa_ditemukan:
        print("Mahasiswa dengan npm tersebut tidak ditemukan.")

def menu():
    print("Menu:")
    print("1. Daftar Mahasiswa")
    print("2. Lihat Data Mahasiswa")
    print("3. Cari Mahasiswa")
    print("4. Keluar")


    pilihan = input("Masukkan pilihan Anda: ")

    return pilihan

def main():
    data_mahasiswa = []
    while True:
        menu()
        pilihan = menu()

        if pilihan == "1":
            data_mahasiswa = daftar_mahasiswa()
        elif pilihan == "2":
            lihat_data_mahasiswa(data_mahasiswa)
        elif pilihan == "3":
            cari_mahasiswa(data_mahasiswa)
        elif pilihan == "4":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()