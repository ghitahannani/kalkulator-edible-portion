import streamlit as st

#judul aplikasi
st. set_page_config (page_title= 'edibleportion', page_icon=':chicken', layout= 'wide')
st. title('Hai! Kami siap membantu anda! :chicken: :wave:')
st. write('Aplikasi ini merupakan hasil project dari kami, kelompok 9 untuk memenuhi tugas akhir mata kuliah logika pemrograman komputer. Silahkan gulir layar anda kebawah!')

st. markdown(':fish::broccoli::potato::onion::sunflower::apple::fish::broccoli::potato::onion::sunflower::apple::fish::broccoli::potato::onion::sunflower::apple::fish::broccoli::potato::onion::sunflower::apple::fish::broccoli::potato::onion::sunflower::apple::fish::broccoli::potato::onion::sunflower::apple::fish::broccoli::potato::onion::sunflower::apple::fish::broccoli::potato::onion:')

st.title('Kalkulator Edible Portion Pada Bahan Pangan')
st.write ('Aplikasi ini berguna untuk mempermudah menghitung edible portion pada bahan pangan. Silahkan gulir kebawah dan masukkan bobot yang dapat dimakan dari bahan pangan atau sampel (dalam gram) dan bobot utuh bahan pangan atau sampel (dalam gram) pada layar.')

#menghitung edible portion
bobot_yang_dapat_dimakan = st.number_input ('Masukkan bobot yang dapat dimakan pada bahan pangan atau sampel (dalam gram)')
st.write ('bobot yang dapat dimakan pada bahan pangan atau sampel', bobot_yang_dapat_dimakan )

bobot_utuh_bahan = st.number_input ('Masukkan bobot utuh pada bahan pangan atau sampel (dalam gram)')
st.write ('bobot yang utuh pada bahan pangan atau sampel', bobot_utuh_bahan )

perhitungan_edible_portion = bobot_yang_dapat_dimakan / bobot_utuh_bahan * 100
st.warning('Silahkan masukkan angka selain angka 0.')

st.button ('hitung')

st. write ('Nilai edible portion dari bahan pangan atau sampel tersebut adalah (%)', perhitungan_edible_portion)

st.markdown("Terimakasih telah menggunakan aplikasi ini &mdash;\
            :fish::broccoli::potato::onion::sunflower::apple:")