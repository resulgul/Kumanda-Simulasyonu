
class kumanda:

    def __init__(self):
        self.ac = True
        self.kapa = False
        self.ses = 0

    def mute(self):
        if self.ses == 0:
            return("Ses mutelendi")

    def volumeup(self):
        if self.ac:
            if self.ses < 100:
                self.ses += 10
                return "Ses seviyesi : {}".format(self.ses)
            elif self.ses == 100:
                return "Ses seviyesi maximum seviyede"
    
    def volumedown(self):
        if self.ac:
            if self.ses > 0:
                self.ses -= 10
                return "Ses seviyesi : {}".format(self.ses)
            else:
                return "Ses Mutelendi"
    
    def tvac(self):
        if self.ac:
            self.ac = False
            return "Televizyon açiliyor"
        else:
            return "Televizyon açik durumda"


    def tvkapat(self):
        if not self.kapa:
            self.kapa = True
            return "Televizyon kapatiliyor"
        else:
            return "Televizyon kapali durumda"    


def kanallar():
    kanalist = ["StarTv","KanalD","Trt","ShowTv","Tv8","Atv","Tlc"]
    return str(kanalist)




def write_t(info):
    with open("tv.txt","w") as text:
        text.write(info + "\n")


def main():
    tv_kumanda = kumanda()
    seçim = ""

    while seçim != "7":

        seçim = input("Seçiminiz : ")

        if seçim == "1":
            inf = tv_kumanda.mute()
            write_t(inf)
            print(inf)
            
        elif seçim == "2":
            inf = tv_kumanda.volumeup()
            write_t(inf)
            print(inf)
            
        elif seçim == "3":
            inf = tv_kumanda.volumedown()
            write_t(inf)
            print(inf)
            
        elif seçim == "4":
            inf = tv_kumanda.tvac()
            write_t(inf)
            print(inf)
            
        elif seçim == "5":
            inf = tv_kumanda.tvkapat()
            write_t(inf)
            print(inf)

        elif seçim == "6":
            inf = kanallar()
            write_t(inf)
            print(inf)

        elif seçim == "7":
            quit
            



#-Ses seviyesini mutelemek için '1'
#-Ses seviyesini açmak için '2'
#-Ses seviyesini kısmak için '3'
#-Televizyonu açmak için '4'
#-Televizyonu kapatmak için '5'
#-Kanal listesi için '6'
#-Çıkmak için '7'


if __name__ == "__main__":
    main()



                



        