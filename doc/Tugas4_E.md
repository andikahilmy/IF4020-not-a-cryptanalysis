# IF4020 Kriptografi  - Tugas 4: Serangan terhadap RSA / RSA Attack 
## Daftar Isi
* [Identitas](#identitas) 
* [Bagian A](#bagian-a) 
* [Bagian B](#bagian-b)  
## Identitas 
Kelompok: E 
Anggota: 
- Christine Hutabarat (13520005)
- Fawwaz Anugrah Wiradhika Dharmasatya (13520086)
- Andika Naufal Hilmy (13520098)

## Bagian A
### Kasus A
#### Kelemahan
#### Serangan
#### Flag
#### Test Case
### Kasus B
#### Kelemahan
#### Serangan
#### Flag
#### Test Case
### Kasus C
#### Kelemahan
#### Serangan
#### Flag
#### Test Case
### Kasus D
#### Kelemahan
Kelamahan pada Kasus D adalah nilai kunci enkripsi (**e**) yang kecil, yakni hanya bernilai **3**. Hal ini menyebabkan untuk menemukan pesan asli, tidak perlu untuk mmencari kunci dekripsi. Cukup dipangkatkan dengan **1/e** saja.
#### Serangan
1. Dapatkan Nilai **n**, **e**, dan **c**.
2. Pangkatkan **c** dengan **1/e**. Karena di kasus ini diketahui **e=3**, maka kita bisa langsung akar kubikkan saja dengan bantuan fungsi **cbrt** dari pustaka **sympy** agar cepat.
#### Flag
#### Test Case
### Kasus E
#### Kelemahan
#### Serangan
#### Flag
#### Test Case
### Tautan Solusi
## Bagian B

