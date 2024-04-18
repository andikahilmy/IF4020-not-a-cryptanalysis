import os
import pwn
from dotenv import load_dotenv
from sympy import factorint

# Note: Cuma bisa di Linux (Windows gak support modul pwn)

CONTEXT = 'remote'
PYTHON_TYPE = 'python3' 

def set_context(mode:str)->pwn.remote | pwn.process:
  #mode: 'local','remote'
  if(mode=='remote'):
    # Kalau remote, load .env untuk dapetin server token
    load_dotenv()
    return pwn.remote("165.232.161.196", 1303)
  else:
    return pwn.process([PYTHON_TYPE,"source_B.py"])

if __name__=="__main__":
  context:pwn.remote | pwn.process = set_context(CONTEXT)

  if(CONTEXT=="remote"):
    #tunggu prompt token
    print(context.recvline(keepends=False))
    #Masukkan token
    token = os.getenv("SERVER_TOKEN")
    context.sendline(token.encode('utf-8'))
  # tunggu prompt
  context.recvuntil(b"Masukkan perintah: ")
  # Dapatkan nomor arsip admin
  context.sendline(b'3')
  # Dapetin nomor arsip
  nomor_arsip_admin = int(context.recvline(keepends=False).split(b' ')[-1].decode())

  # cari faktor dari nomor arsip admin
  factor_1 = list(factorint(nomor_arsip_admin))[-1]
  factor_2 = nomor_arsip_admin // factor_1

  #token faktor 1
  context.recvuntil(b"Masukkan perintah: ")
  # kirim opsi memasukkan
  context.sendline(b'1')
  # tunggu prompt
  if(CONTEXT=='remote'):
    context.recvuntil(b'Masukkan nomor arsip (dalam bentuk integer): ')
  else:
    context.recvline()
  # kirim faktor_1
  context.sendline(str(factor_1).encode('utf-8'))
  # tunggu prompt
  context.recvuntil(b"Masukkan isi arsip:")
  # kirim dummy
  context.sendline(b"faktor A")
  # dapatkan token faktor 1
  token_A = int(context.recvline(keepends=False).split(b' ')[-1].decode())

  #token faktor 2
  context.recvuntil(b"Masukkan perintah: ")
  # kirim opsi memasukkan
  context.sendline(b'1')
  # tunggu prompt
  if(CONTEXT=='remote'):
    context.recvuntil(b'Masukkan nomor arsip (dalam bentuk integer): ')
  else:
    context.recvline()
  # kirim faktor_2
  context.sendline(str(factor_2).encode('utf-8'))
  # tunggu prompt
  context.recvuntil(b"Masukkan isi arsip:")
  # kirim dummy
  context.sendline(b"faktor B")
  # dapatkan token faktor 2
  token_B = int(context.recvline(keepends=False).split(b' ')[-1].decode())

  # cara mendapatkan token admin(c):
  # c = a*b
  # token_c = token_a * token_b
  token_admin = token_A * token_B
  # kirimkan token admin
  context.recvuntil(b"Masukkan perintah: ")
  # kirim opsi memasukkan
  context.sendline(b'2')
  # tunggu prompt
  context.recvuntil(b'Masukkan token akses nomor arsip (dalam bentuk integer): ')
  # kirimkan token
  context.sendline(str(token_admin).encode('utf-8'))
  # dapatlan flag
  resp = context.recvline(keepends=False)
  flag = resp.decode().split(" ")[-1]
  print(f"Flag: {flag}")