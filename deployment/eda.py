import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# from PIL import Image

def run():
    #membuat function untuk nantinya dipanggil di app.py
    # def run():
    st.title('Welcome to Exploratory Data Analysis from Breast Cancer')
    #Memanggil data csv 
    data1= pd.read_csv('breast-cancer.csv')

    #menampilakn 5 data teratas
    st.table(data1.head())

    #menampilakn distribusi data
    st.table(data1.describe())
    with st.expander('Rekomendasi'):
        st.caption('Berdasarkan karakteristik data ini, dokter dan peneliti medis dapat membuat beberapa rekomendasi seperti berikut: Variabilitas yang besar dalam beberapa fitur mungkin mengindikasikan keragaman dalam jenis dan karakteristik kanker payudara, yang mungkin memerlukan pendekatan perawatan yang berbeda.Pemeriksaan lebih lanjut dapat dilakukan pada pasien dengan nilai ekstrem (minimal atau maksimal) dalam beberapa fitur untuk memahami apakah ada hubungan dengan prognosis atau respon terhadap perawatan.Analisis lebih lanjut dapat dilakukan untuk mengidentifikasi faktor-faktor yang mempengaruhi variasi dalam fitur-fitur ini, seperti usia, jenis kanker, atau faktor risiko lainnya.')

    st.title('Persentase diagnosis kanker payudarah')

    # Membuat pie chart
    fig_pie = plt.figure(figsize=(8, 5))
    data1.diagnosis.value_counts().plot.pie(autopct='%1.1f%%')
    plt.title('Pie Chart of Diagnosis')
    st.pyplot(fig_pie)

    # Membuat barplot
    fig_bar = plt.figure(figsize=(8, 5))
    sns.countplot(data=data1, x='diagnosis')
    plt.title('Bar Plot of Diagnosis')
    st.pyplot(fig_bar)

    # menampilkan penjelasan plot 
    with st.expander('Penjelasan'):
        st.caption('Terlihat dari gambar bahwa persentase pasien yang terkena kanker payudarah lebih sedikit dibandingkan dengan pasien yang tidak terkena kanker payudarah')

    # Menampilkan barplot
    st.title("Rata - Rata titik konkav dengan status kanker atau non kanker payudarah")
    fig_1 = plt.figure(figsize=(8, 6))

    # Group data by 'diagnosis' and calculate the mean of 'concave points_worst'
    grouped_data = data1.groupby(['diagnosis']).agg({'concave points_worst': 'mean'})

    # Create a barplot with custom color
    sns.barplot(x=grouped_data.index, y=grouped_data['concave points_worst'], palette=['#A865C9', '#f6abb6'])

    # Add labels and title
    plt.xlabel('Diagnosis')
    plt.ylabel('Mean concave points_worst')
    plt.title('Mean of concave points_worst by diagnosis')

    # Menampilkan heatmap dalam aplikasi Streamlit
    st.pyplot(fig_1)

    #menampilkan penjelasan plot
    with st.expander('Penjelasan'):
        st.caption('Nilai rata-rata yang lebih tinggi dari "concave points_worst" pada pasien dengan diagnosis "malignant" (ganas) menunjukkan bahwa ada kecenderungan bahwa pasien dengan kanker payudara ganas memiliki nilai "concave points_worst" yang lebih tinggi dibandingkan dengan pasien yang memiliki kanker payudara jinak.')


    # Menampilkan barplot 
    st.title("Rata - Rata nilai luas area sel dengan status kanker atau non kanker payudarah")
    fig_2 = plt.figure(figsize=(8, 6))

    # Group data by 'diagnosis' and calculate the mean of 'area_worst'
    grouped_data = data1.groupby(['diagnosis']).agg({'area_worst': 'mean'})

    # Create a barplot with custom color
    sns.barplot(x=grouped_data.index, y=grouped_data['area_worst'], palette=['#A865C9', '#f6abb6'])

    # Add labels and title
    plt.xlabel('Diagnosis')
    plt.ylabel('Mean area_worst')
    plt.title('Mean of area_worst by diagnosis')

    # Menampilkan heatmap dalam aplikasi Streamlit
    st.pyplot(fig_2)

    #menampilkan penjelasan plot 
    with st.expander('Penjelasan'):
        st.caption('Terdapat perbedaan yang signifikan dalam rata-rata nilai "area_worst" antara pasien dengan diagnosis "benign" dan "malignant". Pasien dengan kanker payudara ganas (malignant) cenderung memiliki nilai "area_worst" yang jauh lebih tinggi daripada pasien dengan kanker payudara jinak (benign).')


    # Menampilkan barplot 
    st.title("Rata - Rata nilai perimeter tumor dengan status kanker atau non kanker payudarah")
    fig_3 = plt.figure(figsize=(8, 6))

    # Group data by 'diagnosis' and calculate the mean of 'areaperimeter_worstorst'
    grouped_data = data1.groupby(['diagnosis']).agg({'perimeter_worst': 'mean'})

    # Create a barplot with custom color
    sns.barplot(x=grouped_data.index, y=grouped_data['perimeter_worst'], palette=['#A865C9', '#f6abb6'])

    # Add labels and title
    plt.xlabel('Diagnosis')
    plt.ylabel('Mean perimeter_worst')
    plt.title('Mean of perimeter_worst by diagnosis')

    st.pyplot(fig_3)

    #menampilkan penjelasan plot 
    with st.expander('Penjelasan'):
        st.caption('Data ini menggambarkan perbedaan dalam rata-rata perimeter tumor pada pasien dengan diagnosis kanker payudara "benign" dan "malignant". Perimeter yang lebih besar pada pasien dengan kanker payudara "malignant" dapat mengindikasikan bahwa tumor tersebut lebih besar dan mungkin memiliki tingkat keganasan yang lebih tinggi.')
    # menapilkan penjelesan


