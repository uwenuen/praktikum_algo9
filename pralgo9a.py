# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 19:34:46 2023

@author: user
"""

def nulisfile():
    innama = input("Masukkin nama kamu: ")
    inumur = input("Masukkin Umur kamu: ")
    inalamat = input("Masukkin alamat kamu: ")
    inemail = input("Masukkin email kamu: ")
    indosen = input("Masukkin dosen wali kamu: ")
    
    filenulis = open("Biodata.txt", "w")
    filenulis.write("Nama: " + innama + "\nUmur: " + inumur + "\nAlamat: " + inalamat + "\nEmail: " + inemail + "\nDosen: " + indosen)
    filenulis.close()
    
def bacafile():
    filebaca = open("Biodata.txt", "r")
    text = filebaca.read()
    print("ini dia data kamu!")
    print(text)
    filebaca.close()
    
nulisfile()
print("\n")
bacafile()