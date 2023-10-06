import streamlit as st
import eda
import prediction


page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Model Prediksi'])

if page == 'Home Page':
    st.header('Welcome Page') 
    st.write('')
    st.write('Milestone 2')
    st.write('Nama      : Aditya Pramana Putra')
    st.write('Batch     : HCK-007')
    st.write('Tujuan Milestone    : Tujuan projek ini adalah untuk membuat model prediksi pasien yang normal dan terkena kanker payudarah di RS.IDA KARTINI.')
    st.write('')
    st.caption('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')
    st.write('')
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('Kanker payudara adalah kanker yang paling umum terjadi pada wanita di dunia. Penyakit ini menyumbang 25% dari seluruh kasus kanker, dan mempengaruhi lebih dari 2,1 Juta orang pada tahun 2015 saja. Ini dimulai ketika sel-sel di payudara mulai tumbuh di luar kendali. Sel-sel ini biasanya membentuk tumor yang terlihat melalui X-ray atau dirasakan sebagai benjolan di area payudara.Tantangan utama dalam pendeteksiannya adalah bagaimana mengklasifikasikan tumor menjadi ganas (kanker) atau jinak (non-kanker). Kami meminta Anda menyelesaikan analisis klasifikasi tumor ini menggunakan pembelajaran mesin dan Kumpulan Data Kanker Payudara Wisconsin (Diagnostik)."Objektif dari proyek ini adalah untuk mengembangkan model klasifikasi tumor payudara menggunakan pembelajaran mesin yang dapat mencapai akurasi pengklasifikasian di atas 95% pada dataset pengujian dalam waktu 6 bulan. Model ini akan membantu dalam diagnosis dini kanker payudara dan akan disiapkan untuk integrasi klinis dalam waktu 1 tahun."')

    with st.expander("Problem Statement"):
            st.caption('Problem Statement : Tujuan dari proyek ini adalah untuk mengembangkan model pembelajaran mesin yang dapat mengklasifikasikan tumor payudara menjadi ganas (kanker) atau jinak (non-kanker) berdasarkan fitur-fitur dari gambar kanker payudara. Tujuan ini diukur dengan mencapai akurasi tinggi dalam mengklasifikasikan tumor, dengan target akurasi di atas 95% pada dataset pengujian. Tujuan ini dapat dicapai dengan menggunakan data medis dan teknik pembelajaran mesin yang tepat. Solusi ini sangat relevan karena dapat membantu dalam diagnosis dini kanker payudara, yang memiliki dampak kesehatan yang serius. Tujuan ini diharapkan akan selesai dalam waktu 6 bulan dan dapat digunakan secara praktis dalam waktu 1 tahun untuk mendukung pekerjaan para profesional medis dalam diagnosis kanker payudara.')

    with st.expander("Kesimpulan"):
        st.caption('Model SVC yang saya kembangkan menunjukkan kinerja yang sangat baik dengan akurasi sebesar 90% pada data pengujian. Meskipun skor recall yang sangat tinggi pada data pelatihan mungkin mengindikasikan potensi overfitting, performa yang tetap tinggi pada data pengujian menunjukkan bahwa model ini memiliki kapasitas yang baik dalam menggeneralisasi dan efektif dalam mengklasifikasikan data yang belum dikenal.')
elif page == 'Exploration Data Analysis':
    eda.run()
else:
    prediction .run()