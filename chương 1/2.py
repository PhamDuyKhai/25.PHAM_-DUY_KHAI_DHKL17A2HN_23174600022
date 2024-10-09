#tạo lớp TS
class TS:
    def __init__(self, ho_ten = '', toan = 0, ly = 0, hoa = 0):
        self.ho_ten = ho_ten
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
    #tạo phương thức nhập thông tin thí sinh
    def nhap_tt(self):
        self.ho_ten = input("nhập họ và tên:")
        self.toan = float(input("nhập điểm toán:"))
        self.ly = float(input("nhập điểm lý:"))
        self.hoa = float(input("nhập điểm hóa:"))
    
    #tạo phương thức in thông tin
    def in_tt(self):
        print (f"họ và tên:{self.ho_ten}\nđiểm toán:{self.toan}\nđiểm hóa:{self.hoa}\nđiểm lý:{self.ly}")
    
    #tạo phương thức tính điểm
    def tinh_diem(self):
        return self.toan + self.ly + self.hoa

#tạo hàm main 
def main():
    #Nhập thông tin của một danh sách các học sinh     
    list = []   #khởi tạo list rỗng
    while True:
        a = 1
        hs = TS()
        hs.nhap_tt()
        list.append({
                    'họ và tên': hs.ho_ten,
                    'điểm Toán': hs.toan,
                    'điểm Lý': hs.ly,
                    'điểm Hóa': hs.hoa,
                    'tổng điểm': hs.tinh_diem()
                    })
        print('tiếp tục nhập?\n1:có\n0:không')
        a = int(input('lựa chọn: '))
        if a == 0:
            break
        
    #Đưa ra danh sách thí sinh trúng tuyển ( tổng điểm >= 20) và sắp xếp giảm dần
    check_list = [x for x in list if x['tổng điểm'] >= 20]
    sorted_list = sorted(check_list, key = lambda x: x['tổng điểm'], reverse = True)
    print(f'danh sách sinh viên trúng tuyển: {sorted_list}')
    
#chạy chương trình
if __name__ == '__main__':  #kiểm tra xem tệp mã nguồn hiện tại có đang được chạy như một chương trình chính hay không, nếu nó đưuocj import vào tệp khác, hàm main() sẽ không tự động chạy
    main()