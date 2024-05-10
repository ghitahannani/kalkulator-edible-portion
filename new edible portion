import streamlit as st

#judul aplikasi
st. set_page_config (page_title= 'edibleportion', page_icon=':chicken', layout= 'wide')
st. title('Hai! Kami siap membantu anda! :chicken: :wave:')
st. write('Aplikasi ini merupakan hasil project dari kami, kelompok 9 untuk memenuhi tugas akhir mata kuliah logika pemrograman komputer. Silahkan gulir layar anda kebawah!')

st.subheader('Anggota Kelompok 9', divider='rainbow')
st.write ('
          1. Bunga Sekar Ningrum (2320514)
          2. Delvina Neva Ghita Hannani (2320516)
          3. Dilla Aulia Efendi (2320518)
          4. Gea Veronika Caniago (2320525)
          5. Muhammad Syaukani Akbar (2320538)')

st. markdown(':fish::broccoli::potato::onion::sunflower::apple::fish::broccoli::potato::onion::sunflower::apple::fish:')

st.subheader('Apa Itu Edible Portion', divider='rainbow')
st.write ('Edible portion adalah bagian dari makanan yang dapat dimakan atau dikonsumsi setelah bagian-bagian yang tidak dapat dimakan atau tidak diinginkan telah dihilangkan.')

st.subheader('Manfaat dan Fungsi Mengetahui Edible Portion', divider='rainbow')
st.write ('
          1. Pengelolaan Bahan Baku: Dengan mengetahui berapa persentase dari bahan baku yang sebenarnya dapat dimakan, produsen makanan dapat mengelola persediaan mereka dengan lebih efisien.
          2. Efisiensi Pengolahan: Mengetahui bagian yang dapat dimakan dari bahan mentah memungkinkan produsen makanan untuk mengoptimalkan proses pengolahan dan mengurangi pemborosan.
          3. Perencanaan Menu yang Lebih Sehat: Restoran atau katering yang memahami edible portion dari berbagai bahan makanan dapat merencanakan menu yang lebih sehat dan seimbang nutrisinya.
          4. Pengurangan Pemborosan Makanan: Dengan memahami berapa banyak dari bahan mentah yang sebenarnya dapat dimakan, individu dan bisnis dapat mengurangi pemborosan makanan dengan memanfaatkan sebanyak mungkin dari bahan tersebut.
          5. Manajemen Biaya: Dengan mengetahui berapa banyak dari bahan yang dapat dimakan, perusahaan makanan dan individu dapat mengelola biaya mereka dengan lebih baik dengan menghindari pembelian atau penggunaan bahan yang tidak diperlukan.
          6. Peningkatan Kesadaran Nutrisi: Memahami bagian makanan yang sebenarnya dapat dimakan membantu individu untuk membuat pilihan makanan yang lebih sehat dan memperhitungkan asupan nutrisi mereka dengan lebih baik.')

st. markdown(':fish::broccoli::potato::onion::sunflower::apple::fish::broccoli::potato::onion::sunflower::apple::fish:')

st.title('Kalkulator Edible Portion Pada Bahan Pangan')
st.write ('Aplikasi ini berguna untuk mempermudah menghitung edible portion pada bahan pangan. Silahkan gulir kebawah dan masukkan bobot yang dapat dimakan dari bahan pangan atau sampel (dalam gram) dan bobot utuh bahan pangan atau sampel (dalam gram) pada layar.')

#menghitung edible portion
bobot_yang_dapat_dimakan = st.number_input ('Masukkan bobot yang dapat dimakan pada bahan pangan atau sampel (dalam gram)')
st.write ('bobot yang dapat dimakan pada bahan pangan atau sampel', bobot_yang_dapat_dimakan )

bobot_utuh_bahan = st.number_input ('Masukkan bobot utuh pada bahan pangan atau sampel (dalam gram)')
st.write ('bobot yang utuh pada bahan pangan atau sampel', bobot_utuh_bahan )

hitung_edibleportion = st.button('Hitung Edible Portion')
if hitung_edibleportion:
            perhitungan_edible_portion = bobot_yang_dapat_dimakan / bobot_utuh_bahan * 100
            st. write(f'Nilai edible portion dari bahan pangan atau sampel tersebut adalah, {perhitungan_edible_portion} %')

st.markdown("Terimakasih telah menggunakan aplikasi ini &mdash;\
            :fish::broccoli::potato::onion::sunflower::apple:")
