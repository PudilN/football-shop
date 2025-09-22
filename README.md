https://ainur-fadhil-footballshop.pbp.cs.ui.ac.id/

## Django AuthenticationForm
Apa itu Django AuthenticationForm?
Django AuthenticationForm adalah sebuah kelas form yang sudah disediakan secara bawaan di dalam django.contrib.auth.forms. Form ini dirancang khusus untuk memvalidasi kredensial pengguna, yaitu username dan password, selama proses login. Alih-alih harus membuat form login dari nol, pengembang bisa langsung menggunakannya di tampilan (view) untuk memproses data yang dikirimkan oleh pengguna, memverifikasi kecocokan data dengan yang ada di database, dan mengonfirmasi apakah pengguna tersebut valid atau tidak.

Salah satu kelebihan utamanya adalah kemudahan penggunaan. Form ini sudah terintegrasi penuh dengan sistem autentikasi Django, sehingga mempercepat proses pengembangan. Selain itu, form ini secara inheren aman karena ia menangani validasi kredensial dengan benar, membantu melindungi dari serangan umum seperti brute-force attack. Ia juga mengikuti standar penanganan form Django, membuatnya konsisten dengan bagian lain dari aplikasi.

Namun, AuthenticationForm juga memiliki kekurangan. Kekurangan yang paling signifikan adalah keterbatasan fungsionalitasnya. Form ini hanya didesain untuk login berbasis username dan password dan tidak dapat dikustomisasi untuk metode login yang lebih kompleks, seperti login menggunakan alamat email, nomor telepon, atau layanan media sosial. Form ini juga tidak bisa digunakan untuk pendaftaran pengguna baru; untuk itu, Django menyediakan form lain seperti UserCreationForm.
## Autentikasi dan Otorisasi
Autentikasi dan otorisasi adalah dua konsep krusial dalam keamanan web yang sering kali disalahartikan. Secara sederhana, autentikasi adalah proses memverifikasi identitas seseorang, menjawab pertanyaan "Apakah Anda benar orang yang Anda klaim?". Ini seperti menunjukkan kartu identitas di pintu masuk sebuah gedung. Sementara itu, otorisasi adalah proses menentukan hak akses yang dimiliki seseorang, menjawab pertanyaan "Apa yang boleh Anda lakukan di dalam gedung ini?". Ini seperti kartu akses yang hanya memberikan izin ke lantai atau ruangan tertentu.

Django mengimplementasikan autentikasi melalui aplikasi django.contrib.auth. Ketika pengguna memasukkan kredensial login, Django menggunakan sistem ini untuk mencocokkan kredensial dengan data di database. Komponen utama dalam proses ini termasuk model User yang menyimpan informasi pengguna, dan LoginView serta AuthenticationForm yang menangani logika dan form untuk proses login itu sendiri. Setelah verifikasi berhasil, Django akan menganggap pengguna tersebut telah terautentikasi.

Untuk otorisasi, Django juga menggunakan django.contrib.auth, khususnya melalui sistem perizinan (permissions) dan grup (groups). Pengembang dapat membuat izin khusus, misalnya can_edit_post, dan menetapkannya pada pengguna atau grup. Di dalam kode, pengembang kemudian dapat memeriksa izin ini menggunakan metode seperti user.has_perm() sebelum mengizinkan pengguna untuk mengakses atau memodifikasi suatu sumber daya, memastikan bahwa mereka tidak hanya terautentikasi tetapi juga memiliki wewenang yang diperlukan.
## Session dan Cookies
Dalam pengembangan web, baik session maupun cookies digunakan untuk menyimpan "state" atau data pengguna di lingkungan HTTP yang pada dasarnya tidak memiliki status. Cookies menyimpan data langsung di sisi klien (browser pengguna). Keuntungan utamanya adalah data tersebut tidak membebani server karena disimpan secara lokal di mesin pengguna. Namun, kekurangannya adalah data ini tidak aman karena dapat diakses dan diubah oleh pengguna atau pihak lain, dan memiliki batasan ukuran yang kecil (sekitar 4KB).

Sebaliknya, sessions menyimpan data di sisi server. Yang dikirim ke klien hanyalah sebuah session ID yang unik dan acak melalui cookie. Kelebihan utama dari pendekatan ini adalah keamanan yang lebih tinggi, karena data sensitif tetap berada di server, jauh dari jangkauan pengguna yang tidak berwenang. Session juga tidak memiliki batasan ukuran data yang ketat seperti cookie. Namun, kekurangannya adalah dapat mengonsumsi sumber daya server dan menimbulkan tantangan dalam hal skalabilitas saat aplikasi web tumbuh dan menggunakan banyak server.
## Cookies
Secara default, penggunaan cookies dalam pengembangan web tidak aman karena data yang tersimpan di dalamnya berada dalam format teks biasa di browser pengguna. Hal ini membuka berbagai risiko potensial, seperti Cross-Site Scripting (XSS) di mana skrip berbahaya dapat mencuri cookie pengguna, atau Cross-Site Request Forgery (CSRF) di mana penyerang dapat memaksa pengguna terautentikasi untuk melakukan permintaan yang tidak mereka inginkan. Karena cookies dikirim dengan setiap permintaan HTTP, mereka juga rentan terhadap intersepsi jika tidak menggunakan koneksi terenkripsi.

Django secara proaktif menangani risiko-risiko ini dengan berbagai fitur keamanan bawaan. Untuk melindungi dari CSRF, Django secara otomatis menyertakan token unik pada setiap form, yang harus diverifikasi server sebelum memproses permintaan. Selain itu, Django sangat merekomendasikan penggunaan HTTPS dan secara default menetapkan flag Secure pada cookie sesi, yang memastikan cookie hanya dikirim melalui koneksi terenkripsi.

Yang terpenting, Django secara default menggunakan sistem session berbasis server daripada menyimpan data langsung di cookie. Ini berarti data sensitif pengguna disimpan dengan aman di sisi server, dan cookie yang dikirimkan ke klien hanya berisi kunci acak yang sulit ditebak. Django juga mengatur flag HttpOnly pada cookie sesi, yang mencegah skrip JavaScript di sisi klien untuk mengaksesnya, secara efektif memitigasi serangan XSS yang mencoba mencuri cookie pengguna.

# Step by Step Tugas 4

## Registrasi, Login, dan Logout
Saya membuat sebuah view baru yang menggunakan UserCreationForm dari Django. View ini bertanggung jawab untuk menerima data yang dimasukkan pengguna (biasanya username dan password), memvalidasi data tersebut, dan jika valid, membuat objek User baru di database. Setelah akun berhasil dibuat, saya akan mengalihkan pengguna ke halaman login.

Untuk login, saya menggunakan LoginView bawaan Django. View ini secara otomatis menangani proses otentikasi: ia menerima kredensial yang dimasukkan pengguna, mencocokkannya dengan data di database, dan jika berhasil, akan membuat sesi login untuk pengguna tersebut.

Saya menggunakan LogoutView dari Django, yang hanya membutuhkan satu baris kode di urls.py. View ini akan menghapus sesi login pengguna, dan setelahnya mengalihkan pengguna ke halaman yang ditentukan, seperti halaman home atau login.

## Membuat Dua Akun Pengguna dengan Tiga Dummy Data
Pertama, saya membuat dua objek User baru. Kemudian, untuk setiap objek User, saya membuat tiga objek Product (dummy data). Objek Product ini dihubungkan dengan objek User yang bersangkutan melalui foreign key, sesuai dengan implementasi di langkah selanjutnya. Contohnya, untuk User pertama, saya membuat tiga produk yang owner-nya adalah User tersebut, dan hal yang sama saya lakukan untuk User kedua.

## Menghubungkan Model Product dengan User
Di dalam file models.py, saya menambahkan sebuah field baru pada model Product. Field ini akan merujuk pada model User dari Django (from django.contrib.auth.models import User). Saya menggunakan models.ForeignKey(User, on_delete=models.CASCADE). Parameter on_delete=models.CASCADE berarti jika seorang pengguna (pemilik) dihapus dari database, semua produk yang terhubung dengannya juga akan ikut terhapus. Ini memastikan integritas data.

## Menampilkan Informasi Pengguna dan Menerapkan Cookies
Saya memanfaatkan variabel request.user yang secara otomatis tersedia di dalam view dan template Django. Di dalam template HTML, saya menambahkan kode kondisional seperti {% if user.is_authenticated %}. Django secara otomatis mengelola cookie sesi untuk melacak status login pengguna. Fitur last_login adalah atribut bawaan dari model User di Django. Setiap kali pengguna berhasil login, Django secara otomatis memperbarui atribut last_login ini. Saya cukup mengambil nilai dari atribut request.user.last_login di dalam view dan meneruskannya ke template, di mana ia bisa ditampilkan kepada pengguna. Saya tidak perlu membuat atau mengelola cookie ini secara manual karena Django sudah menanganinya secara aman dan efisien.

# Feedback Untuk Asisten Dosen Tutorial 1
Tidak ada feedback khusus yang saya berikan karena sudah sangat baik memenuhi tugasnya sebagai asisten dosen. Terima kasih banyak kakak asdos.