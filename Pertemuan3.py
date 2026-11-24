class RumahSakit:
    pass

class Dokter:
    pass

Rumah = RumahSakit()
Tenaga_medis = Dokter()

print(type(Rumah))
print(type(Tenaga_medis))


RS_Sehat = RumahSakit()
Dokter_Asep = Dokter()

print(type(RS_Sehat))
print(type(Dokter_Asep))


Rumah = RumahSakit()
Rumah.umur = 20
Rumah.nama = "RS Sehat Sejahtera"

print(Rumah.umur)
print(Rumah.nama)


Tenaga_medis = Dokter()
Tenaga_medis.umur = 35
Tenaga_medis.nama = "Dokter Asep"

print(Tenaga_medis.umur)
print(Tenaga_medis.nama)