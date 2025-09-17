https://ainur-fadhil-footballshop.pbp.cs.ui.ac.id/

## Data Delivery
Data delivery diperlukan agar aplikasi dapat bertukar data antar sistem dengan format yang konsisten dan mudah dipahami. Misalnya, ketika frontend (React, Vue, dsb.) meminta data ke backend Django, data yang dikirimkan harus dalam format yang bisa dibaca universal. Tanpa mekanisme data delivery, aplikasi akan sulit berkomunikasi dengan sistem lain, API tidak bisa dipakai lintas platform, dan integrasi akan terbatas.
## XML or JSON
JSON lebih baik dalam konteks web modern karena strukturnya sederhana, ringan, dan mudah dipahami oleh manusia maupun mesin. JSON juga langsung kompatibel dengan JavaScript, sehingga lebih natural digunakan pada aplikasi web.

XML memiliki kelebihan seperti dukungan untuk atribut, namespace, dan validasi dengan schema, tetapi cenderung lebih verbose (banyak tag pembuka/penutup).

JSON lebih populer karena lebih efisien (ukuran data lebih kecil), parsing lebih cepat, dan lebih mudah digunakan di hampir semua bahasa pemrograman modern.
## is_valid
Fungsi is_valid() digunakan untuk memvalidasi data yang dimasukkan ke dalam form berdasarkan aturan yang ditentukan di model atau di form itu sendiri. Jika data memenuhi semua syarat (misalnya field tidak kosong, format email benar, angka sesuai range, dsb.), maka is_valid() akan mengembalikan True. Kita membutuhkannya supaya hanya data yang valid dan sesuai kriteria yang masuk ke database, sehingga menjaga integritas data.
## csrf_token
csrf_token adalah token keamanan yang digunakan Django untuk mencegah Cross-Site Request Forgery (CSRF). Tanpa csrf_token, penyerang bisa membuat halaman berbahaya yang secara diam-diam mengirim request ke server dengan identitas user yang sedang login, sehingga data bisa diubah tanpa sepengetahuan user. Dengan adanya csrf_token, setiap form yang dikirim harus menyertakan token unik yang hanya valid untuk sesi pengguna tertentu, sehingga request palsu dari luar akan ditolak.

# Step by Step Tugas 3

## 4 view baru
Ini dibuat agar data yang ada di database bisa diakses dalam format standar yang umum dipakai aplikasi lain. XML dan JSON adalah dua format paling sering digunakan. Versi all (semua data) berguna kalau kita ingin menampilkan seluruh isi tabel.Versi by ID dibuat supaya kita bisa melihat detail dari satu objek saja. Karena nanti aplikasi bisa fleksibel: mau ambil semua data bisa, mau ambil satu data juga bisa.

## Membuat routing URL untuk masing-masing views
Routing itu seperti alamat jalan. Supaya setiap fungsi view yang sudah dibuat bisa diakses lewat browser atau API, kita perlu kasih “jalan masuknya” dengan URL. Kalau tidak ada routing, fungsi tadi ada tapi tidak bisa diakses.

## Membuat halaman form untuk menambahkan objek model
Form adalah cara standar untuk input data baru. Jadi ketika user klik tombol "Add", mereka diarahkan ke form ini. Supaya data baru bisa langsung masuk ke database dengan cara yang rapi dan mudah.

## Membuat halaman detail dari setiap data objek model
Halaman ini menampilkan informasi lebih lengkap tentang 1 data tertentu. Karena tidak semua informasi cocok ditampilkan di daftar utama. Kadang ada data yang detailnya panjang, jadi lebih baik dipisah di halaman khusus.

# Feedback Untuk Asisten Dosen Tutorial 1
Tidak ada feedback khusus yang saya berikan karena sudah sangat baik memenuhi tugasnya sebagai asisten dosen. Terima kasih banyak kakak asdos.