import streamlit as st  # type: ignore

def konfigurasi_elektron(atomic_number):
    # Dictionary untuk menyimpan jumlah elektron di setiap kulit
    data_konfigurasi = {
    "1": "1s¹",
    "2": "1s²",
    "3": "1s² 2s¹",
    "4": "1s² 2s²",
    "5": "1s² 2s² 2p¹",
    # Tambahkan konfigurasi untuk unsur-unsur lain di sini...
    "118": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d¹⁰ 7p⁶"
}

    # Mengecek apakah nomor atom valid
    if atomic_number not in electron_config: # type: ignore
        return "Nomor atom tidak valid. Masukkan nomor atom antara 1 hingga 118."

    return electron_config[atomic_number] # type: ignore

def main():
    st.title("Aplikasi Konfigurasi Elektron")
    st.write("Aplikasi ini menghasilkan konfigurasi elektron untuk atom dengan nomor atom tertentu.")

    # Membuat input untuk nomor atom
    atomic_number = st.text_input("Masukkan nomor atom (1-18):")

    # Memanggil fungsi konfigurasi_elektron dan menampilkan hasilnya
    if st.button("Tampilkan Konfigurasi Elektron"):
        result = konfigurasi_elektron(atomic_number)
        st.write("Konfigurasi elektron untuk atom dengan nomor atom", atomic_number, "adalah:", result)