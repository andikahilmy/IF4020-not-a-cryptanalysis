# IF4020 Kriptografi - Tugas 4: Serangan terhadap RSA / RSA Attack

## Daftar Isi

- [Identitas](#identitas)
- [Bagian A](#bagian-a)
- [Bagian B](#bagian-b)

## Identitas

Kelompok: E
Anggota:

- Christine Hutabarat (13520005)
- Fawwaz Anugrah Wiradhika Dharmasatya (13520086)
- Andika Naufal Hilmy (13520098)

## Bagian A

### Kasus A

#### Kelemahan

Kelemahan pada Kasus A terdapat pada pembangkitan nilai **p** dan **q** seperti yang ditunjukkan oleh baris berikut

```
p = nextprime(getStrongPrime(1024) - ran)
q = nextprime(nextprime(nextprime(nextprime(p) + ran) + ran) - ran)
```

Nilai `ran` berada pada range [1,100]. Karena nilai tersebut tidak terlalu besar jika dibandingkan dengan bilangan prima 1024 bit, maka nilai **p** tidak akan jauh berbeda atau bahkan sama dengan nilai `getStrongPrime(1024)` yang dihasilkan.

Hal yang sama berlaku pada pembangkitan nilai **q**. Karena nilai **q** hanya mengandalkan bilangan prima lain yang berada sebelum atau sesudah **p**. Oleh karena itu, nilai **p** dan nilai **q** tidak terlalu berbeda jauh dengan `p < q`. Hal ini menyebabkan nilai **n** mendekati kuadrat dari salah satu nilai **p** atau **q**.

#### Serangan

1. Cari akar kuadrat dari **n** dengan menggunakan fungsi **isqrt** dari pustaka **math**. Untuk tahap berikutnya nilai ini akan disebut sebagai **sqrt_n**.
2. Hitung beberapa nilai prima terdekat dari **sqrt_n** menggunakan fungsi **nextprime** dan **prevprime** dari pustaka **sympy**. Pada program solver, diambil bilangan prima yang lebih kecil dari **sqrt_n** sebagai nilai **p** yang potensial.
3. Dari setiap kemungkinan nilai **p**, hitung nilai **q** yang bersesuaian dengan `p * q = n` dan `GCD(e, (p-1)*(q-1) == 1)`.

#### Test Case

### Kasus B

#### Kelemahan

#### Serangan

#### Test Case

### Kasus C

#### Kelemahan

#### Serangan

#### Test Case

### Kasus D

#### Kelemahan

Kelamahan pada Kasus D adalah nilai kunci enkripsi (**e**) yang kecil, yakni hanya bernilai **3**. Hal ini menyebabkan untuk menemukan pesan asli, tidak perlu untuk mmencari kunci dekripsi. Cukup dipangkatkan dengan **1/e** saja.

#### Serangan

1. Dapatkan Nilai **n**, **e**, dan **c**.
2. Pangkatkan **c** dengan **1/e**. Karena di kasus ini diketahui **e=3**, maka kita bisa langsung akar kubikkan saja dengan bantuan fungsi **cbrt** dari pustaka **sympy** agar cepat.

#### Test Case

### Kasus E

#### Kelemahan

Kelemahan pada Kasus E adalah nilai **n** adalah bilangan prima, sehingga untuk mendapatkan totien n tinggal kurangkan saja **n** dengam 1. Jika totien **n** sudah didapat, _inverse modulo_-kan saja dengan **e** untuk mendapatkan kunci dekripsi.

#### Serangan

1. Dapatkan Nilai **n**, **e**, dan **c**.
2. Kurangan **n** dengan **1** untuk mendapatkan totien n.
3. _Inverse modulo_-kan **e** dengan modulo totien n. Hasil **inverse** merupakan kunci dekripsi.

#### Test Case

### Flag

### Tautan Solusi

- Tautan Repositori: [GitHub](https://github.com/dawetmaster/IF4020-not-a-cryptanalysis)
- Solver Bagian A berada di `src/solver_A.py`.

## Bagian B
