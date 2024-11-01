# Jarkom-Socket-Programming

13_Tugas-Socket-Programming 

Tugas UDP Socket Programming

Kelompok 13, Nitra Abitara
Anggota : 
1. Carlen Asadel Axelle (18223017)
2. Adam Joaquin Girsang (18223089)

//Prosedur untuk menjalankan program chatroom
I. Persiapan
 1. Pastikan pengaturan firewall sudah memperbolehkan koneksi UDP pada port "12345"
 2. Pastikan kedua device connect ke wifi yang sama dan stabil
 3. Pastikan "server.py" dan "client.py" berada dalam satu folder

II. Pengujian Program
 A. Menjalankan Server
  1. Buka command prompt/terminal lain pada folder
  2. Ketik : "python server.py" pada terminal
  3. Apabila berhasil, akan muncul text : "Server berjalan di 0.0.0.0:12345" di terminal

 B. Menjalankan Client
  1. Buka command prompt/terminal lain pada folder
  2. Ketik : "python client.py" pada terminal
  3. Apabila berhasil, akan muncul dialogbox untuk memasukkan IP Server, Port Server, 
     Password Chatroom, Username
  4. Setelah semua dimasukkan, akan tampil text : "Terhubung ke chatroom. Ketik 'exit' untuk keluar."
     di chatroom, selain itu, di terminal server akan muncul text : <username> (('<IP Server>', <Port Number>)) terhubung ke chatroom.
  5. Lakukan langkah yang sama apabila ingin melakukan pengujian pada 2 client

 C. Teknis Chatroom
  1. Di chatroom, silahkan ketik teks di box diatas tombol kirim, lalu tekan tombol "kirim"
  2. Pesan akan diteruskan ke server, lalu ke client melalui GUI
  3. Selain itu, pesan oleh masing-masing client akan ditampilkan di terminal server
     dengan text : "Pesan dari <username> (('<IP Server>', <Port Number>)): <pesan>'
  4. Untuk keluar dari chatroom, client bisa mengetik "exit"
