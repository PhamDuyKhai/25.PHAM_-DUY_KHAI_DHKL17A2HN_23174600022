#tạp lớp HCN
class HCN:
    def __init__(self, dai = 0, rong = 0):
        self.dai = dai
        self.rong = rong  
    
    #Nhập dữ liệu hai cạnh
    def nhap(self):
        self.dai = float(input('nhập chiều dài:'))
        self.rong = float(input('nhập chiều rộng:'))
    
    #Tính chu vi
    def chu_vi(self):
        return (self.dai + self.rong) * 2
    
    #Tính diện tích
    def dien_tich(self):
        return self.dai * self.rong

    #in thông tin
    def in_tt(self):
        print(f"chiều dài HCN: {self.dai}\nchiều rộng HCN: {self.rong}\nchu vi HCN: {self.chu_vi()}\ndiện tích HCN: {self.dien_tich()}")

#tạo đối tượng
HCN1 = HCN()
HCN1.nhap()
HCN1.in_tt()