# Fungsi untuk konversi suhu dari Celsius ke Fahrenheit
def celsius_ke_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Fungsi untuk konversi suhu dari Fahrenheit ke Celsius
def fahrenheit_ke_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Fungsi untuk konversi suhu dari Celsius ke Kelvin
def celsius_ke_kelvin(celsius):
    return celsius + 273.15

# Fungsi untuk konversi suhu dari Kelvin ke Celsius
def kelvin_ke_celsius(kelvin):
    return kelvin - 273.15

# Fungsi untuk konversi suhu dari Fahrenheit ke Kelvin
def fahrenheit_ke_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

# Fungsi untuk konversi suhu dari Kelvin ke Fahrenheit
def kelvin_ke_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Fungsi untuk menampilkan menu pilihan konversi suhu
def menu_konversi():
    print("\nPilih jenis konversi suhu:")
    print("1. Celsius ke Fahrenheit")
    print("2. Fahrenheit ke Celsius")
    print("3. Celsius ke Kelvin")
    print("4. Kelvin ke Celsius")
    print("5. Fahrenheit ke Kelvin")
    print("6. Kelvin ke Fahrenheit")
    print("7. Keluar")  # Opsi untuk keluar dari program

# Loop utama, terus berjalan sampai user pilih keluar
while True:
    menu_konversi()  # Tampilkan menu
    pilihan = input("Masukkan pilihan (1/2/3/4/5/6/7): ")

    # Kalau pilihannya valid, minta suhu dan lakukan konversi
    if pilihan in ['1', '2', '3', '4', '5', '6']:
        suhu = float(input("Masukkan suhu yang ingin dikonversi: "))
        
        # Sesuaikan dengan pilihan yang dipilih dan tampilkan hasil konversinya
        if pilihan == '1':
            print(f"{suhu} Celsius = {celsius_ke_fahrenheit(suhu)} Fahrenheit")
        elif pilihan == '2':
            print(f"{suhu} Fahrenheit = {fahrenheit_ke_celsius(suhu)} Celsius")
        elif pilihan == '3':
            print(f"{suhu} Celsius = {celsius_ke_kelvin(suhu)} Kelvin")
        elif pilihan == '4':
            print(f"{suhu} Kelvin = {kelvin_ke_celsius(suhu)} Celsius")
        elif pilihan == '5':
            print(f"{suhu} Fahrenheit = {fahrenheit_ke_kelvin(suhu)} Kelvin")
        elif pilihan == '6':
            print(f"{suhu} Kelvin = {kelvin_ke_fahrenheit(suhu)} Fahrenheit")
    # Kalau user pilih untuk keluar, program berhenti
    elif pilihan == '7':
        print("Terima kasih sudah menggunakan program konversi suhu! :)")
        break  # Keluar dari loop dan program selesai
    else:
        # Kalau pilihannya gak valid, kasih tau user dan minta pilih lagi
        print("Pilihan tidak valid. Silakan coba lagi.")
