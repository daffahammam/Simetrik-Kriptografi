# Description: Substitution Cipher

import string # untuk mengakses string.ascii_uppercase
import random # untuk mengakses fungsi random.shuffle

# Fungsi untuk mengenkripsi pesan dengan algoritma substitusi cipher
def encrypt(plaintext):
    # Daftar huruf alfabet
    alphabet = list(string.ascii_uppercase)
    # Acak urutan huruf alfabet
    random.shuffle(alphabet)
    # Buat kamus substitusi
    substitution_map = {}
    for i in range(26):
        substitution_map[alphabet[i]] = string.ascii_uppercase[i]
    # Inisialisasi variabel yang akan menampung pesan terenkripsi
    ciphertext = ''
    # Enkripsi setiap karakter pada pesan
    for char in plaintext:
        if char.isalpha(): # jika karakter merupakan huruf alfabet
            ciphertext += substitution_map[char.upper()] # tambahkan karakter yang telah dienkripsi ke variabel ciphertext
        else: # jika karakter bukan huruf alfabet
            ciphertext += char # tambahkan karakter ke variabel ciphertext

    return ciphertext, substitution_map

# Fungsi untuk mendekripsi pesan yang telah dienkripsi dengan algoritma substitusi cipher
def decrypt(ciphertext, substitution_map):
    # Inisialisasi variabel yang akan menampung pesan terdekripsi
    decrypted_message = ''
    # Dekripsi setiap karakter pada pesan
    for char in ciphertext:
        if char.isalpha(): # jika karakter merupakan huruf alfabet
            for key, value in substitution_map.items(): # cari karakter yang telah dienkripsi pada kamus substitusi
                if char.upper() == value: # jika karakter yang telah dienkripsi ditemukan
                    decrypted_message += key # tambahkan karakter yang telah didekripsi ke variabel decrypted_message
        else: # jika karakter bukan huruf alfabet
            decrypted_message += char # tambahkan karakter ke variabel decrypted_message

    return decrypted_message

# Fungsi utama
def main():
    print('Aplikasi Substitution Cipher')
    plaintext = input('Masukkan teks: ')  # Input teks
    ciphertext, substitution_map = encrypt(plaintext)  # Enkripsi teks
    print('Teks yang telah dienkripsi: ', ciphertext)  # Cetak teks yang telah dienkripsi
    print('Teks yang telah didekripsi: ', decrypt(ciphertext, substitution_map))  # Cetak teks yang telah didekripsi

# Panggil fungsi utama
if __name__ == '__main__':
    main()