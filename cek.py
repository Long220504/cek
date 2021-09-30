#!/usr/bin/python3
# coding=utf-8
# Author : Sptty Chan
# Cie Kang Recode Ngelirik Nih ya wkwk

import requests,json,os

def logo():
	print("""
╭━━━┳━━━┳━━━┳━╮╱╭┳━╮╱╭┳━━━┳━━━╮
┃╭━╮┃╭━╮┃╭━╮┃┃╰╮┃┃┃╰╮┃┃╭━━┫╭━╮┃
┃╰━━┫┃╱╰┫┃╱┃┃╭╮╰╯┃╭╮╰╯┃╰━━┫╰━╯┃
╰━━╮┃┃╱╭┫╰━╯┃┃╰╮┃┃┃╰╮┃┃╭━━┫╭╮╭╯
┃╰━╯┃╰━╯┃╭━╮┃┃╱┃┃┃┃╱┃┃┃╰━━┫┃┃╰╮
╰━━━┻━━━┻╯╱╰┻╯╱╰━┻╯╱╰━┻━━━┻╯╰━╯
(+) github.com/Sptty-Chan""")

def login():
	os.system("clear")
	logo()
	iya = input("\nLogin Token : ")
	try:
		toll = requests.get("https://graph.facebook.com/me?access_token="+iya)
		ogh = json.loads(toll.text)
		name = ogh["name"]
		lah = open("tokek.txt","w")
		lah.write(iya)
		lah.close()
		print("Login Berhasil")
		info()
	except KeyError:
		print("Token Kadaluarsa/Salah")
		login()

def info():
	try:
		bisu = open("tokek.txt","r").read()
		ggs = requests.get("https://graph.facebook.com/me?access_token="+bisu)
		srigala = json.loads(ggs.text)
		nama = srigala["name"]
	except (KeyError, IOError):
		print("Token Kadaluarsa")
		login()
	os.system("clear")
	logo()
	print("\n["+srigala["name"]+"]")
	print("\n1. Mulai")
	print("2. Ganti Token/Logout")
	pilih()

def pilih():
	pill = input("\nPilih : ")
	if pill=="1":
		sayang()
	elif pill=="2":
		os.system("rm -rf tokek.txt")
		login()

def sayang():
	try:
		token = open("tokek.txt","r").read()
	except IOError:
		print("Token Kadaluarsa")
		login()
	idt = input("\nMasukkan ID : ")
	ink = input("Nama File Untuk Menyimpan : ")
	try:
		tod = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		bp = json.loads(tod.text)
		print("Nama : "+bp["name"])
	except KeyError:
		print("ID Tidak Ditemukan Atau Token Kadaluarsa/Limit")
		exit()
	try:
		tit = requests.get("https://graph.facebook.com/"+idt+"/friends?limit=10000&access_token="+token)
		uid = []
		tot = json.loads(tit.text)
		for i in tot["data"]:
			uid.append(i["id"])
		print("Total ID : %s"%(len(uid)))
		print("\nGet Info Massal Dimulai...")
		print("Untuk Berhenti, Tekan CTRL + Z")
	except KeyError:
		print("Limit Bro, Silahkan Ganti Tumbal Dulu")
		exit()
	try:
		git = requests.get("https://graph.facebook.com/"+idt+"/friends?limit=10000&access_token="+token)
		bl = json.loads(git.text)
		for c in bl["data"]:
			bf = c["id"]
			ar = requests.get("https://graph.facebook.com/"+bf+"?access_token="+token)
			cok = requests.get("https://graph.facebook.com/"+bf+"/friends?limit=10000&access_token="+token)
			id = []
			bs = json.loads(ar.text)
			bc = json.loads(cok.text)
			for t in bc["data"]:
				id.append(t["id"])
			print("\nID Facebook         : "+bs["id"])
			print("User Name           : "+bs["name"])
			print("Jumlah Teman        : %s"%(len(id)))
			try:
				fr = bs["hometown"]["name"]
				print("Dari                : "+fr)
			except (KeyError, IOError):
				fr = "-"
				print("Dari                : "+fr)
			try:
				tin = bs['location']['name']
				print("Tinggal Di          : "+tin)
			except (KeyError, IOError):
				tin = "-"
				print("Tinggal Di          : "+tin)
			try:
				mek = bs["updated_time"][:10]
				year, month, day = mek.split("-")
			except (KeyError, IOError):
				year = "-"
				month = "-"
				day = "-"
			print("Terakhir Diperbarui : Tanggal "+day+"-"+month+"-"+year)
			cm = open(ink+".json","a")
			cm.write("ID Facebook         : "+bs["id"]+"\nUser Name           : "+bs["name"]+"\nJumlah Teman        : %s"%(len(id))+"\nDari                : "+fr+"\nTinggal Di          : "+tin+"\nTerakhir Diperbarui : Tanggal "+day+"-"+month+"-"+year+"\n\n")
			cm.close()
		print("Selesai, Hasil Disimpan Kedalam File "+ink+".json")
	except KeyError:
		print("Limit Bro, Silahkan Ganti Tumbal Dulu")
		exit()
info()
