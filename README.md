# FecalGuard  
**Inovasi Deteksi Dini Penyakit Ayam melalui Analisis Citra Feses Berbasis AI**

---

## Deskripsi Proyek  
FecalGuard adalah sistem AI berbasis Convolutional Neural Network (CNN) untuk klasifikasi penyakit ayam melalui analisis citra feses. Proyek ini membantu peternak skala kecil dan menengah mendeteksi dini penyakit seperti Coccidiosis, Newcastle Disease, dan Salmonella secara cepat, murah, dan efisien. Dataset citra feses ayam berlabel dari Tanzania digunakan untuk melatih model agar mampu mengenali kondisi ayam dalam empat kategori utama:  
- Healthy  
- Coccidiosis  
- Newcastle Disease  
- Salmonella  

---

## Link Dataset  

  Dataset ini diperoleh dari platform penyedia dataset [Kaggle](https://www.kaggle.com)
  
  Dataset: 
    [Chicken Disease Dataset - Kaggle](https://www.kaggle.com/datasets/allandclive/chicken-disease-1)

---

## Tim Proyek  
| Nama                          | ID Cohort         | Institusi             | Status |  
|-------------------------------|--------------|-----------------------|--------|  
| Duma Mora Arta Sitorus         | A200XBM138   | Universitas Diponegoro | Aktif  |  
| Labiba Adinda Zahwana          | A200XBM251   | Universitas Diponegoro | Aktif  |  
| Muhammad Rizki                 | A200YBM347   | Universitas Diponegoro | Aktif  |  
| Tiara Fitra Ramadhani Siregar | A200XBM484   | Universitas Diponegoro | Aktif  |  

---

## Pernyataan Masalah  
Peternak ayam skala kecil dan menengah menghadapi kesulitan deteksi dini penyakit karena keterbatasan alat diagnostik yang praktis dan terjangkau. Keterlambatan penanganan menyebabkan penyebaran penyakit dan angka kematian tinggi. Feses ayam mengandung informasi biologis penting sebagai indikator kesehatan, namun belum banyak dimanfaatkan teknologi untuk analisisnya. Proyek ini mengembangkan sistem AI untuk menganalisis citra feses ayam secara cepat, murah, dan akurat.

---

## Pertanyaan Penelitian  
- Bagaimana efektivitas model AI berbasis klasifikasi citra dalam mendeteksi dini penyakit ayam melalui citra feses?  
- Seberapa akurat model membedakan ayam sehat dan terinfeksi penyakit?

---

## Lingkup Proyek  
- Pengumpulan dan preprocessing data citra feses ayam  
- Eksplorasi arsitektur CNN dan transfer learning  
- Pelatihan dan fine-tuning model klasifikasi  
- Pengembangan aplikasi web untuk upload dan klasifikasi gambar  
- Dokumentasi dan evaluasi berkala  

---

## Implementasi Model  

---

### Data Loading & Eksplorasi  
- Dataset 4 kelas penyakit dengan resolusi dominan 224x224 piksel  
- Data dibagi train:val:test = 80:15:15 secara stratifikasi

---

### Data Augmentation  
- Augmentasi train data (rotasi, geser, zoom, flip)  
- Normalisasi val dan test data

---

### Model  
Eksperimen dilakukan dengan beberapa arsitektur deep learning populer untuk klasifikasi citra feses ayam, yaitu:  
- CNN custom (`cnn_model.h5`)  
- VGG16 pretrained ImageNet (`vgg16_model.h5`)  
- ResNet50 (`ResNet50_model.h5`)  
- DenseNet121 (`denseNet121_model.h5`)  
- MobileNetV2 (`mobileNetV2_model.h5`)  

Dari hasil evaluasi performa di dataset, model **VGG16** memberikan hasil terbaik dari segi akurasi, stabilitas pelatihan, serta kemampuan generalisasi ke data validasi dan test.

Model VGG16 yang digunakan adalah versi pretrained dari ImageNet, yang dipakai sebagai **base model tanpa lapisan fully connected (top layer)**. Pada base model tersebut, tambahkan beberapa layer khusus agar sesuai dengan klasifikasi 4 kelas pada proyek ini, meliputi:  
- Global Average Pooling untuk mereduksi dimensi output fitur  
- Dense layer dengan 256, 128, dan 64 neuron beraktivasi ReLU untuk ekstraksi fitur lanjut  
- Batch Normalization untuk menstabilkan dan mempercepat pelatihan  
- Dropout dengan rate 0.2 untuk mengurangi risiko overfitting  
- Dense output layer dengan aktivasi softmax sebanyak 4 neuron, sesuai jumlah kelas penyakit  

Pelatihan dilakukan dengan strategi **transfer learning**:  
- Pada tahap awal, base model VGG16 **dibekukan (freeze)** agar bobot pretrained tidak berubah, hanya layer atas yang dilatih.  
- Setelah itu, buka (unfreeze) 20 lapisan terakhir base model untuk proses **fine-tuning** dengan learning rate kecil, guna menyesuaikan model terhadap karakteristik dataset spesifik citra feses ayam.  

---

### Pelatihan & Evaluasi  
- Epochs: 25 dengan EarlyStopping  
- Metrik: akurasi, precision, recall, f1-score  
- Akurasi test: ~96.6%  
- Precision, recall, f1-score rata-rata >95%  

---

### Penyimpanan  
- Model disimpan sebagai `vgg16_model.h5`

---

### Struktur Proyek  
📁 ML-Fecalguard/</br>
├── 📁 img/</br>
│   ├── a-few-img.png</br>
│   ├── conv-matrix.png</br>
│   └── evaluation-train-val.png</br>
├── 📁 model/</br>
│   ├── vgg16_model.h5</br>
│   ├── ResNet50_model.h5</br>
│   ├── DenseNet121_model.h5</br>
│   ├── MobileNetV2_model.h5</br>
│   └── CNN_model.h5</br>
├── 📁 notebook/</br>
│   ├── capstone_vgg16.ipynb</br>
│   ├── capstone_ResNet50.ipynb</br>
│   ├── capstone_DenseNet121.ipynb</br>
│   ├── capstone_MobileNetV2.ipynb</br>
│   └── capstone_CNN.ipynb</br>
├── .gitattributes</br>
├── evaluation-results.pdf</br>
├── README.md</br>
└── requirements.txt</br></br>

---

## Visualisasi  
- Contoh gambar dataset
<br>
<br>
    <p align='center'><img src="https://raw.githubusercontent.com/Fecalguard/ML-Fecalguard/main/img/a-few-img.png" alt="Contoh gambar dataset" width="400" />
    </p>
<p align='center'>Gambar 1. Contoh Gambar</p>
<br>
- Kurva akurasi dan loss pelatihan 
<br>
<br>
    <p align='center'><img src="https://raw.githubusercontent.com/Fecalguard/ML-Fecalguard/main/img/evaluation-train-val.png" alt="evaluasi" width="400" />
    </p>
<p align='center'>Gambar 2. Visualisasi Kurva Accuracy Train dan Loss</p>
<br>
- Confusion matrix model
<br>
<br>
    <p align='center'><img src="https://raw.githubusercontent.com/Fecalguard/ML-Fecalguard/main/img/conv-matrix.png" alt="Contoh gambar dataset" width="400" />
    </p>
<p align='center'>Gambar 3. Convusion Matrix</p>
<br>

---

## Teknologi yang Digunakan

| Teknologi / Library              | Versi      | Keterangan                                         |
|---------------------------------|------------|---------------------------------------------------|
| Python                          | 3.x        | Bahasa pemrograman utama                           |
| TensorFlow                      | 2.18.0     | Framework deep learning untuk pelatihan model CNN |
| Keras (bagian dari TensorFlow)  | 2.18.0     | API high-level untuk membangun model neural network|
| FastAPI                 | 4.22.0     | Untuk deploy model di lingkungan JavaScript/web   |
| scikit-learn                   | 1.6.1      | Untuk evaluasi performa dan pemrosesan data       |
| pandas                         | 2.2.2      | Manipulasi dan analisis data tabular               |
| numpy                          | 2.0.2      | Operasi numerik dan array                           |
| matplotlib                     | 3.10.0     | Visualisasi data dan grafik                          |
| seaborn                       | 0.13.2     | Visualisasi statistik berbasis matplotlib          |
| pillow (PIL)                  | 11.1.0     | Pengolahan gambar                                   |
| kagglehub                     | 0.3.11     | Tool untuk mengakses dataset Kaggle secara otomatis|

Selain itu, beberapa modul bawaan Python juga digunakan seperti `os`, `shutil`, `io`, `random`, dan `collections` untuk pengelolaan file, operasi sistem, dan struktur data dasar.

---

## Cara Menjalankan  
1. Clone repositori dan install dependensi:  
   ```bash
   git clone https://github.com/Fecalguard/ML-Fecalguard.git
   cd ML-Fecalguard
   pip install -r requirements.txt
   ```
2. Jalankan notebook training dan evaluasi model (Optional)
3. Deploy model .h5 ke aplikasi web menggunakan FastAPI