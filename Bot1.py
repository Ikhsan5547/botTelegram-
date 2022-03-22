import telebot
import requests
import os
import json
api = '5167888071:AAGTOe3pqE0XaqZPECdr8BBo4JR1CNx9Bf4'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Ketik /menu ketik /curhat untuk curhat ketik /jam Untuk Melihat Jam Ketik /Creator Untuk Melihat Pembuat Bot Ini ketik /info Untuk Melihat Informasi Bot Ketik /MenuDosa Untuk Menampilkan Pekob(Dilarang Untuk Anak Dibawah 18+) Ketik /CodeNuklirMenu Untuk Para Wibu ketik /nekoapp buat jadi bandar ketik /CersexMenu Untuk nganceng Ketik /ApkMod untuk Mod Apk ketik /akbarmenu Untuk orang Yang Bernama Akbar ketik /owner untuk chat owner ketik /scwa untuk memunculkan menu sc Ketik /snk Untuk Syarat Ketentuan Bot Telegram Ketik /Emulator Untuk Mendapatkan Emulator Game Jadul Ketik /NomorWaBot Untuk Mendapatkan Bot Wa Gratis ketik /ScTermuxMenu Untuk Jadi Hengkel')
    
@bot.message_handler(commands=['curhat'])
def send_welcome(message):
    bot.reply_to(message, '/GuaLagiSedih /gualagisenang')

@bot.message_handler(commands=['GuaLagiSedih'])
def send_welcome(message):
    bot.reply_to(message, 'Bodo Amat🗿')

@bot.message_handler(commands = ['gualagisenang'])
def send_welcome(message):
    bot.reply_to(message, 'Bodo Amat🗿')

@bot.message_handler(commands = ['Creator'])
def send_welcome(message):
    bot.reply_to(message, 'Create By Ikhsan Spesial Thanks To @Manybot and @BotFather')

@bot.message_handler(commands = ['info'])
def send_welcome(message):
    bot.reply_to(message, 'Bot Ini Adalah Sebuah Bot Termux Dengan Server Python Yang Dibuat Oleh Ikhsan Dengan Kerja Sama @BotFather Dan @Manybot')

@bot.message_handler(commands = ['MenuDosa'])
def send_welcome(message):
    bot.reply_to(message, '/Dosa1 /Dosa2 /Dosa3 /Dosa4')

@bot.message_handler(commands = ['Dosa1'])
def send_welcome(message):
    bot.reply_to(message, 'Semoga Elu Masuk Neraka:https://www.mediafire.com/file/h2nygxbyb6n9cyo/VID-20210107-WA1468.mp4/file')

@bot.message_handler(commands = ['Dosa2'])
def send_welcome(message):
    bot.reply_to(message, 'Semoga Elu Masuk next:https://www.mediafire.com/file/pk8hozohzdc076c/VID-20210107-WA1466.mp4/file')

@bot.message_handler(commands = ['Dosa3'])
def send_welcome(message):
    bot.reply_to(message, 'https://www.mediafire.com/file/112q3u286tnvzjo/VID-20210107-WA1467.3gp/file')

@bot.message_handler(commands = ['Dosa4'])
def send_welcome(message):
    bot.reply_to(message, 'https://www.mediafire.com/file/arpphhxsv94ak0r/VID-20210107-WA1462.mp4/file')

@bot.message_handler(commands = ['codenuklir1'])
def send_welcome(message):
    bot.reply_to(message, 'Gampang Mode :• https://nhentai.net/g/316755/• https://nhentai.net/g/316596/• https://nhentai.net/g/311850/• https://nhentai.net/g/315578/• https://nhentai.net/g/315488/• https://nhentai.net/g/315406/• https://nhentai.net/g/315344/• https://nhentai.net/g/315323/• https://nhentai.net/g/315136/• https://nhentai.net/g/315099/')

@bot.message_handler(commands = ['codenuklir2'])
def send_welcome(message):
    bot.reply_to(message, 'Medium Mode :• https://nhentai.net/g/316869/• https://nhentai.net/g/316785/• https://nhentai.net/g/316250/• https://nhentai.net/g/311283/• https://nhentai.net/g/265671/• https://nhentai.net/g/312127/• https://nhentai.net/g/311560/')

@bot.message_handler(commands = ['codenuklir3'])
def send_welcome(message):
    bot.reply_to(message, 'Hard Mode :• https://nhentai.net/g/316820/• https://nhentai.net/g/316481/• https://nhentai.net/g/316430/• https://nhentai.net/g/276347/• https://nhentai.net/g/196329/• https://nhentai.net/g/304543/• https://nhentai.net/g/295295/• https://nhentai.net/g/311262/• https://nhentai.net/g/311882/• https://nhentai.net/g/312180/')

@bot.message_handler(commands = ['CodeNuklirMenu'])
def send_welcome(message):
    bot.reply_to(message, '/codenuklir1 /codenuklir2 /codenuklir3')

@bot.message_handler(commands = ['owner'])
def send_welcome(message):
    bot.reply_to(message, 'Ni Owner Ku @Ikhsan5475:')

@bot.message_handler(message=['P'])
def send_welcome(message):
    bot.reply_to(message, 'Apa Bro')

@bot.message_handler(commands=['nekoapp'])
def send_welcome(message):
    bot.reply_to(message, 'ni link nya bro:https://linkpoi.cc/nekopoiapp')

@bot.message_handler(commands=['CersexMenu'])
def send_welcome(message):
    bot.reply_to(message, '/Cersex1 /Cersex2 /cersex3')

@bot.message_handler(commands=['Cersex1'])
def send_welcome(message):
    bot.reply_to(message, 'Hy nama ku Gery aku akan menceritakan pengalam sex ku yang cukup konyol tapi ini sangat menarik untuk saya ceritakan, Cerita ini di awali sejak saya kelas 5 SD, hmmm ini awal saya merasakan yang namanya s***e saya tidak bermaksud mengundang kalian melakukan ini, karena saya hanya membagikan pengalaman saya saja, cerita ini berawal dari saat saya sd kelas 5 saya merasakan rasanya sakit hati, tapi ini bukan karena cinta, ini karena ortu saya, ayah dan ibu saya sering bertengkar dan akhir nya ibu dan ayah saya berpisah, saya tidak tau kemana pergi nya ibu saya saat itu, hmm lalu saya tinggal dengan ayah saya dan selang 1 bulan ayah sayapun mau menikah, awal nya saya tidak setuju, tapi setelah saya di kenal kan dengan cewek baru ayah saya, ternyata dia masih muda usia nya 20 tahun, sedangkan ayah saya sudah 30 tahun, dan awal nya saya takut dengan dia, ternyata dia baik dia juga menggap saya seperti anak nya sendiri, dia yang saya maksud adalah calon ibu tiri saya, kemudian setelah saya kenalan 2 bulan saya mulai dekat dengan dia, dan ayah dan ibu baru sayapun menikah, sekarang saya sebut saja dia ibu saya, nah setelah 3 hari menikah nasib malang menimpa kami, saya, ibu, dan ayah saya pergi keluar membawa mobil dan mobil ayah saya mengalami rem blong, kami pun kecelakaan dan yang selamt cuma saya dan ibu saya, ibu sayapun menangis dan hancur sambil memeluk saya di waktu pemakaman ayah saya, dan ibu saya depresi dan berjanji kepada ayah saya akan menjaga saya dan tidak akan menikah, hmmm lalu setelah beberapa bulan sayapun naik kelas ke kelas 5 SD btw di awal itu saya kelas 4 yak, nah lalu ibu saya udah bisa melupakan semua itu tapi masih memegang janji nya, dan pada suatu hari saya kebelet pipis nah kebetulan waktu itu ibu saya lagi mandi pas saya pipis tanpa saya sadari di kamar mandi ada ibu saya yang sedang mandi, Toilet dan tempat mandi nya terpisah jadi saya tidak tau, nah waktu itulah pas saya mau keluar ibu saya keluar dari kamar mandi tanpa busana, dan saya mengintip dari toilet, nah lalu saya terpeleset dan jatuh, lalu ibu saya membantu saya, hmmm dia gak malu atau kaget mungkin karena dia sudah mengagap saya anak nya dan masih kecil jadi dia b aja, nah lalu saya memperhatikan dia terus sampai akhirnya burung saya berdiri 😂, nah lalu malampun tiba ibu saya kedatangan temen cewek nya, dan mengatakan soal hamil gitu lah, nah pas waktu itu saya lagi ada di tangga mau ambil air lalu ibu saya berkata ke temen nya, gimana mau hamil ngen*** aja gak pernah, cukup gery aja jadi anak ku karena aku udh berjanji sama makam ayah nya, dan bla bla bla, fokus aja ke pikiran saya dan saat itulah saya tau kalo ibu saya perawan, hehehe, lalu malam hari saya pura pura gak bisa tidur dan minta di temenin, lalu saya pun di peluk, dan dalam sudut pandang dia, dia memeluk anak nya saat Tidur, tapi saya melihat, cewek cantik pakai pakaian seksi memeluk saya, lalu saya di cium dan saya minta di lamain nah beberapa jam kemudian dia tertidur, dan kemudian ko**** saya berdiri, lalu aku mencari Video bo*** di internet lalu aku mau mempraktekan nya kepada ibu saya, lalu saya cium dulu ibu saya habis itu saya naikin daster nya, nah pas saya masukan kontol saya ke mulut nya dia tiba tiba bangun dengan kaget, saya pun kaget dan takut, lalu tiba tiba dia tersenyum lalu berkata, Kamu pengen?, lalu saya jawab maaf ma, aku gak lakuin apa apa sambil nangis😂😂, lalu dia ketawa dan membuka pakaian, lalu dia bilang udah jangan nangis,,sini mama kasih apa yang kamu kaasih,lalu aku pun di suruh masukin anu aku, lalu ah enak banget, lalu kami pun melakukan nya, sambil dia desah ah ah ah tapi pelan karena gak terlalu sakit, lalu kami pun semakin dekat, dan baru beberapa kali aku keluar masukin dia pun bilang stop, lalu dia bilang, bentar ya sayank mama mau beli kondo* dulu biar aman, lalu aku tanya apa itu kondo*, lalu di jelaskan, singkat nya setelah beli kami lanjut gitu, dan lalu waktu dah capek dn puas, Kami pun Tidur dan akhir nya kamipun tiap hari ena ena, dan mungkin ini udah lama, sampai sini aja, bye semua :)                                                 ')

@bot.message_handler(commands=['Cersex2'])
def send_welcome(message):
    bot.reply_to(message, 'Menu Ini Error Entah Kenapa')

@bot.message_handler(commands=['WaMods'])
def send_welcome(message):
    bot.reply_to(message, '*Download Wa [ HW MODS ] Anti Virus Di Bawah ini🤖*[ *https://www.mediafire.com/file/lvw4guvpz6bfmvh/WhatsApp_2.20.207.19.apk/file* ]')

@bot.message_handler(commands=['GTA'])
def send_welcome(message):
    bot.reply_to(message, 'BERIKUT ADALAH LINK GTA SAN ANDROID GRATIS TERBARU %day_of_week%/%day_of_month_short%/%month_name%/%year%*[ LINK APK: https://www.mediafire.com/file/z6ms3ovfqftzwsh/APK+GTA+SA+V1.0.8.7z/file ][ LINK OBB: https://www.mediafire.com/file/3xl7gqpoktukhg4/OBB+GTA+SA+ORIGINAL+V1.0.8.7z/file ]')

@bot.message_handler(commands=['Hentai'])
def send_welcome(message):
    bot.reply_to(message, 'Astafirullah Kawan ')

@bot.message_handler(commands=['hentai'])
def send_welcome(message):
    bot.reply_to(message, 'Astafirullah Kawan')

@bot.message_handler(commands=['Neko'])
def send_welcome(message):
    bot.reply_to(message, 'Astafirullah Kawan')

@bot.message_handler(commands=['neko'])
def send_welcome(message):
    bot.reply_to(message, 'Astafirullah Kawan')

@bot.message_handler(commands=['Loli'])
def send_welcome(message):
    bot.reply_to(message, 'Dasar Wibu')

@bot.message_handler(commands=['loli'])
def send_welcome(message):
    bot.reply_to(message, 'Dasar Wibu')

@bot.message_handler(commands=['ApkMod'])
def send_welcome(message):
    bot.reply_to(message, '/WaMods /GTA /Minecraft /KinemasterDiamond /AveePlayer /GeometryDash /Bullylite /ZARCHIVER /facebook /TeleGram /PixelLab /AlightMotion /Aspalthnitro /TotalConquest')

@bot.message_handler(commands=['Ara-Ara'])
def send_welcome(message):
    bot.reply_to(message, 'Pergi Ke Vtuber Ngab')

@bot.message_handler(commands=['Ara-ara'])
def send_welcome(message):
    bot.reply_to(message, 'pernah ke Vtuber Ngab')

@bot.message_handler(commands=['ara-ara'])
def send_welcome(message):
    bot.reply_to(message, 'Pergi Ke Vtuber Ngab')

@bot.message_handler(commands=['AraAra'])
def send_welcome(message):
    bot.reply_to(message, 'Pergi Ke Vtuber Ngab')

@bot.message_handler(commands=['Araara'])
def send_welcome(message):
    bot.reply_to(message, 'Pergi Ke Vtuber Ngab')

@bot.message_handler(commands=['araara'])
def send_welcome(message):
    bot.reply_to(message, 'Pergi Ke Vtuber Ngab')

@bot.message_handler(commands=['Bokep'])
def send_welcome(message):
    bot.reply_to(message, 'Astafirullah Kawan')

@bot.message_handler(commands=['bokep'])
def send_welcome(message):
    bot.reply_to(message, 'Astafirulilah Kawan')

@bot.message_handler(commands=['covidindo'])

def sambutan_start(message):

    api = requests.get('https://api.kawalcorona.com/indonesia/')
    api_json = api.json()
    api_content = api_json
    for wan in api_content:
         negara = api_content[0]['name']
         positif = api_content[0]['positif']
         sembuh = api_content[0]['sembuh']
         meninggal = api_content[0]['meninggal']
         dirawat = api_content[0]['dirawat']
         kirim = ('''
Negara = {}
Positif = {}
Sembuh = {}
Meninggal = {}
Dirawat = {}
'''.format(negara,positif,sembuh,meninggal,dirawat))
         wans.reply_to(message, kirim)

@bot.message_handler(commands=['Minecraft'])
def send_welcome(message):
    bot.reply_to(message, 'Minecraft (Original)https://www.mediafire.com/file/4hixmktsfkhky91/Minecraft_v1.16.101.01_Terbaru.zip/file')

@bot.message_handler(commands=['KinemasterDiamond'])
def send_welcome(message):
    bot.reply_to(message, 'Kinemaster Diamond (MOD)https://www.mediafire.com/download/9p8wsnwupnq0lun')

@bot.message_handler(commands=['AveePlayer'])
def send_welcome(message):
    bot.reply_to(message, 'Avee Player (PRO)https://www.mediafire.com/download/5vkde8d1gcyk33y')

@bot.message_handler(commands=['AlightMotion'])
def send_welcome(message):
    bot.reply_to(message, 'http://www.mediafire.com/file/tpxj2grwf8imp6i/Alight_Motion_V.3.1.4_%2528Mod%2529_By_bilqis_neha.apk/file') 

@bot.message_handler(commands=['PixelLab'])
def send_welcome(message):
    bot.reply_to(message, 'Inshot (PRO)https://www.mediafire.com/download/7qcmrfdy2o1ynxf')

@bot.message_handler(commands=['GeometryDash'])
def send_welcome(message):
    bot.reply_to(message, 'Geometry Dash (MOD)http://www.mediafire.com/file/thnoi1wpa5ex2wn/Geometry_Dash_%2528MOD%2529.apk/file')

@bot.message_handler(commands=['Bullylite'])
def send_welcome(message):
    bot.reply_to(message, '*BULLY ANDROID HANYA SUPPORT ANDROID 8 KE ATAS*LINK: https://www.mediafire.com/file/m9tocfh4emo2wds/BULLY_MOD_2020_BY_BANG_BOR.7z/file')

@bot.message_handler(commands=['ZARCHIVER'])
def send_welcome(message):
    bot.reply_to(message, 'BERIKUT ADALAH LINK ZARCHIVER PRO MOD TERBARU  Link:Rusak')

@bot.message_handler(commands=['facebook'])
def send_welcome(message):
    bot.reply_to(message, 'LINK: https://m.apkpure.com/id/delta-fb-lite-pro/gudaljaran.jaranpolah.deltafblitepro/download ]')

@bot.message_handler(commands=['TeleGram'])
def send_welcome(message):
    bot.reply_to(message, 'LINK: https://gamestoremobi.com/id/telegram.html ]')

@bot.message_handler(commands=['listhp'])
def send_welcome(message):
    bot.reply_to(message, '/Samsung /Oppo /Realme /Xiaomi /Redmi /')

@bot.message_handler(commands=['Samsung'])
def send_welcome(message):
    bot.reply_to(message, '1. Samsung Galaxy M30s   Harga: Rp 3.299.000Hp samsung galaxy m30s tl                               Spesifikasi Samsung Galaxy M30s:        Layar: 6,4” FHD+Super AMOLED Infinity-U    DisplayDimensi: 159 x 75,1 x 8,9  mm     SIM Card: Dual SIM (SIM 1 + SIM 2 + MicroSD)                                     Kamera: Main: 48MP, F2.0 Ultra Wide: 8MP, F2.2 (123o)Depth: 5MP, F2.0          Chipset: Exynos 9611                Prosesor: Octa Core 2.3GHz,1.7GHz         OS: Android 9.0 (Pie)                  Memori: 4GB RAM 64 GBInternalStorage MicroSD Up to 512GB                Biometrik: Rear Fingerprint            Baterai: 6.000 mAh dengan teknologi Fast Charging                               Warna: Black, Blue, White Desain: Glossy Plastic                                     2. Samsung Galaxy A20sHarga: Rp 2,4 juta Hp samsung terbaru galaxy a20s   Spesifikasi Samsung Galaxy A20s:9     Display: IPS LCD, 6.5 inches, 103.7 cm2 (~81.9% screen-to-body ratio)              Resolusi: 720 x 1560 pixels, 19.5:9 ratio (~264 ppi density)                        OS: Android 9.0 (Pie)                Chipset: Qualcomm SDM450 Snapdragon 450 (14 nm)                                       CPU: Octa-core 1.8 GHz Cortex-A53        GPU: Adreno 506                          RAM: 3/32GB, 4/64GB                    Memori eksternal: microSD, up to 1 TB (dedicated slot)                      Kamera Utama: Triple (13 MP, f/1.8, 27mm (wide), PDAF; 5 MP, f/2.2, 13mm (ultrawide); 5 MP); f/2.2, depth sensor; LED flash, panorama, HDRVideo: 1080p@30fps        Kamera Selfie: 8 MP, f/2.0               NFC: Tidak ada                           USB: Type-C 1.0 reversible connector Baterai: Li-Po 4000 mAh, Fast battery charging 15W                             Warna: Black, Blue, Red, Green                                                                        3. Samsung Galaxy A10S harga: Rp 1.899.000s                    samsung galaxy a10s                 Spesifikasi Samsung Galaxy A10s:      Dimensi: 156.9 x 75.8 x 7.8mm           Warna: Merah, Hijau, dan Hitam          Layar: 6.2-inch HD+ (720×1520)PLS, Infinity Display                                 Kamera belakang: 13MP (F1.8) + 2MP (F2.4)Kamera selfie: 8MP (F2.0)                OS: Android 9.0 (Pie)                     RAM: 2GB RAM                              ROM: 32GB                             Memori eksternal: Micro SD slot (up to 512GB)                               Baterai: 4000 mAh                   Biometric Authentications: Rear Fingerprint,Face Recognition')

@bot.message_handler(commands=['akbarmenu'])
def send_welcome(message):
    bot.reply_to(message, '/Akbar1 /Akbar2 /Akbar3 /Akbar4')

@bot.message_handler(commands=['Akbar1'])
def send_welcome(message):
    bot.reply_to(message, 'https://ngewibusite.wordpress.com/')

@bot.message_handler(commands=['Akbar2'])
def send_welcome(message):
    bot.reply_to(message, 'https://wibu-elit.blogspot.com/2021/10/tongkrongan-tempat-kumpul-wibu.html?m=1')

@bot.message_handler(commands=['Akbar3'])
def send_welcome(message):
    bot.reply_to(message, 'https://www.elinotes.com/2020/11/kumpulan-situs-tempat-mencari-gambar.html?m=1')

@bot.message_handler(commands=['Akbar4'])
def send_welcome(message):
    bot.reply_to(message, 'https://id.pinterest.com/Ale_Zlavor/wibu/')

@bot.message_handler(commands=['sc1'])
def send_welcome(message):
    bot.reply_to(message, 'scwa AutoResponder by Zellbotz [https://www.mediafire.com/file/hihfaxjmqqvyacj/ZeilBotz_V.1%25E3%2580%25BD%25EF%25B8%258F.7z/file]')

@bot.message_handler(commands=['sc2'])
def send_welcome(message):
    bot.reply_to(message, 'https://github.com/RzLModz/R [Bot Termux] by Rxlmodz')

@bot.message_handler(commands=['sc3'])
def send_welcome(message):
    bot.reply_to(message, 'https://www.mediafire.com/file/gdk5oqvtljqrfdi/v16.7z/file [Bot Termux] By Ramdani Official')

@bot.message_handler(commands=['sc4'])
def send_welcome(message):
    bot.reply_to(message, 'https://zeeoneofc.blogspot.com/?m=1 [Bot Termux By Zeeoneofc]')

@bot.message_handler(commands=['sc5'])
def send_welcome(message):
    bot.reply_to(message, ':https://github.com/sanzykawaiiii/SanzyMDV3 [Bot Termux by SanzyMDV3]')

@bot.message_handler(commands=['MyBoy'])
def send_welcome(message):
    bot.reply_to(message, 'https://play.google.com/store/apps/details?id=com.fastemulator.gbafree')

@bot.message_handler(commands=['NES'])
def send_welcome(message):
    bot.reply_to(message, 'https://play.google.com/store/apps/details?id=com.super8bit.free')

@bot.message_handler(commands=['CaraPemasangan'])
def send_welcome(message):
    bot.reply_to(message, '/ScTermux /ScAutoresponder')

@bot.message_handler(commands=['ScTermux'])
def send_welcome(message):
    bot.reply_to(message, '[apt update && apt upgrade]~~~[pkg install bash]~~~[pkg install nodejs]~~~[pkg install ffmpeg]~~~[pkg install nodejs-ls]~~~[pkg install libwebp]~~~[pkg install imagemagick]~~~[pkg update && pkg upgrade]~~~[termux-setup-storage]~~~[cd NamaBotlu]~~~npm start (Setiap Sc Berbeda Commands Lihat Di Yt)')

@bot.message_handler(commands=['ScAutoresponder'])
def send_welcome(message):
    bot.reply_to(message, 'Unduh Apk AutoResponder:[https://www.mediafire.com/file/dqnev954m0jkott/com.mod.autoresponder.for.wa.mod.apk.2.4.9.premium.unlocked2.4.9.zip/file [(Not Respon Ganti versi )]    ([Tekan Titik 3][Tekan Import aturan][Cari Tempat Config Dengan Format csv])')

@bot.message_handler(commands=['scwa'])
def send_welcome(message):
    bot.reply_to(message, '/sc1 /sc2 /sc3 /sc4 /sc5 /CaraPemasangan')

@bot.message_handler(commands=['CaraPemasangan'])
def send_welcome(message):
    bot.reply_to(message, '/ScTermux /ScAutoresponder')

@bot.message_handler(commands=['Aspalthnitro'])
def send_welcome(message):
    bot.reply_to(message, 'https://www.mediafire.com/file/kgf4zju72u86gdd/Asphalt-Nitro-mod-apk-v1.7.4a.Password.7z/file [PW:ADA DI VIDEO]')

@bot.message_handler(commands=['TotalConquest'])
def send_welcome(message):
    bot.reply_to(message, 'https://www.mediafire.com/file/66sl3rmim9vsxmr/Total%252BConquest%252BFeris_Tukang_Mod.apk/file')

@bot.message_handler(commands=['cersex3'])
def send_welcome(message):
    bot.reply_to(message, 'Erly Gadis PerawanKuperkenalkan dulu diriku, aku seorang yang berasal dari keluarga sederhana. Namaku Heri, umurku sekarang 23 tahun,aku akan menceritakan awal mula pertama kali melakukan hubungan badan dengan lawan jenis. Saat itu usiaku 18 tahun, aku baru saja lulus dari SMK swasta di kotaku, boleh dikata nilai ijazahku sangat memuaskan,lalu aku melamar pekerjaan ke salah satu perusahaan otomotif terkemuka di negeri ini, disaat aku menunggu panggilan kerja, Om ku datang menawarkan pekerjaan buat aku, katanya ada lowongan di tempat om bekerja, tapi posisinya sebagai OB alias appointment boy,waduuh apes banget gue, begitu ada yang nawarin pekerjaan tapi Cuma sebagai OB”pikirku, tapi nggak apa dech, itung- itung ngisi waktu buat nunggu panggilan kerja. Dihari pertama aku kerja di tempat om ku, sungguh diluar dugaanku. Ternyata karyawan ceweknya cantik2, banyak lagi. Wah kesempatan nih mumpung aku lagi jomblo, siapa tahu ada karayawati om yang mau sama aku,gumamku. Aku melihat salah seorang karyawati yang kuketahui bernama Erly, orangnya cantik, putih, tinggi badan kurang lebih 168 cm, ukuran bra kira-kira 36 C ditambah bodinya yang aduhai karena dia giat banget fitness,apalagi pantatnya yang besar,kalau dia lagi jalan,pantatnya naik turun yang bikin pikiran cowok yang memandangnya ingin meremas pantatnya,pernah suatu hari aku melihatnya diruang blow room,dia sedang menanggalkan blouse atasnya,saat itu aku liat dia Cuma pakai hem warna putih transparant yang seakan-akan terlalu kecil buat dia,seakan-akan ada yang nggak muat dibalik bajunya,mungkin karena teteknya terlalu gede kali,wah..wah..montok banget nih cewek, aku sudah membayangkan bagaimana kalau aku bisa meluk dia…pastinya angeeeet banget,Aku mulai cari informasi mengenai dia,apa yang dia suka dan apa yang dibencinya,tiap kali bertemu dia,aku selalu menyapanya..diapun membalas sapaanku..ada kemajuan nih pikirku. Selang waktu 2 bulan, keakraban kami bukan lagi sebagai atasan dan bawahan,saat aku capital kerumahnya diapun menyambutku dengan ramah.Sudah saatnya aku mengungkapkan perasaanku kalau aku sayang padanya.”Er aku mau ngomong sesuatu sama kamu,sebenarnya aku sudah absolutist pengin ngomong ini”dia jawabngomong aja,”aku sebenarnya sayang sama kamu, kamu mau kan jadi pacar aku?lalu dengan ekspresi kaget di jawab” Her, berarti selama ini kamu salah tafsir tentang kebaikanku ke kamu,aku Cuma nganggap kamu teman,lagian kedudukan kita berbeda,aku sekretaris kantor sedangkan kamu Cuma OB”saat itu aku bagaikan tersambar petir,bukan masalah aku ditolak, tapi dia sudah menghina aku dengan kata-kata seperti itu.Saatnya aku bikin perhitungan sama dia,nggak masalah aku ditolak,tapi aku harus bikin dia takluk sama aku…besok harinya kebetulan dia kerja lembur karena dapat banyak tugas dari om ku,seandainya dia aku perkosa,jelas sekali kalau dia akan mengadukan aku ke polisi, tapi kalau aku bius, darimana aku bisa dapat Chloroform?akhirnya aku dapat ide, temenku pernah cerita kalau minuman bersoda bermerek s***** dicampur salah satu obat tetes mata I****,bisa bikin orang teler alias pingsan,segera aku membeli minuman serta obat tersebut. Begitu aku sampai kantor, aku campur minuman tadi dengan obat tetes mata dengan dosis beberapa 2 tetes, aku pura2 ngasih sama dia minuman tadi, dengan alasan sebagai permintaan maaf atas kelancanganku dan berharap kita masih bisa temenan, awalnya dia nolak,tapi aku bilang ke dia kalau aku nggak ada maksud lain…biar tidak curiga lalu aku pura2 ijin pulang,tapi sebenarnya aku sembunyi di allowance direksi,aku intip dia dari ruang itu,aku liat dia mulai teguk minuman yang aku kasih tadi,ternyata benar juga,dalam hitungan menit dia langsung jatuh pingsan diatas kursi kerjanya,wah inilah kesempatanku,aku datangi dia lalu aku coba bangunin dia,siapa tau dia Cuma tertidur….aku colek tangannya dia diem,lalu aku colek teteknya,dia tetep diem…ehhh ternyata beneran dia pingsan,dia kusandarkan dikursi,aku jongkok didepannya,lalu aku peluk dia erat2,akhirnya apa yang aku impikan selama ini tercapai,awalnya aku remas teteknya yang gede itu dari luar pakaiannya,wihh kenyal banget pentilmu Er,ooohhh…enak banget Erly,lalu aku mulai mencium bibirnya yang seksi,aku kulum sampai bibirnya memerah,slurp…oh enak banget…slurp…slurp, aku mulai turun mencumbu lehernya,lalu melepas blousenya, mulai kubuka kancing bajunya satu persatu,wowwww……tiba tiba aku terbelalak seakan tak percaya dengan apa yang aku lihat,tetek loe gede banget Er,ini beneran tetek? Kok bent segedesemangka gini…???lalu aku lanjutin membuka BH nya,wiiiii… what a nice tits babe…..aku rasa tetekmu ini lebih dari 36 C,atau mungkintepatnya 39 C, American cup admeasurement man..pokoknya malam ini loe harus muasin gue,mulai kukulum putingnya yang berwarna merah muda,dan putingnya yang belum nongol,apa mungkin dia sama sekali belum dijamah sama cowok ya? Pikirku,aku mulai menjilati ujung teteknya, kadang aku gigit sampai ada bekas di teteknya,aku makin bergairah saja,aku remas teteknya yang kenyal banget, habisnya kayak bola karet,he..he..kukulum2 sampai putingnya mulai mengeras,lalu aku mulai menjilati pusarnya dan akhirnya kulepas roknya yang seksi itu,Erly aku udah nggak sabar nih,pengin masukin kon***ku ke lubang vag***mu, begitu roknya terlepas dari kakinya,kulihat celana dalamnya yang makin bikin aku bertambah gairah, dia memakai tounge G-string(celana dalam seksi yang kayak tali),yang biasa dipake bule saat berjemur di pantai (kayak yang aku liat di tivi),transparan lagi….aku jilati pahanya yang putih mulus,lalu aku sampai pada ujung pangkal pahanya,mulai kuturunkan celana dalamnya,pelan-pelan aku menghayati aksiku,aku lihat pemandangan yang luar biasa,vag***nya menggelembung kayak seonggok daging,dan mataku tertuju pada klitorisnya yang sedikit basah kemerahan,dengan ditumbuhi bulu halus disekitar agency kewanitaannya.Waduh harus cepet-cepet nih masukin barang gue,udah ngaceng keatas gini…aku mulai menjilati dengan ganasnya,lalu aku buka bibir kemaluannya,kujilati terus tanpa henti,Erly ini saatnya gue masukin tongkol gue ke vag*** loe,kon*** gue udah nggak tahan nih,aku tanggalkan semua pakaianku,kini kami berdua telanjang tanpa sehelai benangpun,aku geser tubuhnya sedikit lalu aku angkat kaki kanannya…..aku tempelkan kon***ku ke vaginanya,mula-mula kugosokkan pelan-pelan mulai dari bibir atas vag***nya yang sudah basah oleh liurku,ini backbone sih lubangnya? Susah amat nyarinya,pembaca harap maklum, saat itu aku baru pertama kali ngelakuin yang namanya chargeless sex,begitu ketemu,aku tekan maju mundur dengan pelan2,kok sempit banget pikirku…oke,aku akan paksa kont**ku ngambil perawan loe Er..satu..dua..tiii..gaaaaa…preeet..preett,kok kayak ada yang sobek?? Tapi apa’an ya,awwwww yes…kont**ku dah masuk separuh,tapi rasanya ada yang ngilu di pusakaku ini,kayak kejepit pintu..tapi bedanya ini rasanya enak banget,kutarik pelan-pelan,kudorong lagi..blesssss..akhirnya kont**ku masuk sepenuhnya,lalu mulai kugenjot dia sampai teteknya yang montok itu bergoyang keatas dan kebawah,Er enak banget memiawloe,udah cantik,putih,montok ditambah memiawmu yang sempit ini,beruntung banget aku….kugenjot dia selama setengah jam,Er gue mau kluar nih,kluarin didalem aja ya….langsung kuluberkan spermaku kedalam vag***nya crooott…croott,ohhh…ohhh… begitu kont** aku tarik keluar,ada bekas noda darah dikemaluanku, juga pada memiawnya,ternyata dia masih perawan ooiiii….lumayan ML pertama kali dapet bidadari perawan,setelah istirahat 5 menit,kuangkat dia keatas meja,kutaruh dia dengan posisi tengkurap,lalu aku ent*t lagi memiawnya dari belakang,kuremas teteknya,oohhh..opffhh….yes…oh my god…(biar kayak di film2 porno gitu),enak er…terusin ya sayang,aku lebarkan lagi kakinya dengan posisi badan membungkuk diatas meja,kupeluk dia sambil terus meremas toketnya yang yahud,sampai-sampai genjotanku terdengar suara..creeek..creeek…ccreeek…aku masih belum puas,lalu kurapikan lagi pakaiannya,mulai dari baju, blouse sampai roknya,tapi tanpa BH dan celana dalamnya,gue akan lebih puas kalau ngent*t loe dengan pakaian utuh,biar kayak karyawan kantor yang lagi ngelakuin activity secara sembunyi,lalu aku duduk dikursi,kutaruh dia diatasku dengan posisi membelakangiku,tangan kiriku meremas teteknya dari belakang,sedang tangan kananku menelusup kedalam roknya,aku arahkan lagi rudalku kearah vag***nya,dan bleeess…ohhh…enak banget Erly,oohhh…ngent*t loe dari belakang sambil megang toket loe,oohh..nggak tahan neh Er,gue mau keluar lagi nih….croott..croott…legaaa….aku bangun lagi,lalu aku telentangkan dia dilantai,kubuka lagi kancing bajunya,Erly aku pengin ngent*t toket loe nih….kuhisap dulu pentilmu ya,sluuuurp….sluuuurp…segeeeerr….enaaak banget kalo minum susu dari sumbernya,lalu kutaruh ludahku ditengah toketnya yang putih mulus itu,biar licin gitu….kutempatkan kont**ku di situ,kutekan toketnya dari samping kiri kanan biar bisa menjepit kont**ku,mulai ku maju mundurkan rudalku,,wowwwww…..what absurd tits honey,I ‘d never acquainted like this afore ( ya iyalaaahh,namanya juga baru pertama kali ngesexnya),kont**ku Cuma kliatan helmnya,seakan-akan kont**ku tertelan sama toketnya erly,,apalagi saat aku duduk diatas tubuhnya,pantatku terasa angeet banget,dan pahaku terasa bergetar saat terbentur toketnya yang montok dan kenyal itu,makin kupercepat gerakanku,makin terasa nikmat…ploook…plokk…plook…ohhhh…aohhhh…terusin ya sayang,toketmu bener2 luar biasa,sambil aku remas pentilmu yang gede dan putih ini,putingmu aku pelintir ya,biar makin nongol keatas,babe,my agent appetite to cum’….mau kluar nih saying,udah nggak tahan,crooottt…crooot….crooottt….spermaku keluar membasahi wajahnya yang cantik,,thanks honey…malam ini gue bener-bener puas,loe udah ngelayanin gue sampai kont**ku nggak sanggup berdiri lagi,lalu aku ambil tisu sama air buat bersihin dia,lalu kurapikan pakaiannya seakan-akan tak terjadi apa-apa,nggak terasa sudah 3 jam aku melampiaskan nafsuku sama erly,saat aku hendak keluar dari ruangan tersebut…tiba-tiba……terdengar suara seorang cewek yang memanggilku, mas….mas heri bangun…udah siang nih…mau narik nggak….jam segini masih molor,ooohhh sialan ternyata semua Cuma khayalan mimpiku,aku dibangunin sama istriku yang namanya juga erly tapi jauh banget dari apa yang aku impikan tadi,dia gendut, pendek,kulitnya item,ditambah lagi kerjanya sebagai penjual jamu gendong, sedangkan aku sendiri bekerja sebagai tukang becak……')

@bot.message_handler(commands=['snk'])
def send_welcome(message):
    bot.reply_to(message, 'Syarat dan Ketentuan Bot ❗1. Teks dan nama pengguna Telegram anda akan kami simpan di dalam server selama bot aktif 2. Data anda akan di hapus ketika bot Offline 3. Kami tidak menyimpan gambar, video, file, audio, dan dokumen yang anda kirim 4. Kami tidak akan pernah meminta anda untuk memberikan informasi pribadi 5. Jika menemukan Bug/Error silahkan langsung lapor ke Owner bot 6. Apapun yang anda perintah pada bot ini, KAMI TIDAK AKAN BERTANGGUNG JAWAB! Thanks !')

@bot.message_handler(commands=['sc'])
def send_welcome(message):
    bot.reply_to(message, 'Sc Bot Ini Masih Private Jika Mau Saya Jual Harga 10.000 Buat Beli Kuota🗿')

@bot.message_handler(commands=['Emulator'])
def send_welcome(message):
    bot.reply_to(message, '/NintendoDs /Nintendo3DS /PPSSPP /ePSxe /DamonPs2 /MyBoy /NES')

@bot.message_handler(commands=['NintendoDs'])
def send_welcome(message):
    bot.reply_to(message, '.mediafire https://www.mediafire.com/file/53gdck3u20hvxl6/DraStic_DS_Emulator_r2.5.2.2a_apkmody.io.apk/file')

@bot.message_handler(commands=['Nintendo3DS'])
def send_welcome(message):
    bot.reply_to(message, '.mediafire .mediafire https://www.mediafire.com/file/h2brngsd020c430/CITRA_SETUP_BY_GLITCHER.7z/file [PW:subscribe]')

@bot.message_handler(commands=['PPSSPP'])
def send_welcome(message):
    bot.reply_to(message, 'LINK ERROR')

@bot.message_handler(commands=['ePSxe'])
def send_welcome(message):
    bot.reply_to(message, 'https://youtu.be/X7k131njxqM (INI NGAB )')

@bot.message_handler(commands=['DamonPs2'])
def send_welcome(message):
    bot.reply_to(message, 'https://youtu.be/sYf1KfDqVok (Ni Ngab)')

@bot.message_handler(commands=['NomorWaBot'])
def send_welcome(message):
    bot.reply_to(message, 'Botnya Masih Baru (Awali Perintah dengan #menu.)                   wa.me/6281227144597 | wa.me/6281548429317 | wa.me/6285939425191 | wa.me/6289601147681 | wa.me/6281260037745 | wa.me/6285795035418 | wa.me/6289602542305 | wa.me/6281311419508 | wa.me/6282137579031 | wa.me/6285161551745 | wa.me/6285226629295 | wa.me/994405374076   | wa.me/6283114031932 | wa.me/6289515488433 | wa.me/6281278895286 | wa.me/6281363484604 | wa.me/62895336918539 | wa.me/6288212465570| wa.me/6289512129763 | wa.me/62881037526876 | wa.me/6281299038342 | wa.me/6282214772787 | wa.me/6283170498920 | wa.me/62895326097674')

@bot.message_handler(commands=['audio'])
def text(message):
       chatid = message.chat.id
       bot.send_audio(chat_id, open('contoh.mp3','rb'))

@bot.message_handler(commands=['ScTermuxMenu'])
def send_welcome(message):
    bot.reply_to(message, '/darkfb /phising /nmap /lazymux /bughunter')

@bot.message_handler(commands=['darkfb'])
def send_welcome(message):
    bot.reply_to(message, 'TOOLS DARK FB V1.9   [pkg install git python2]~~~[pip2 install mechanize requests]~~~[git clone https://github.com/storiku/darkfb1.9]~~~[cd darkfb1.9]~~~[python2 dark.pyc]            ID: Termux             Pass: omaliptv')

@bot.message_handler(commands=['phising'])
def send_welcome(message):
    bot.reply_to(message, '[pkg update && upgrade]~~~[pkg install wget]~~~[pkg install ssh]~~~[pkg install php]~~~[git clone https://github.com/xHak9x/SocialPhish]~~~[cd SocialPhish]~~~[chmod +x *]~~~[./socialphish.sh]')

@bot.message_handler(commands=['nmap'])
def send_welcome(message):
    bot.reply_to(message, '[pkg update && upgrade]~~~[pkg install nmap]~~~[nmap [Scan Type(s)] [Options] {target specification}]')

@bot.message_handler(commands=['lazymux'])
def send_welcome(message):
    bot.reply_to(message, '[apt update && apt upgrade]~~~[apt install git]~~~[apt install python]~~~[apt install python2]~~~[git clone https://github.com/Gameye98/Lazymux.git]~~~[cd Lazymux]~~~[python2 lazymux.py]')

@bot.message_handler(commands=['bughunter'])
def send_welcome(message):
    bot.reply_to(message, '[pkg update && pkg upgrade]~~~[pkg install python]~~~[pkg install python2]~~~[git clone https://github.com/thehackingsage/bughunter.git]~~~[cd bughunter]~~~[chmod +x bughunter.py]~~~[]')

print ("Bot Berjalan......")
print ("Creator By Ikhsan Spesial Thanks To @BotFather and @Manybot")
print ("◢▃▃▃▃◤▔▔▔◥▃▃▃▃◣✺�𝙷𝙰𝙲𝙺 ☬𝐂𝐲𝐛𝐞𝐫𝐓𝐞𝐚𝐦�✺ ◥▔▔▔▔◣▃▃▃◢▔▔▔▔◤")
print ("◥🄼🄾🄱🄸🄻🄴◤ ╭═══════╮╰═══════╯◢🄻🄴🄶🄴🄽🄳◣")

bot.polling()