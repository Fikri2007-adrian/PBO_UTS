class Teman:
    # Class Attribute
    Hobi = " "

    # Constructor
    def __init__(self, nama, hobi):
        # Instance Attribute
        self.nama = nama
        self.hobi = hobi

    # Method percakapan
    def perkenalan(self):
        print("Halo, nama saya", self.nama)
        print("Hobi saya adalah", self.hobi)

    def ngobrol(self, teman):
        print(f"{teman2.nama}: fik, sinii ngopii")

        print(f"{teman1.nama}: Otewee gaskeeun.")

        print(f"{teman2.nama}: lama nih ga ketemu, gimana sehat?")

        print(f"{teman1.nama}: Alhamdulillah, seperti yang you tingali wae?")

        print(f"{teman2.nama}: Hahahaa baguslah, by the way hobi maneh sekarang apaan si?")

        print(f"{teman1.nama}: Tiba-tiba bet dah nanyain hobi, hobi urangmah mendaki")

        print(f"{teman2.nama}: Widihh mainnya di alam ye, tapi bukan sejak ditinggal si itu kan? hahaha")
        print(f"{teman1.nama}: cihh sotoy, kite mah mendaki kalo lagi ada money aja!")
        print(f"{teman2.nama}: Yaa siapa know kan, kapan² ajak hiking lah?")

        print(f"{teman1.nama}: atu gaskeeun")

        print(f"{teman1.nama}: ouh iya, klo hobi maneh apaan?")
        print(f"{teman2.nama}: Hobi urangmah masih sama, main bola")
        print(f"{teman1.nama}: itumah hobi maneh dari kids, emang seru main bola?")

        print(f"{teman2.nama}: Yaa gimana ya, selain kegiatan yg bikin bahagia, sebenernya urang juga punya cita-cita jadi pemain timnas.")

        print(f"{teman1.nama}: widiih pantesan ajee baru tau urang, kerenn lah semoga sukses!!")

        print(f"{teman2.nama}: AAMIIN YRA")
        print(f"{teman1.nama}: menurut maneh, why kita harus memiliki hobi ")

        print(f"{teman2.nama}: gimana ya, karenaa sebagai bentuk penyaluran emosi yang sehat aja, supaya ga terjebak stress berlebihan ")
        print(f"{teman1.nama}: anjay mabaar")

        print(f"{teman2.nama}: Yoaay, jadi kita harus punya suatu Hobi yang positif untuk meredakan stress selain dari beribadah.")

        print(f"{teman1.nama}: gilaa, rispek kali aku bahh.")

        print(f"{teman2.nama}: Yowess urang balik dulu yah, lagi ada urusan soalnya")

        print(f"{teman1.nama}: Siapp next time yak, tiati!")
# Object
teman1 = Teman("Fikri", "Mendaki gunung")
teman2 = Teman("Ibad", "Main Football")

# Menampilkan percakapan
print("=== PROGRAM PERCAKAPAN HOBI ===")
print("Hobi:", Teman.Hobi)

teman1.perkenalan()
teman2.perkenalan()

print("\n=== PERCAKAPAN ===")
teman1.ngobrol(teman2)