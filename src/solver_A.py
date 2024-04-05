from sympy import cbrt
import pwn

# Note: Cuma bisa di Linux (Windows gak support modul pwn)

CONTEXT = 'local'
PYTHON_TYPE = 'python3' 

def solve_A()->int:
  pass

def solve_B()->int:
  pass

def solve_C()->int:
  pass

def solve_D(c:int)->int:
  m = cbrt(c)
  return int(m)

def solve_E()->int:
  pass

def set_context(mode:str)->pwn.remote|pwn.process:
  #mode: 'local','remote'
  if(mode=='remote'):
    return pwn.remote("65.232.161.196", 4020)
  else:
    return pwn.process([PYTHON_TYPE,"source_A.py"])

if __name__=="__main__":
  # c = int(input("c:"))
  # m = solve_D(c)
  # print(m.to_bytes(21,'big'))
  context:pwn.remote | pwn.process = set_context(CONTEXT)

  # iteration
  iterations = int(input("Masukkan Jumlah Iterasi:"))

  # skip pesan awalnya
  context.recvuntil(b":D\n\n")
  
  # lakukan iterasi
  for _ in range(iterations):
    # print tahap sekarang
    print(context.recvline(keepends=False))
    # skip baris
    context.recvline()
    #dapetin paket soal
    paket_soal = context.recvuntil(b'\n\n',drop=True).decode().split(' ')[-1].strip()
    #dapetin n
    n = int(context.recvuntil(b'\n\n',drop=True).decode().split(' ')[-1].strip())
    #dapetin e
    e = int(context.recvuntil(b'\n\n',drop=True).decode().split(' ')[-1].strip())
    #dapetin c
    c = int(context.recvuntil(b'\n\n',drop=True).decode().split(' ')[-1].strip())

    # bikin payload
    payload = ""
    if(paket_soal=="A"):
      payload = solve_A().to_bytes(21,'big')
    elif(paket_soal=="B"):
      payload = solve_B().to_bytes(21,'big')
    elif(paket_soal=="C"):
      payload = solve_C().to_bytes(21,'big')
    elif(paket_soal=="D"):
      payload = solve_D(c).to_bytes(21,'big')
    elif(paket_soal=="E"):
      payload = solve_E().to_bytes(21,'big')
    else:
      context.close()
      raise ValueError("Mode Hanya Terdiri dari A hingga E saja")
  
    #preprocess payload
    payload = payload.split(b'\x00')[-1]
    #tunggu prompt jawaban
    context.recvuntil(b'=\n')

    #kirim payload
    context.sendline(payload)

    # lihat responsnya
    print(context.recvuntil(b'\n\n',drop=True))
  
  # Print Flag Akhir
  print(context.recvline(drop=True))