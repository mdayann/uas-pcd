# uas-pcd
![image](https://github.com/user-attachments/assets/c8c271ec-07d1-4b57-8077-559e358fe933)

Analisis Perbandingan:
1. Sensitivitas Noise:
   - Roberts lebih sensitif terhadap noise karena kernel kecil (2x2)
   - Sobel lebih tahan noise karena kernel lebih besar (3x3)

2. Ketebalan Tepi:
   - Roberts menghasilkan tepi lebih tipis dan detail
   - Sobel menghasilkan tepi lebih tebal dan jelas

3. Orientasi Tepi:
   - Roberts lebih baik mendeteksi tepi diagonal
   - Sobel lebih baik untuk tepi vertikal/horizontal

4. Komputasi:
   - Roberts lebih cepat karena kernel kecil
   - Sobel lebih lambat tapi akurasi lebih baik
