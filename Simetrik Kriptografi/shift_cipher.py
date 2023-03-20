# Description: Shift Cipher

# Fungsi untuk mengenkripsi pesan dengan algoritma shift cipher
def encrypt(message, key):
    cipher = ''  # inisialisasi variabel cipher
    for char in message:
        if char.isupper():  # jika karakter saat ini adalah huruf kapital
            cipher += chr((ord(char) - 65 + key) % 26 + 65)  # tambahkan karakter yang telah dienkripsi ke variabel cipher
        elif char.islower():  # jika karakter saat ini adalah huruf kecil
            cipher += chr((ord(char) - 97 + key) % 26 + 97)  # tambahkan karakter yang telah dienkripsi ke variabel cipher
        else:  # jika karakter saat ini bukan huruf
            cipher += char  # tambahkan karakter asli ke variabel cipher
    return cipher

# Fungsi untuk mendekripsi pesan yang telah dienkripsi dengan algoritma shift cipher
def decrypt(cipher, key):
    message = ''  # inisialisasi variabel message
    for char in cipher:
        if char.isupper():  # jika karakter saat ini adalah huruf kapital
            message += chr((ord(char) - 65 - key) % 26 + 65)  # tambahkan karakter yang telah didekripsi ke variabel message
        elif char.islower():  # jika karakter saat ini adalah huruf kecil
            message += chr((ord(char) - 97 - key) % 26 + 97)  # tambahkan karakter yang telah didekripsi ke variabel message
        else:  # jika karakter saat ini bukan huruf
            message += char  # tambahkan karakter asli ke variabel message
    return message

# Fungsi utama
def main():
    print('Aplikasi Shift Cipher')
    message = input('Masukkan pesan: ')  # input pesan
    # NIM L200210062
    # Menggunakan shift 62, dikarenakan 2 Digit terakhir NIM saya adalah 62
    key = 62  # inisialisasi variabel key
    cipher = encrypt(message, key)  # enkripsi pesan
    print('Pesan yang telah dienkripsi: ', cipher)  # cetak pesan yang telah dienkripsi
    print('Pesan yang telah didekripsi: ', decrypt(cipher, key))  # cetak pesan yang telah didekripsi

# Panggil fungsi utama
if __name__ == '__main__': 
    main()