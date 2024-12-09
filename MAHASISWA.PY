```
class DataMahasigma : 
    def __init__(self):
        self.DataMahasigma = []
    
    def tambah(self, nama, nilai): 
        self.DataMahasigma.append({"nama" : nama, "nilai": nilai})
        print(f'data {nama} berhasil di tambahkan')
        
    def tampilkan (self):
        if not self.DataMahasigma:
            print("Data Tidak Di Temukan")
        else:
            print("Daftar Nilai Mahasiswa")
            for i, mahasiswa in enumerate(self.DataMahasigma, start= 1) :
                print(f"{i}. Nama: {mahasiswa['nama']}\n   Nilai: {mahasiswa['nilai']}")
                
    def hapus (self, nama):
        for mahasiswa in self.DataMahasigma:
            if mahasiswa ['nama'] == nama:
                self.DataMahasigma.remove(mahasiswa)
                print(f"Data {nama} Mahaiswa Berhasil Di Hapus")
                return
        print("Data Tidak Di Temukan")
    
    def ubah (self, nama, nilai_baru):
        for mahasiswa in self.DataMahasigma:
            if mahasiswa ["nama"] == nama:
                mahasiswa ["nilai"] = nilai_baru
                print(f"Data {nama} Berhasil Di Ubah")
                return
            print("Data Tidak Di Temukan")
```
A
