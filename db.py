import sqlite3

with sqlite3.connect("quiz.db") as db:
    cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
username VARCHAR(20) NOT NULL Primary Key,
name VARCHAR(20) NOT NULL,
password VARCHAR(20) NOT NULL,
jumlahtes INT(11) default 0
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS sesi(
username VARCHAR(20) NOT NULL,
name VARCHAR(20) NOT NULL,
jumlahtes INT(11)
);
''')

cursor.execute('SELECT * from users')
if cursor.fetchall():
    x=1
else:
    cursor.execute('''INSERT INTO users(username,name,password) VALUES('master','headmaster','master')''')
    db.commit()

cursor.execute('''
CREATE TABLE IF NOT EXISTS soal(
	id			INTEGER DEFAULT 1 PRIMARY KEY AUTOINCREMENT,
	matpel		VARCHAR(10),
	soal 		VARCHAR(500),
	tingkat_kesulitan	 INT(11)
);''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS soalterpilih(
	id			INTEGER,
    matpel VARCHAR(10),
	soal 		VARCHAR(500),
    tingkat_kesulitan INT(11)
);''')

cursor.execute('SELECT * from soal')

if cursor.fetchall():
    x=2
else:
    cursor.execute('''INSERT INTO Soal(matpel, soal, tingkat_kesulitan) VALUES
("IPA", "Rangka tersusun dari ...", 1),
("IPA", "Alat indra yang paling peka untuk membedakan benda panas dan benda dingin adalah", 1),
("IPA", "Penghubung antar tulang disebut...", 3),
("IPA", "Rangsangan yang dapat diterima hidung berupa...", 1),
("IPA", "Alat indra tubuh berguna untuk...", 1),
("IPA", "Daun kebanyakan berwarna hijau karena mengandung...", 2),
("IPA", "Bagian tumbuhan yang berfungsi mencari air dan zat hara di dalam tanah adalah ...", 2),
("IPA", "Berikut adalah fungsi-fungsi daun, kecuali ...", 2),
("IPA", "Bagian tumbuhan yang berfungsi sebagai alat transportasi atau pengangkut adalah ...", 2),
("IPA", "Daun selalu tumbuh dari...", 1),
("IPA", "Lebah mengambil ... yang ada di tumbuhan", 1),
("IPA", "Di bawah ini yang merupakan salah satu makanan burung elang adalah ...", 1),
("IPA", "Walaupun bertubuh kecil, laba-laba merupakan ... karena memangsa hewan kecil lain yang terjebak di sarangnya.", 1),
("IPA", "Hewan yang sumber makanannya berupa jagung, cacing, beras, dan ulat adalah ...", 1),
("IPA", "Fungsi taring dan cakar yang tajam pada kucing adalah untuk ...", 1),
("IPA", "Seluruh tahap pertumbuhan yang dialami makhluk hidup selama hidupnya disebut ...", 3),
("IPA", "Hewan yang mengalami metamorfosis sempurna adalah ...", 3),
("IPA", "Hewan berikut ini yang mengalami metamorfosis tidak sempurna adalah ...", 3),
("IPA", "Serangga dibawah ini yang mengalami tahap kepompong (pupa) dalam daur hidupnya adalah. ...", 3),
("IPA", "Telur kupu-kupu menetas menjadi ...", 2),
("IPA", "Hubungan makhluk hidup yang saling menguntungkan terjadi antara ...", 2),
("IPA", "Simbiosis parasitisme terjadi antara ...", 2),
("IPA", "Padi dimakan burung, lalu burung dimakan ular. Urutan ini disebut ...", 1),
("IPA", "Hubungan antara benalu dengan pohon mangga membentuk simbiosis ...", 2),
("IPA", "Hewan dibawah ini yang bergantung hidupnya tergantung pada hewan lain adalah ...", 1),
("IPA", "Benda padat adalah ...", 1),
("IPA", "Yang termasuk benda padat yaitu ...", 1),
("IPA", "Perubahan benda apdat menjadi cair disebut ...", 1),
("IPA", "Benda yang bentuknya berubah-ubah mengikuti tempatnya, tetapi volumenya tetap disebut ...", 2),
("IPA", "Menyublim merupakan ...", 3),
("Matematika", "8,078 + 6,586 - 5,749", 1),
("Matematika", "Operasi hitung yang menghasilkan bilangan 56 adalah ...", 1),
("Matematika", "Hasil 1,302 + (-17) - (-137) = ...", 1),
("Matematika", "KPK dari 24, 54, dan 63 adalah ...", 2),
("Matematika", "Bentuk desimal dari pecahan 3/24 adalah ...", 2),
("Matematika", "Hasil dari 2,5 gross - 7,5 lusin + 11 biji adalah ... biji ", 2),
("Matematika", "Luas dari sebuah persegi (s=16 cm) dan segitiga siku-siku (t=16 cm, a=12 cm) adalah ...", 3),
("Matematika", "Jarak rumah Edwin Kristian ke sekolah 3 km. Edwin Kristian berangkat ke sekolah dengan naik sepeda 06.30 dan tiba pukul 06.45. Kecepatan rata-rata ada …km/jam", 3),
("Matematika", "Rata-rata nilai di sebuah kelas dengan 27 orang adalah 70. Berapa rata-rata kelas jika ditambah seorang murid dengan nilai 86?", 3),
("Matematika", "Survey pada suatu kelas menghasilkan bahwa 20 orang menyukai sepakbola, 5 orang menyukai basket, dan 9 orang menyukai baseball. Berapa presentase orang yang menyukai basket?", 3),
("Matematika", "Keliling sebuah pentagon dengan sisi 40 cm adalah ...", 3),
("Matematika", "Hasil dari 24 - 2 x 5 + 3 = ", 1),
("Matematika", "Hasil 872 + 63 x(-9) - 927 : (-9) = ...", 1),
("Matematika", "Ibu Sakura membeli gula pasir 6 Kg, berasa 25 Kg, dan telor 4 kg. Harga setiap 1 Kg gula pasir Rp. 12.600,00, beras Rp 8.200,00 dan telor Rp. 18.500,00. Ibu Sakura membayar denga 4 lembar uang seratus ribuan. Ibu Sakura menerima uang pengembalian sebanyak...?", 2),
("Matematika", "Ibu Hinata membeli beras sebanyak   3 1/4 Kg, kemudian dimasak sebanyak 1,5 kg. Ibu Hinata membeli lagi 2 3/4 kg. Berat beras Ibu Hinata sekarang adalah.... ?", 2),
("Matematika", "Lampu biru menyala  setiap 3 menit, lampu kuning menyala setiap 5 menit, dan lampu hijau menyala setiap 8 menit. Jika pukul 18.15 ketiga lampu dinyalakan bersamaan, maka ketiga lampu akan menyala bersamaan untuk kedua kalinya pada....?", 3),
("Matematika", "Sifat bangun datar trapesium sama kaki adalah ...", 3),
("BI", "Paman bekerja sebagai wartawan. Makna kata wartawan adalah ...", 3),
("BI", "Pertunjukan wayang kulit, biasanya dilakukan semalam suntuk.
Sinonim kata pertunjukkan adalah ...", 3),
("BI", "Nani membeli obat di apotek. Arti kata apotek adalah ...", 3),
("BI", "Lomba baca puisi itu bukan untuk siswa SMP ... untuk siswa SD. Kata yang tepat untuk melengkapi kalimat tersebut adalah ...", 3),
("BI", "Buaya itu sudah ditolong sang Kancil .... malah balik menyerang. Kata gabung untuk melengkapi kalimat tersebut adalah ...", 3),
("BI", "Adi : Yul, mengapa kamu kemarin tidak masuk sekolah?. Yulia : (...). Adi : Oh, syukurlah kalau kamu sudah sembuh. Kalimat yang tepat untuk melengkapi teks percakapan tersebut adalah ...", 2),
("BI", "Hakim : Bagaimana menurutmu lukisan buatanku? Ica : (...). Hakim : Kamu benar, warna laut dalam lukisanku kurang menarik. Aku akan memperbaiki nya. Kalimat tanggapan yang tepat untuk melengkapi teks percakapan tersebut adalah ...", 2),
("BI", "Rita tidak pernah berbicara kasar terhadap siapa pun. Jika bertemu guru ia selalu memberi salam. Rita selalu menolong teman-teman nya. Sifat Rita dalam cerita tersebut adalah ...", 2),
("BI", "Penulisan tempat tanggal lahir yang sesuai dengan kaidah yang benar adalah ...", 2),
("BI", "Ketut mewakili sekolahnya mengikuti lomba lukis. Tanggapan yang logis untuk kalimat tersebut adalah ...", 2),
("BI", "(1) Butet : Kau memang pantas jadi juara. (2) Ikhsan : Ini berkat doa kalian. (3) Kristin : Selamat ya, Ikhsan! \n(4) Ikhsan : Terima kasih, Kristin. Susunan yang baik untuk percakapan tersebut adalah ...", 1),
("BI", "Betusta tinggal hanya bersama ibunya yang miskin. Walaupun demikian, Betusta selalu ceria. Ia dan ibunya hanya memiliki dua ekor domba. Betusta rajin menggembalakan domba di tepi hutan. Setiap pagi, ibunya memasukkan sepotong roti dan sebuah tempat air kosong ke dalam tasnya. Watak tokoh Betusta dalam dongeng tersebut adalah ...", 1),
("BI", "Baginda: Hai, anakku! Hati-hati engkau, jangan tergoda oleh harta sebab engkau akan menyesal jika ajal telah datang. Kejujuran lebih berharga dan mulia dari segalanya. Pesan utama dari cerita tersebut ialah ...", 1),
("BI", "Bayu ingin bermain sepak bola. Agus ingin bermain sepak bola. Gabungan yang tepat dari dua kalimat tersebut adalah ...", 1),
("BI", "Saat menyeberang jalan maka kita harus ...", 1);''')
    db.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS pilihan(
	id_soal		INT(11),
	pilihan 	VARCHAR(500),
	value		BOOLEAN,
	PRIMARY KEY(id_soal, pilihan),
	FOREIGN KEY (id_soal) REFERENCES soal(id)
);''')

cursor.execute('SELECT * from pilihan')
if cursor.fetchall():
    x=3
else:
    cursor.execute('''INSERT INTO Pilihan(id_soal, pilihan, value) VALUES
(1, "Tulang dan daging", 2),
(1, "Tulang dan otot", 3),
(1, "Tulang dan kulit", 4),
(1, "Rangkaian tulang", 1),
(2, "Hidung", 2),
(2, "Kulit", 1),
(2, "Mata", 3),
(2, "Telinga", 4),
(3, "Otot", 2),
(3, "Sendi", 1),
(3, "Daging", 3),
(3, "Rangka", 4),
(4, "Getaran", 2),
(4, "Larutan", 3),
(4, "Bau", 1),
(4, "Cahaya", 4),
(5, "Mengenal keadaan luar tubuh", 1),
(5, "Melindungi organ tubuh", 2),
(5, "Menguatkan tubuh", 3),
(5, "Mengetahui posisi tubuh", 4),
(6, "Oksigen", 2),
(6, "Klorofil", 1),
(6, "Air", 3),
(6, "Karbondioksida", 4),
(7, "Daun", 2),
(7, "Batang", 3),
(7, "Bunga", 4),
(7, "Akar", 1),
(8, "Tempat memasak makanan", 2),
(8, "Sebagai alat pernapasan", 3),
(8, "Tempat berlangsungnya proses penguapan", 4),
(8, "Menyerap air dalam tanah", 1),
(9, "Batang", 1),
(9, "Akar", 2),
(9, "Daun", 3),
(9, "Bunga", 4),
(10, "Batang", 1),
(10, "Akar", 2),
(10, "Bunga", 3),
(10, "Biji", 4),
(11, "Bunga", 2),
(11, "Putik", 3),
(11, "Serbuk sari", 4),
(11, "Nektar", 1),
(12, "Badak", 2),
(12, "Kelinci", 1),
(12, "Jagung", 3),
(12, "Pepaya", 4),
(13, "Karnivora", 1),
(13, "Omnivora", 2),
(13, "Herbivora", 3),
(13, "Ortovora", 4),
(14, "Anjing", 2),
(14, "Ayam", 1),
(14, "Burung kakatua", 3),
(14, "Kucing", 4),
(15, "Menangkap mangsanya", 1),
(15, "Mendapatkan nektar", 2),
(15, "Menyobek dedaunan", 3),
(15, "Melompat dari tempat tinggi", 4),
(16, "Metamorfosis", 2),
(16, "Pengembangbiakan", 3),
(16, "Pertumbuhan", 4),
(16, "Daur hidup", 1),
(17, "Belalang", 2),
(17, "Kupu-kupu", 1),
(17, "Katak", 3),
(17, "Kecoak", 4),
(18, "Kupu-kupu", 2),
(18, "Lalat", 3),
(18, "Kecoak", 1),
(18, "Katak", 4),
(19, "Kecoak", 2),
(19, "Laba-laba", 3),
(19, "Nyamuk", 1),
(19, "Belalang", 4),
(20, "Ulat", 1),
(20, "Kepompong", 2),
(20, "Berudu", 3),
(20, "Pupa", 4),
(21, "Benalu dan tumbuhan inang", 2),
(21, "Kerbau dan kutu", 3),
(21, "Kerbau dan burung jalak", 1),
(21, "Anggrek dan benalu", 4),
(22, "Kerbau dan kutu", 1),
(22, "Kerbau dan burung jalak", 2),
(22, "Ikan hiu dan ikan remora", 3),
(22, "Benalu dan tali putri", 4),
(23, "Siklus kehidupan", 2),
(23, "Jaring-jaring makanan", 3),
(23, "Rantai makanan", 1),
(23, "Rantai kehidupan", 4),
(24, "Mutualisme", 2),
(24, "Parasitisme", 1),
(24, "Komensalisme", 3),
(24, "Netralisme", 4),
(25, "Singa", 1),
(25, "Kijang", 2),
(25, "Gajah", 4),
(25, "Kuda", 3),
(26, "Benda yang mempunyai bentuk dan volum yang tetap", 1),
(26, "Benda yang mempunyai bentuk tidak tetap dan volum yang tetap", 2),
(26, "Benda yang mempunyai bentuk dan volum yang tidak tetap", 3),
(26, "Benda yang mempunyai bentuk tidak tetap dan volum yang tidak tetap", 4),
(27, "Balok es", 1),
(27, "Minyak", 2),
(27, "Kecap", 3),
(27, "Air putih", 4),
(28, "Membeku", 2),
(28, "Mencair", 1),
(28, "Mengembun", 3),
(28, "Menguap", 4),
(29, "Benda padat", 2),
(29, "Benda cair", 1),
(29, "Benda gas", 3),
(29, "Semua benar", 4),
(30, "Perubahan benda padat menjadi gas", 1),
(30, "Perubahan benda padat menjadi cair", 2),
(30, "Perubahan benda cair menjadi gas", 3),
(30, "Perubahan benda gas menjadi padat", 4),
(31, "8,925", 2),
(31, "8,915", 1),
(31, "8,905", 3),
(31, "8,805", 4),
(32, "128 / 8 x 4", 2),
(32, "336 / 3 x 2", 3),
(32, "112 x 7 / 14", 1),
(32, "72 x 6 / 8", 4),
(33, "-1,182", 2),
(33, "-1,148", 3),
(33, "1,148", 4),
(33, "1,422", 1),
(34, "1,512", 1),
(34, "508", 2),
(34, "378", 3),
(34, "1,68", 4),
(35, "0,012", 2),
(35, "0,120", 3),
(35, "1,250", 1),
(35, "12,50", 4),
(36, "360", 2),
(36, "288", 3),
(36, "281", 1),
(36, "270", 4),
(37, "66", 2),
(37, "352", 1),
(37, "256", 3),
(37, "152", 4),
(38, "5", 2),
(38, "12", 1),
(38, "15", 3),
(38, "18", 4),
(39, "70,57", 1),
(39, "71", 2),
(39, "75,47", 3),
(39, "73,27", 4),
(40, "33,8%", 2),
(40, "58,8%", 3),
(40, "15%", 4),
(40, "26,5%", 1),
(41, "200", 1),
(41, "160", 2),
(41, "120", 3),
(41, "240", 4),
(42, "8", 2),
(42, "17", 1),
(42, "113", 3),
(42, "176", 4),
(43, "408", 1),
(43, "318", 4),
(43, "292", 3),
(43, "202", 2),
(44, "Rp. 45.400,00", 1),
(44, "Rp. 46.400,00", 2),
(44, "Rp. 55.400,00", 3),
(44, "Rp. 56.400,00", 4),
(45, "3 1/4 Kg.", 2),
(45, "3 1/2 Kg.", 3),
(45, "4 1/4 Kg.", 4),
(45, "4 1/2 Kg.", 1),
(46, "Pukul 18.45", 3),
(46, "Pukul 19.15", 2),
(46, "Pukul 19.45", 4),
(46, "Pukul 20.15", 1),
(47, "Mempunyai empat sisi, mempunyai sepasang sisi sejajar, mempunyai dua sudut siku siku", 3),
(47, "Mempunyai empat sisi, mempunyai sepasang sisi sejajar yang tidak sama panjang, mempunyai dua pasang sudut sama besar.", 2),
(47, "Mempunyai empat sisi, mempunyai dua pasang sudut sama besar, mempunyai dua diagonal yang saling berpotongan dan tegak lurus.", 1),
(47, "Mempunyai empat sisi, mempunyai dua sudut siku siku, mempunyai dua diagonal yang saling berpotongan dan tegak lurus.", 4),
(48, "Menjual berita", 3),
(48, "Mencari berita", 2),
(48, "Menyiarkan berita", 1),
(48, "Menyunting berita", 4),
(49, "Permainan", 4),
(49, "Perlombaan", 2),
(49, "Pementasan", 1),
(49, "Pertandingan", 3),
(50, "Pembeli obat-obatan", 2),
(50, "Pembuat obat-obatan", 3),
(50, "Tempat menjual obat-obatan", 1),
(50, "Peminum obat-obatan", 4),
(51, "melainkan", 1),
(51, "yang", 4),
(51, "mungkin", 2),
(51, "dan", 3),
(52, "dan", 3),
(52, "sedangkan", 4),
(52, "tetapi", 1),
(52, "sebab", 2),
(53, "Aku kemarin ke Jakarta.", 3),
(53, "Aku kemarin bangun kesiangan.", 4),
(53, "Aku kemarin sakit demam, tetapi sekarang sudah sehat.", 1),
(53, "Ibuku kemarin pergi ke Surabaya.", 2),
(54, "Bagus, sayang warna lautnya kurang biru.", 1),
(54, "Jelek, buatlah lukisan yang lain saja.", 3),
(54, "Aku sangat menyukai lukisanmu.", 4),
(54, "Aku tidak punya pendapat apa-apa.", 2),
(55, "Rita anak yang manja", 4),
(55, "Rita anak yang baik dan ramah", 1),
(55, "Rita suka mencari muka", 3),
(55, "Rita anak yang ceria", 2),
(56, "Ambon, 10 Januari 1990", 1),
(56, "Ambon ; 10 Januari 1990", 3),
(56, "Ambon / 10 Januari 1990", 2),
(56, "Ambon : 10 Januari 1990", 4),
(57, "Tidak perlu dibesar-besarkan, masih banyak kesempatan.", 2),
(57, "Semoga dia menjadi juara.", 1),
(57, "Dia anak yang berbakat.", 4),
(57, "Hebat ya, aku ingin seperti dia.", 2),
(58, "(1)-(2)-(3)-(4)", 3),
(58, "(2)-(3)-(1)-(4)", 2),
(58, "(3)-(4)-(1)-(2)", 1),
(58, "(4)-(3)-(2)-(1)", 4),
(59, "ceria dan rajin", 1),
(59, "tidak mau mengalah", 3),
(59, "egois dan besar kepala", 4),
(59, "ramah dan baik", 2),
(60, "pesan anak kepada Baginda", 4),
(60, "harta yang harus dijaga", 3),
(60, "kejujuran lebih mulia dan berharga", 2),
(60, "pesan Baginda kepada anak nya", 1),
(61, "Bayu ingin bermain sepak bola, juga Agus.", 2),
(61, "Bayu bermain sepak bola, Agus ingin bermain sepak bola.", 4),
(61, "Bayu dan Agus ingin bermain sepak bola.", 1),
(61, "Bayu bermain sepak bola, Agus bermain sepak bola.", 3),
(62, "Berlari", 3),
(62, "Menunggu lampu hijau", 4),
(62, "Menoleh ke kanan, kiri, dan kanan", 1),
(62, "Menangis", 2); ''')
    
cursor.execute('''CREATE TABLE IF NOT EXISTS list_Nilai(
	username	VARCHAR(50),
	teske		INT(11),
    matpel VARCHAR(10),
	nilai 		INT(11),
   tingkat INT(11)
); ''')

db.commit()

#cursor.execute("SELECT * from pilihan")
#print(cursor.fetchall())
    