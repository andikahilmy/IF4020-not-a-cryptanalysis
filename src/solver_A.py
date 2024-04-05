from sympy import cbrt
import pwn
from dotenv import load_dotenv
import os

# Note: Cuma bisa di Linux (Windows gak support modul pwn)

CONTEXT = 'local'
PYTHON_TYPE = 'python3' 

def solve_A()->int:
  # dummy
  return 1

def solve_B()->int:
  # dummy
  return 1

def solve_C()->int:
  # dummy
  return 1

def solve_D(c:int)->int:
  m = cbrt(c)
  return int(m)

def solve_E()->int:
  # dummy
  return 1

def set_context(mode:str)->pwn.remote|pwn.process:
  #mode: 'local','remote'
  if(mode=='remote'):
    # Kalau remote, load .env untuk dapetin server token
    load_dotenv()
    return pwn.remote("165.232.161.196", 4020)
  else:
    return pwn.process([PYTHON_TYPE,"source_A.py"])

if __name__=="__main__":
  context:pwn.remote | pwn.process = set_context(CONTEXT)

  # iteration
  iterations = int(input("Masukkan Jumlah Iterasi: "))

  if(CONTEXT=="remote"):
    #tunggu prompt token
    print(context.recvline(keepends=False))
    #Masukkan token
    token = os.getenv("SERVER_TOKEN")
    print(token)
    context.sendline(token)
  # skip pesan awalnya
  if(CONTEXT=="remote"):
    context.recvuntil(b":D\n")
  else:
    context.recvuntil(b":D\n\n")
  # lakukan iterasi
  paket_soal = ""
  n = 0
  e = 0
  c = 0
  for _ in range(iterations):
    # print tahap sekarang
    print(context.recvline(keepends=False))
    # skip baris
    if(CONTEXT!='remote'):
      context.recvline()
      #dapetin paket soal
      paket_soal = context.recvuntil(b'\n\n',drop=True).decode().split(' ')[-1].strip()
      #dapetin n
      n = int(context.recvuntil(b'\n\n',drop=True).decode().split(' ')[-1].strip())
      #dapetin e
      e = int(context.recvuntil(b'\n\n',drop=True).decode().split(' ')[-1].strip())
      #dapetin c
      c = int(context.recvuntil(b'\n\n',drop=True).decode().split(' ')[-1].strip())
    else:
      #dapetin paket soal
      paket_soal = context.recvline(keepends=False).decode().split(' ')[-1].strip()
      #dapetin n
      n = int(context.recvline(keepends=False).decode().split(' ')[-1].strip())
      #dapetin e
      e = int(context.recvline(keepends=False).decode().split(' ')[-1].strip())
      #dapetin c
      c = int(context.recvline(keepends=False).decode().split(' ')[-1].strip())
    #tunggu prompt jawaban
    if(CONTEXT!='remote'):
      print(context.recvline(keepends=False))

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
    payload = payload.replace(b'\x00',b'')
    #cetak payload
    print(payload)
    #kirim payload
    context.sendline(payload)

    # lihat responsnya
    if(CONTEXT!='remote'):
      print(context.recvuntil(b'\n\n',drop=True))
    else:
      print(context.recvline(keepends=False))
  
  # Print Flag Akhir
  print(context.recvline())