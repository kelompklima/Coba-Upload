import tkinter
import time

def tampilkanJam():
	waktu = time.localtime()
	tahun = waktu[0]
	bulan = waktu[1]
	tanggal = waktu[2]
	jam = waktu[3]
	menit = waktu[4]
	detik = waktu[5]

	labelInfo["text"] = "%02d/%02d/%4d %02d:%02d:%02d" % \
						(tanggal, bulan, tahun, jam, menit, detik)

jendela = tkinter.Tk()
jendela.geometry("250x100")
jendela.title("Jam Sekarang")
labelInfo = tkinter.Label (jendela, text = "Waktu sekarang ? Klik button !")
labelInfo.pack()

tombolJam = tkinter.Button (jendela, text = "Waktu sekarang", command = tampilkanJam)
tombolJam.pack()
jendela.mainloop()