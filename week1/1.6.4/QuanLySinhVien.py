from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []
    def generateID(self):
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
                maxId - maxId + 1
        return maxId
    
    def soLuongSinhVien(self):
        return self.listSinhVien._len_()

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svId = self.generateID()

        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành của sinh viên: ")
        diemTB = float(input("Nhập điểm của sinh viên: "))

        sv = SinhVien(svId, name, sex, major, diemTB)

        self.xepLoaiHocLuc(sv)

        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv: SinhVien = self.findByID(ID)
        if (sv  != None):           
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính sinh viên: ")
            major = input("Nhập chuyên ngành của sinh viên: ")
            diemTB = float(input("Nhập điểm của sinh viên: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)