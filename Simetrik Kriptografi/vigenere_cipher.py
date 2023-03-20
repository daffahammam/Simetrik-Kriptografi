# Description: Vigenere Chiper

# Fungsi untuk mengenkripsi pesan dengan algoritma Vigenere Cipher
def encrypt(message, key):
    encrypted_message = ''  # Inisialisasi variabel yang akan menampung pesan terenkripsi
    for i in range(len(message)):
        char = message[i]  # Mengakses karakter pada pesan yang akan dienkripsi
        key_char = key[i % len(key)]  # Mengakses karakter pada kunci yang sesuai dengan karakter pesan

        if char.isalpha():  # Memeriksa apakah karakter pada pesan adalah huruf
            char_num = ord(char.upper()) - 65  # Menghitung nilai numerik dari karakter pesan
            key_num = ord(key_char.upper()) - 65  # Menghitung nilai numerik dari karakter kunci

            encrypted_num = (char_num + key_num) % 26  # Menghitung nilai numerik dari karakter yang dienkripsi
            encrypted_char = chr(encrypted_num + 65)  # Mengonversi nilai numerik kembali menjadi karakter

            if char.isupper():  # Memeriksa apakah karakter pada pesan adalah huruf kapital
                encrypted_message += encrypted_char  # Menambahkan karakter terenkripsi ke pesan terenkripsi
            else:
                encrypted_message += encrypted_char.lower()  # Menambahkan karakter terenkripsi ke pesan terenkripsi dalam huruf kecil
        else:
            encrypted_message += char  # Menambahkan karakter yang bukan huruf ke pesan terenkripsi

    return encrypted_message  # Mengembalikan pesan terenkripsi

# Fungsi untuk mendekripsi pesan yang telah dienkripsi dengan algoritma Vigenere Cipher
def decrypt(ciphertext, key):
    decrypted_message = ''  # Inisialisasi variabel yang akan menampung pesan terdekripsi
    for i in range(len(ciphertext)):
        char = ciphertext[i]  # Mengakses karakter pada pesan terenkripsi
        key_char = key[i % len(key)]  # Mengakses karakter pada kunci yang sesuai dengan karakter pesan

        if char.isalpha():  # Memeriksa apakah karakter pada pesan terenkripsi adalah huruf
            char_num = ord(char.upper()) - 65  # Menghitung nilai numerik dari karakter pesan terenkripsi
            key_num = ord(key_char.upper()) - 65  # Menghitung nilai numerik dari karakter kunci

            decrypted_num = (char_num - key_num) % 26  # Menghitung nilai numerik dari karakter yang didekripsi
            decrypted_char = chr(decrypted_num + 65)  # Mengonversi nilai numerik kembali menjadi karakter

            if char.isupper():  # Memeriksa apakah karakter pada pesan terenkripsi adalah huruf kapital
                decrypted_message += decrypted_char  # Menambahkan karakter terdekripsi ke pesan terdekripsi
            else:
                decrypted_message += decrypted_char.lower()  # Menambahkan karakter terdekripsi ke pesan terdekripsi dalam huruf kecil
        else:
            decrypted_message += char  # Menambahkan karakter yang bukan huruf ke pesan terdekripsi

    return decrypted_message  # Mengembalikan pesan terdekripsi

# Fungsi utama
def main():
    print('Aplikasi Vigenere Cipher')
    message = input('Masukkan pesan: ')  # Input pesan
    # NIM L200210062
    # Menggunakan key 062, dikarenakan 3 Digit terakhir NIM saya adalah 062
    key = '062'  # Inisialisasi variabel key
    ciphertext = encrypt(message, key)  # Enkripsi pesan
    print('Pesan yang telah dienkripsi: ', ciphertext)  # Cetak pesan yang telah dienkripsi
    print('Pesan yang telah didekripsi: ', decrypt(ciphertext, key))  # Cetak pesan yang telah didekripsi

# Panggil fungsi utama
if __name__ == '__main__':
    main()