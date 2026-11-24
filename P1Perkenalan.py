class mhs:
    nim = 0
    nama = ""

    def perkenalan(self):
        print(f"Halo nama saya {self.nama}")

    def hello(self, nama):
        print(f"Halo {self.nama}, nama saya {nama} ")


mhs = mhs()
mhs.nama = "Fikri"
mhs.perkenalan()
mhs.hello("adrian")