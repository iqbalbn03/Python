from experta import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

def preprocess():
    global diseases_list, diseases_symptoms, symptom_map, d_desc_map, d_treatment_map
    
    # Inisialisasi list dan peta sebelum penggunaan
    diseases_symptoms = []
    symptom_map = {}
    d_desc_map = {}
    d_treatment_map = {}

    with open("penyakit.txt", "r") as diseases:
        diseases_t = diseases.read()
        diseases_list = diseases_t.split("\n")

    for disease in diseases_list:
        with open(f"Gejala_penyakit/{disease}.txt", "r") as disease_s_file:
            disease_s_data = disease_s_file.read()
            s_list = disease_s_data.split("\n")
            diseases_symptoms.append(s_list)
            symptom_map[str(s_list)] = disease

        with open(f"Deskripsi_penyakit/{disease}.txt", "r") as disease_s_file:
            disease_s_data = disease_s_file.read()
            d_desc_map[disease] = disease_s_data

        with open(f"Obat_penyakit/{disease}.txt", "r") as disease_s_file:
            disease_s_data = disease_s_file.read()
            d_treatment_map[disease] = disease_s_data

# Memanggil fungsi preprocess
if __name__ == "__main__":
    preprocess()
    # Lanjutkan dengan kode lain yang diperlukan, seperti membuat objek Greetings dan menjalankannya.

	

def identify_disease(*arguments):
	symptom_list = []
	for symptom in arguments:
		symptom_list.append(symptom)
	# Handle key error
	return symptom_map[str(symptom_list)]

def get_details(disease):
	return d_desc_map[disease]

def get_treatments(disease):
	return d_treatment_map[disease]

def if_not_matched(disease):
		print("")
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		print("")
		print("Kemungkinan Penyakit yang Anda Derita adalah %s\n" %(id_disease))

		plt.imshow(mpimg.imread("./img/" + id_disease + ".jpg"))
		plt.title(id_disease)
		plt.axis('off')
		plt.show()

		print("Beberapa deskripsi tentang penyakit yang diberikan :")
		print(disease_details+"\n")
		print("Pengobatan umum dan prosedur yang disarankan oleh dokter adalah :")
		print(treatments+"\n")

class Greetings(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		print("")
		print("Hai! Selamat Datang saya adalah Skin Health Tracker-bot, Saya akan mendiagnosa penyakit kulit yang anda Derita!")
		print("Oleh sebab itu saya harap anda  menjawab beberapa pertanyaan  gejala agar nantinya saya dapat mengetahui penyakit kulit yang anda derita ")
		print("Apakah anda merasakan beberapa gejala dibawah ini(ya/tidak):")
		print("")
		yield Fact(action="find_disease")

#Gejala
	@Rule(Fact(action='find_disease'), NOT(Fact(kulit_membengkak=W())),salience = 1)
	def symptom_0(self):
		self.declare(Fact(kulit_membengkak=input("Apakah anda mengalami pembengkakan kulit: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(benjolan_di_kulit=W())),salience = 1)
	def symptom_1(self):
		self.declare(Fact(benjolan_di_kulit=input("Apakah anda mengalami benjolan di kulit: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(mengeluarkan_nanah=W())),salience = 1)
	def symptom_2(self):
		self.declare(Fact(mengeluarkan_nanah=input("Apakah kulit anda mengeluarkan nanah: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(demam=W())),salience = 1)
	def symptom_3(self):
		self.declare(Fact(demam=input("Apakah anda demam: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(mata_merah=W())),salience = 1)
	def symptom_4(self):
		self.declare(Fact(mata_merah=input("Apakah mata anda merah: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(kulit_kepala_berminyak=W())),salience = 1)
	def symptom_5(self):
		self.declare(Fact(kulit_kepala_berminyak=input("Apakah kulit kepala anda berminyak: ")))
	 
	@Rule(Fact(action='find_disease'), NOT(Fact(rasa_gatal=W())),salience = 1)
	def symptom_6(self):
		self.declare(Fact(rasa_gatal=input("Apakah anda merasakan gatal: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(luka_dari_bagian_mulut=W())),salience = 1)
	def symptom_7(self):
		self.declare(Fact(luka_dari_bagian_mulut=input("Apakah ada luka dari bagian mulut: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(memiliki_gelembung_berisi_air=W())),salience = 1)
	def symptom_8(self):
		self.declare(Fact(memiliki_gelembung_berisi_air=input("Apakah ada semacam gelembung berisi air: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(rasa_nyeri=W())),salience = 1)
	def symptom_9(self):
		self.declare(Fact(rasa_nyeri=input("Apakah anda merasakan nyeri: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(kulit_melepuh=W())),salience = 1)
	def symptom_10(self):
		self.declare(Fact(kulit_melepuh=input("Apakah kulit anda melepuh: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(memiliki_bercak_bercak_merah=W())),salience = 1)
	def symptom_11(self):
		self.declare(Fact(memiliki_bercak_bercak_merah=input("Apakah timbul bercak bercak merah: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(iritasi_kulit=W())),salience = 1)
	def symptom_12(self):
		self.declare(Fact(iritasi_kulit=input("Apakah terjadi iritasi kulit: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(uban_muncul_sebelum_waktunya=W())), salience=1)
	def symptom_13(self):
		self.declare(Fact(uban_muncul_sebelum_waktunya=input("Apakah muncul uban sebelum waktunya: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(muncul_keringat_berlebihan=W())), salience=1)
	def symptom_14(self):
		self.declare(Fact(muncul_keringat_berlebihan=input("Apakah anda mengalami keringat yang berlebihan: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(menimbulkan_warna_kekuningan=W())), salience=1)
	def symptom_15(self):
		self.declare(Fact(menimbulkan_warna_kekuningan=input("Apakah ada timbul warna kekuningan pada kulit anda: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(kulit_kering=W())), salience=1)
	def symptom_16(self):
		self.declare(Fact(kulit_kering=input("Apakah anda mengalami kulit kering: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(kulit_bersisik=W())), salience=1)
	def symptom_17(self):
		self.declare(Fact(kulit_bersisik=input("Apakah kulit bersisik pada bagian tertentu: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(bintik_atau_bintik_merah=W())), salience=1)
	def symptom_18(self):
		self.declare(Fact(bintik_atau_bintik_merah=input("Apakah bintik atau bintik merah muncul di kulit: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(ruam_kulit=W())), salience=1)
	def symptom_19(self):
		self.declare(Fact(ruam_kulit=input("Apakah Anda mengalami ruam kulit: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(luka=W())), salience=1)
	def symptom_20(self):
		self.declare(Fact(luka=input("Apakah ada luka pada kulit yang perlu diatasi: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(mati_rasa=W())), salience=1)
	def symptom_21(self):
		self.declare(Fact(mati_rasa=input("Apakah ada mati rasa pada kulit: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(luka_tidak_terasa_nyeri=W())), salience=1)
	def symptom_22(self):
		self.declare(Fact(luka_tidak_terasa_nyeri=input("Apakah Anda memiliki luka yang tidak terasa nyeri: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(kulit_tidak_berkeringat=W())), salience=1)
	def symptom_23(self):
		self.declare(Fact(kulit_tidak_berkeringat=input("Apakah kulit tidak berkeringat secara normal: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(kesemutan=W())), salience=1)
	def symptom_24(self):
		self.declare(Fact(kesemutan=input("Apakah Anda merasakan kesemutan pada kulit: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(benjolan_berwarna_merah_atau_kulit_kemerahan=W())), salience=1)
	def symptom_25(self):
		self.declare(Fact(benjolan_berwarna_merah_atau_kulit_kemerahan=input("Apakah ada benjolan berwarna merah atau kulit kemerahan: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(infeksi_kulit=W())), salience=1)
	def symptom_26(self):
		self.declare(Fact(infeksi_kulit=input("Apakah Anda mengalami infeksi kulit: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(sakit_kepala=W())), salience=1)
	def symptom_27(self):
		self.declare(Fact(sakit_kepala=input("Apakah Anda sering mengalami sakit kepala: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(rasa_kelelahan=W())), salience=1)
	def symptom_28(self):
		self.declare(Fact(rasa_kelelahan=input("Apakah ada rasa kelelahan secara umum: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(mual=W())), salience=1)
	def symptom_29(self):
		self.declare(Fact(mual=input("Apakah Anda mengalami mual: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(nyeri_otot=W())), salience=1)
	def symptom_30(self):
		self.declare(Fact(nyeri_otot=input("Apakah terdapat nyeri otot pada tubuh: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(benjolan_putih=W())), salience=1)
	def symptom_31(self):
		self.declare(Fact(benjolan_putih=input("Apakah ada benjolan putih di kulit: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(bintil=W())), salience=1)
	def symptom_32(self):
		self.declare(Fact(bintil=input("Apakah kulit memiliki bintil atau tonjolan: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(lesi_gatal_atau_kemerahan=W())), salience=1)
	def symptom_33(self):
		self.declare(Fact(lesi_gatal_atau_kemerahan=input("Apakah ada lesi gatal atau kemerahan pada kulit: ")))
		
	@Rule(Fact(action='find_disease'), NOT(Fact(tonjolan_kasar_atau_keras=W())), salience=1)
	def symptom_34(self):
		self.declare(Fact(tonjolan_kasar_atau_keras=input("Apakah timbul tonjolan kasar atau keras: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(bintik_atau_bercak_putih_berwarna_terang=W())), salience=1)
	def symptom_35(self):
		self.declare(Fact(bintik_atau_bercak_putih_berwarna_terang=input("Apakah timbul bintik atau bercak putih yang berwarna terang: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(ruam_berbentuk_cincin=W())), salience=1)
	def symptom_36(self):
		self.declare(Fact(ruam_berbentuk_cincin=input("Apakah timbul ruam yang berbentuk cincin: ")))


	@Rule(Fact(action='find_disease'),Fact(kulit_membengkak="tidak"),Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"),Fact(demam="tidak"),Fact(mata_merah="tidak"),Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="ya"),Fact(luka_dari_bagian_mulut="tidak"),Fact(memiliki_gelembung_berisi_air="ya"),
		  Fact(rasa_nyeri="tidak"),Fact(kulit_melepuh="tidak"),Fact(memiliki_bercak_bercak_merah="tidak"),Fact(iritasi_kulit="tidak"),
		  Fact(uban_muncul_sebelum_waktunya="tidak"),Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="ya"),Fact(kulit_bersisik="ya"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="ya"),Fact(luka="ya"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="tidak"),Fact(infeksi_kulit="ya"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_0(self):
		self.declare(Fact(disease="Eksim"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="ya"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="tidak"), Fact(kulit_melepuh="tidak"), Fact(memiliki_bercak_bercak_merah="ya"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="ya"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="ya"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="ya"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_1(self):
		self.declare(Fact(disease="Kurap"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="ya"), Fact(mata_merah="ya"),
		  Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="tidak"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="ya"), Fact(kulit_melepuh="tidak"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="ya"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="tidak"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="ya"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_2(self):
		self.declare(Fact(disease="Campak"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="ya"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="tidak"), Fact(kulit_melepuh="tidak"), Fact(memiliki_bercak_bercak_merah="ya"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="ya"),Fact(kulit_bersisik="ya"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="tidak"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="ya"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_3(self):
		self.declare(Fact(disease="Psoriasis"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="ya"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="tidak"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="tidak"), Fact(kulit_melepuh="tidak"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="tidak"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="tidak"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="ya"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_4(self):
		self.declare(Fact(disease="Kutil"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="ya"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="tidak"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="ya"), Fact(kulit_melepuh="ya"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="ya"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="ya"),Fact(luka="ya"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="ya"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="ya"),Fact(rasa_kelelahan="ya"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_5(self):
		self.declare(Fact(disease="Herpes"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="ya"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="tidak"), Fact(kulit_melepuh="tidak"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="ya"),Fact(kulit_bersisik="ya"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="ya"),Fact(luka="ya"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="tidak"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_6(self):
		self.declare(Fact(disease="Kudis"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="tidak"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="ya"),
		  Fact(rasa_nyeri="ya"), Fact(kulit_melepuh="ya"), Fact(memiliki_bercak_bercak_merah="ya"),
		  Fact(iritasi_kulit="ya"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="tidak"),Fact(luka="ya"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="tidak"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_7(self):
		self.declare(Fact(disease="Impetigo"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="ya"), Fact(benjolan_di_kulit="ya"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="tidak"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="nyeri"), Fact(kulit_melepuh="tidak"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="ya"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="tidak"),Fact(luka="tidak"),Fact(mati_rasa="ya"),Fact(luka_tidak_terasa_nyeri="ya"),Fact(kulit_tidak_berkeringat="ya"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="tidak"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_8(self):
		self.declare(Fact(disease="Lepra"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="ya"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="ya"), Fact(kulit_melepuh="tidak"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="tidak"),Fact(luka="ya"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="ya"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="ya"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_9(self):
		self.declare(Fact(disease="Keloid"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="tidak"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="tidak"), Fact(kulit_melepuh="tidak"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="tidak"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="ya"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_10(self):
		self.declare(Fact(disease="Hemangioma"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="ya"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="tidak"), Fact(kulit_melepuh="tidak"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="ya"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="ya"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="tidak"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="ya"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_11(self):
		self.declare(Fact(disease="Vitiligo"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="tidak"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="tidak"), Fact(kulit_melepuh="tidak"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="ya"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="tidak"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="tidak"),Fact(infeksi_kulit="ya"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_12(self):
		self.declare(Fact(disease="Hypohidrosis"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="ya"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="ya"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="ya"), Fact(kulit_melepuh="ya"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="ya"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="ya"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="ya"),Fact(rasa_kelelahan="ya"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_13(self):
		self.declare(Fact(disease="Varicella"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="ya"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="ya"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="ya"), Fact(kulit_melepuh="tidak"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="ya"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="ya"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_14(self):
		self.declare(Fact(disease="Urtikaria"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="ya"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="ya"), Fact(demam="ya"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="tidak"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="ya"), Fact(kulit_melepuh="ya"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="tidak"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="ya"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_15(self):
		self.declare(Fact(disease="Selulitis"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="ya"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="ya"), Fact(kulit_melepuh="ya"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="ya"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="ya"),Fact(luka="ya"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="tidak"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_16(self):
		self.declare(Fact(disease="Lichenplanus"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="tidak"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="ya"), Fact(kulit_melepuh="tidak"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="ya"),Fact(kulit_bersisik="ya"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="tidak"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="ya"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_17(self):
		self.declare(Fact(disease="Rosacea"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="tidak"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="tidak"), Fact(kulit_melepuh="tidak"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="tidak"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="tidak"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="ya"),Fact(bintil="ya"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_18(self):
		self.declare(Fact(disease="Milia"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="ya"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="tidak"), Fact(kulit_melepuh="tidak"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="ya"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="tidak"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="ya"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_19(self):
		self.declare(Fact(disease="Keratosispilaris"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="ya"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="tidak"), Fact(kulit_melepuh="tidak"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="tidak"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="tidak"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="ya"),Fact(lesi_gatal_atau_kemerahan="ya"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_20(self):
		self.declare(Fact(disease="Molluscumcontagiosum"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="ya"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="ya"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="tidak"), Fact(kulit_melepuh="tidak"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="ya"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="tidak"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="ya"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_21(self):
		self.declare(Fact(disease="Larvamigrans"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="ya"), Fact(demam="ya"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="tidak"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="tidak"), Fact(kulit_melepuh="tidak"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="ya"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="tidak"),Fact(luka="ya"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="tidak"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="ya"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_22(self):
		self.declare(Fact(disease="Favus"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="ya"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="ya"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="air"),
		  Fact(rasa_nyeri="ya"), Fact(kulit_melepuh="ya"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="tidak"),Fact(luka="ya"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="ya"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="ya"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_23(self):
		self.declare(Fact(disease="Pemphigus"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="ya"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="tidak"), Fact(kulit_melepuh="tidak"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="ya"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="ya"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="ya"))
	def disease_24(self):
		self.declare(Fact(disease="Granulomaannulare"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="ya"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="ya"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="ya"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="ya"), Fact(kulit_melepuh="ya"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="tidak"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="ya"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_25(self):
		self.declare(Fact(disease="Folikulitis"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="ya"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="ya"), Fact(demam="ya"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="tidak"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="ya"), Fact(kulit_melepuh="tidak"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="tidak"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="ya"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_26(self):
		self.declare(Fact(disease="Furunkel"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="ya"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="tidak"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="ya"), Fact(kulit_melepuh="ya"), Fact(memiliki_bercak_bercak_merah="ya"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="ya"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="ya"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="ya"),Fact(rasa_kelelahan="ya"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="ya"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_27(self):
		self.declare(Fact(disease="Sindromstevejohnson"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="tidak"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="tidak"), Fact(kulit_melepuh="ya"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="tidak"),Fact(luka="ya"),Fact(mati_rasa="ya"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="ya"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="tidak"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="ya"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_28(self):
		self.declare(Fact(disease="Lukaakibatsengatanlistrik"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="ya"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="tidak"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="ya"), Fact(kulit_melepuh="ya"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="ya"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="ya"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="tidak"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="ya"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_29(self):
		self.declare(Fact(disease="Lukaakibatbahankimia"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="tidak"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="tidak"), Fact(kulit_melepuh="ya"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="tidak"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="ya"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_30(self):
		self.declare(Fact(disease="Fixeddrugeruption"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="ya"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="tidak"), Fact(kulit_melepuh="tidak"), Fact(memiliki_bercak_bercak_merah="ya"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="ya"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="tidak"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="tidak"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_31(self):
		self.declare(Fact(disease="Eritrasma"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="ya"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="ya"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="ya"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="ya"), Fact(kulit_melepuh="ya"), Fact(memiliki_bercak_bercak_merah="ya"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="ya"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="tidak"),Fact(infeksi_kulit="ya"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_32(self):
		self.declare(Fact(disease="Kandidosismukokutan"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="ya"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="tidak"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="tidak"), Fact(kulit_melepuh="ya"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="ya"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="tidak"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="ya"),Fact(rasa_kelelahan="ya"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_33(self):
		self.declare(Fact(disease="Erisipelas"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="tidak"),
		  Fact(mengeluarkan_nanah="tidak"), Fact(demam="tidak"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="ya"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="tidak"), Fact(kulit_melepuh="ya"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="tidak"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="ya"),Fact(kulit_bersisik="ya"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="tidak"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="tidak"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="tidak"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="tidak"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_34(self):
		self.declare(Fact(disease="Tineapedis"))

	@Rule(Fact(action='find_disease'), Fact(kulit_membengkak="tidak"), Fact(benjolan_di_kulit="ya"),
		  Fact(mengeluarkan_nanah="ya"), Fact(demam="ya"), Fact(mata_merah="tidak"), Fact(kulit_kepala_berminyak="tidak"),
		  Fact(rasa_gatal="tidak"), Fact(luka_dari_bagian_mulut="tidak"), Fact(memiliki_gelembung_berisi_air="tidak"),
		  Fact(rasa_nyeri="tidak"), Fact(kulit_melepuh="tidak"), Fact(memiliki_bercak_bercak_merah="tidak"),
		  Fact(iritasi_kulit="tidak"), Fact(uban_muncul_sebelum_waktunya="tidak"), Fact(muncul_keringat_berlebihan="ya"),
		  Fact(menimbulkan_warna_kekuningan="tidak"),Fact(kulit_kering="tidak"),Fact(kulit_bersisik="tidak"),Fact(bintik_atau_bintik_merah="tidak"),Fact(ruam_kulit="tidak"),Fact(luka="tidak"),Fact(mati_rasa="tidak"),Fact(luka_tidak_terasa_nyeri="tidak"),Fact(kulit_tidak_berkeringat="tidak"),Fact(kesemutan="tidak"),Fact(benjolan_berwarna_merah_atau_kulit_kemerahan="tidak"),Fact(infeksi_kulit="tidak"),Fact(sakit_kepala="tidak"),Fact(rasa_kelelahan="ya"),Fact(mual="tidak"),Fact(nyeri_otot="tidak"),Fact(benjolan_putih="tidak"),Fact(bintil="tidak"),Fact(lesi_gatal_atau_kemerahan="tidak"),Fact(tonjolan_kasar_atau_keras="ya"),Fact(bintik_atau_bercak_putih_berwarna_terang="tidak"),Fact(ruam_berbentuk_cincin="tidak"))
	def disease_35(self):
		self.declare(Fact(disease="Skrofuloderma"))

	

	@Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998)

	def disease(self, disease):
		print("")
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		print("")
		print("Kemungkinan terbesar yang anda alami adalah %s\n" %(id_disease))

		plt.imshow(mpimg.imread("./img/" + id_disease + ".jpg"))
		plt.title(id_disease)
		plt.axis('off')
		plt.show()

		print("Berikut deskripsi singkat dari penyakit yang diberikan :")
		print(disease_details+"\n")
		print("Beberapa pengobatan yang disarankan :")
		print(treatments+"\n")

	@Rule(Fact(action='find_disease'),
		  Fact(kulit_membengkak=MATCH.kulit_membengkak),
		  Fact(benjolan_di_kulit=MATCH.benjolan_di_kulit),
		  Fact(mengeluarkan_nanah=MATCH.mengeluarkan_nanah),
		  Fact(demam=MATCH.demam),
		  Fact(mata_merah=MATCH.mata_merah),
		  Fact(kulit_kepala_berminyak=MATCH.kulit_kepala_berminyak),
		  Fact(rasa_gatal=MATCH.rasa_gatal),
		  Fact(luka_dari_bagian_mulut=MATCH.luka_dari_bagian_mulut),
		  Fact(memiliki_gelembung_berisi_air=MATCH.memiliki_gelembung_berisi_air),
		  Fact(rasa_nyeri=MATCH.rasa_nyeri),
		  Fact(kulit_melepuh=MATCH.kulit_melepuh),
		  Fact(memiliki_bercak_bercak_merah=MATCH.memiliki_bercak_bercak_merah),
		  Fact(iritasi_kulit=MATCH.iritasi_kulit),
		  Fact(uban_muncul_sebelum_waktunya=MATCH.uban_muncul_sebelum_waktunya),
		  Fact(muncul_keringat_berlebihan=MATCH.muncul_keringat_berlebihan),
		  Fact(menimbulkan_warna_kekuningan=MATCH.menimbulkan_warna_kekuningan),
		  Fact(kulit_kering=MATCH.kulit_kering),
		  Fact(kulit_bersisik=MATCH.kulit_bersisik),
		  Fact(bintik_atau_bintik_merah=MATCH.bintik_atau_bintik_merah),
		  Fact(ruam_kulit=MATCH.ruam_kulit),
		  Fact(luka=MATCH.luka),
		  Fact(mati_rasa=MATCH.mati_rasa),
		  Fact(luka_tidak_terasa_nyeri=MATCH.luka_tidak_terasa_nyeri),
		  Fact(kulit_tidak_berkeringat=MATCH.kulit_tidak_berkeringat),
		  Fact(kesemutan=MATCH.kesemutan),
		  Fact(benjolan_berwarna_merah_atau_kulit_kemerahan=MATCH.benjolan_berwarna_merah_atau_kulit_kemerahan),
		  Fact(infeksi_kulit=MATCH.infeksi_kulit),
		  Fact(sakit_kepala=MATCH.sakit_kepala),
		  Fact(rasa_kelelahan=MATCH.rasa_kelelahan),
		  Fact(mual=MATCH.mual),
		  Fact(nyeri_otot=MATCH.nyeri_otot),
		  Fact(benjolan_putih=MATCH.benjolan_putih),
		  Fact(bintil=MATCH.bintil),
		  Fact(lesi_gatal_atau_kemerahan=MATCH.lesi_gatal_atau_kemerahan),
		  Fact(tonjolan_kasar_atau_keras=MATCH.tonjolan_kasar_atau_keras),
		  Fact(bintik_atau_bercak_putih_berwarna_terang=MATCH.bintik_atau_bercak_putih_berwarna_terang),
		  Fact(ruam_berbentuk_cincin=MATCH.ruam_berbentuk_cincin),
		  NOT(Fact(disease=MATCH.disease)),salience = -999)

	def not_matched(self,kulit_membengkak, benjolan_di_kulit, mengeluarkan_nanah, demam, mata_merah, kulit_kepala_berminyak,
					rasa_gatal, luka_dari_bagian_mulut,memiliki_gelembung_berisi_air ,rasa_nyeri ,kulit_melepuh ,memiliki_bercak_bercak_merah ,
					iritasi_kulit,uban_muncul_sebelum_waktunya,muncul_keringat_berlebihan,menimbulkan_warna_kekuningan,kulit_kering,kulit_bersisik,bintik_atau_bintik_merah,ruam_kulit,luka,mati_rasa,luka_tidak_terasa_nyeri,kulit_tidak_berkeringat,kesemutan,benjolan_berwarna_merah_atau_kulit_kemerahan,infeksi_kulit,sakit_kepala,rasa_kelelahan,mual,nyeri_otot,benjolan_putih,bintil,lesi_gatal_atau_kemerahan,tonjolan_kasar_atau_keras,bintik_atau_bercak_putih_berwarna_terang,ruam_berbentuk_cincin):
		print("\nTidak menemukan penyakit yang sangat pas dengan gejala yang anda alami")
		lis = [kulit_membengkak, benjolan_di_kulit, mengeluarkan_nanah, demam, mata_merah, kulit_kepala_berminyak,
					rasa_gatal, luka_dari_bagian_mulut,memiliki_gelembung_berisi_air ,rasa_nyeri ,kulit_melepuh ,memiliki_bercak_bercak_merah ,
					iritasi_kulit,uban_muncul_sebelum_waktunya,muncul_keringat_berlebihan,menimbulkan_warna_kekuningan,kulit_kering,kulit_bersisik,bintik_atau_bintik_merah,ruam_kulit,luka,mati_rasa,luka_tidak_terasa_nyeri,kulit_tidak_berkeringat,kesemutan,benjolan_berwarna_merah_atau_kulit_kemerahan,infeksi_kulit,sakit_kepala,rasa_kelelahan,mual,nyeri_otot,benjolan_putih,bintil,lesi_gatal_atau_kemerahan,tonjolan_kasar_atau_keras,bintik_atau_bercak_putih_berwarna_terang,ruam_berbentuk_cincin]
		max_count = 0
		max_disease = ""
		for key,val in symptom_map.items():
			count = 0
			temp_list = eval(key)
			for j in range(0,len(lis)):
				if(temp_list[j] == lis[j] and lis[j] == "iya"):
					count = count + 1
			if count > max_count:
				max_count = count
				max_disease = val
		if_not_matched(max_disease)


if __name__ == "__main__":
	preprocess()
	engine = Greetings()
	while(1):
		engine.reset()  # Prepare the engine for the execution.
		engine.run()  # Run it!
		print("Ingin mencoba diagnosa dengan gejala yang lain?")
		if input() == "tidak":
			exit()
		#print(engine.facts)
