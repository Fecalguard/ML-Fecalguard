# FecalGuard : **Inovasi Deteksi Dini Penyakit Ayam melalui Analisis Citra Feses Berbasis AI**

## Deskripsi Proyek  
FecalGuard adalah sistem AI berbasis Convolutional Neural Network (CNN) untuk klasifikasi penyakit ayam melalui analisis citra feses. Proyek ini membantu peternak skala kecil dan menengah mendeteksi dini penyakit seperti Coccidiosis, Newcastle Disease, dan Salmonella secara cepat, murah, dan efisien. 

## Link Dataset 
  Dataset: 
    [Chicken Disease Dataset - Kaggle](https://www.kaggle.com/datasets/allandclive/chicken-disease-1)

## Model  
Eksperimen dilakukan dengan beberapa arsitektur deep learning populer untuk klasifikasi citra feses ayam, dengan model terbaik yaitu VGG16 pretrained ImageNet (`vgg16_model.h5`). Dari hasil evaluasi performa di dataset, model **VGG16** memberikan hasil terbaik dari segi akurasi, stabilitas pelatihan, serta kemampuan generalisasi ke data validasi dan test.

- Model disimpan sebagai `vgg16_model.h5`

Model VGG16 yang digunakan adalah versi pretrained dari ImageNet, yang dipakai sebagai **base model tanpa lapisan fully connected (top layer)**. Pada base model tersebut, tambahkan beberapa layer khusus agar sesuai dengan klasifikasi 4 kelas pada proyek ini, meliputi:  
- Global Average Pooling untuk mereduksi dimensi output fitur  
- Dense layer dengan 256, 128, dan 64 neuron beraktivasi ReLU untuk ekstraksi fitur lanjut  
- Batch Normalization untuk menstabilkan dan mempercepat pelatihan  
- Dropout dengan rate 0.2 untuk mengurangi risiko overfitting  
- Dense output layer dengan aktivasi softmax sebanyak 4 neuron, sesuai jumlah kelas penyakit  

Pelatihan dilakukan dengan strategi **transfer learning**:  
- Pada tahap awal, base model VGG16 **dibekukan (freeze)** agar bobot pretrained tidak berubah, hanya layer atas yang dilatih.  
- Setelah itu, buka (unfreeze) 20 lapisan terakhir base model untuk proses **fine-tuning** dengan learning rate kecil, guna menyesuaikan model terhadap karakteristik dataset spesifik citra feses ayam.  

## Pelatihan & Evaluasi  
- Epochs: 25 dengan EarlyStopping  
- Metrik: akurasi, precision, recall, f1-score  
- Akurasi test: 96.6%  
- Precision, recall, f1-score rata-rata >95%  

## Struktur Proyek  
📁 ML-Fecalguard/</br>
├── 📁 model/</br>
│   ├── vgg16_model.h5</br>
├── 📁 notebook/</br>
│   ├── capstone_vgg16.ipynb</br>
├── 📁 streamlit-inference/</br>
│   ├── app.py</br>
│   ├── requirements.txt</br>
│   ├── Web-Screenshoot.png</br>
├── .gitattributes</br>
├── README.md</br>
└── requirements.txt</br></br>

## Cara Menjalankan  
1. Clone repositori dan install dependensi:  
   ```bash
   git clone https://github.com/Fecalguard/ML-Fecalguard.git
   cd ML-Fecalguard
   pip install -r requirements.txt
   ```
2. Jalankan notebook training dan evaluasi model (Optional)
3. Deploy model .h5 ke aplikasi web menggunakan FastAPI
4. Jalankan Inference model dengan panduan yang dapat anda akses pada Folder 📁 streamlit-inference
