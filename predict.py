import pandas as pd
import joblib
import numpy as np

def run_prediction():
    # 1. Load Model dan Tools pendukung
    try:
        model = joblib.load('model_attrition.pkl')
        features = joblib.load('features_list.pkl')
    except FileNotFoundError:
        print("Error: File model tidak ditemukan. Pastikan sudah menjalankan proses training.")
        return

    print("--- Program Prediksi Attrition Karyawan ---")
    print(f"Masukkan data untuk {len(features)} fitur berikut:")

    # 2. Input Data (Contoh sederhana: Mengambil satu baris input)
    # Di dunia nyata, ini bisa diganti dengan input dari User Interface atau Excel
    input_data = {}
    for feature in features:
        val = input(f"Masukkan nilai untuk {feature}: ")
        input_data[feature] = [float(val)]

    df_input = pd.DataFrame(input_data)


    # 4. Prediksi dengan Threshold 0.35 (Sesuai optimasi terakhir Anda)
    probability = model.predict_proba(df_input)[:, 1]
    
    threshold = 0.35
    result = "Resign (High Risk)" if probability >= threshold else "Stay (Low Risk)"

    print("\n--- HASIL ANALISIS ---")
    print(f"Probabilitas Resign: {probability[0]:.2%}")
    print(f"Rekomendasi HR: {result}")

if __name__ == "__main__":
    run_prediction()
