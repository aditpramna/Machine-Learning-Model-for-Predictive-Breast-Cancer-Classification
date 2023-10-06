import streamlit as st
import pandas as pd
import pickle


def run():

    # Load All Files
    with open('all_process_aditpramna.pkl', 'rb') as file_1:
        all_process_aditpramna = pickle.load(file_1)

    # Menentukan rentang untuk masing-masing fitur
    feature_ranges = {
        'radius_mean': (7, 28),
        'texture_mean': (9, 40),
        'perimeter_mean': (44, 189),
        'area_mean': (144, 2501),
        'smoothness_mean': (0.05, 0.16),
        'compactness_mean': (0.02, 0.35),
        'concavity_mean': (0.0, 0.43),
        'concave points_mean': (0.0, 0.20),
        'symmetry_mean': (0.11, 0.3),
        'fractal_dimension_mean': (0.05, 0.1),
        'radius_se': (0.1, 2.9),
        'texture_se': (0.36, 4.9),
        'perimeter_se': (0.76, 22.0),
        'area_se': (6.8, 542.2),
        'smoothness_se': (0.0017, 0.03),
        'compactness_se': (0.002, 0.14),
        'concavity_se': (0.0, 0.4),
        'concave points_se': (0.0, 0.05),
        'symmetry_se': (0.007, 0.08),
        'fractal_dimension_se': (0.0009, 0.03),
        'radius_worst': (7.9, 36.0),
        'texture_worst': (12, 50),
        'perimeter_worst': (50, 251),
        'area_worst': (185, 4254),
        'smoothness_worst': (0.07, 0.2),
        'compactness_worst': (0.03, 1.06),
        'concavity_worst': (0.0, 1.25200),
        'concave points_worst': (0.0, 0.29),
        'symmetry_worst': (0.16, 0.7),
        'fractal_dimension_worst': (0.06, 0.21)
    }

    # Buat dictionary untuk menyimpan nilai input
    input_values = {}

    # Membuat input Streamlit menggunakan perulangan for
    for feature, (min_val, max_val) in feature_ranges.items():
        input_label = f'Tolong masukan {feature}'
        input_values[feature] = st.number_input(label=input_label, min_value=min_val, max_value=max_val)

    # Buat DataFrame dengan nilai input
    data_inf = pd.DataFrame(input_values, index=[0])

    # Tambahkan tombol untuk melakukan prediksi
    if st.button(label='Predict'):
        # Melakukan prediksi data dummy
        y_pred_inf = all_process_aditpramna.predict(data_inf)

        st.write(y_pred_inf[0])

        if y_pred_inf[0] == 0:
            st.write('Pasien terprediksi terkena kanker payudarah')
        else:
            st.write('Pasien terprediksi tidak terkena kanker payudarah')
