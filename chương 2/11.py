import json
from datetime import datetime

class GiaoDich:
    def __init__(self, loai, ngay, so_tien, so_vang):
        self.loai = loai
        self.ngay = ngay
        self.so_tien = so_tien
        self.so_vang = so_vang

    def to_dict(self):
        return {
            'Loai': self.loai,
            'Ngay': self.ngay,
            'SoTien': self.so_tien,
            'SoVang': self.so_vang
        }

def ghi_giao_dich_vao_tep_tin(ngay, giao_dich_list):
    tep_tin = f"{ngay}.json"

    with open(tep_tin, 'w') as f:
        json.dump([gd.to_dict() for gd in giao_dich_list], f)

def main():
    giao_dich_list = []
    
    while True:
        loai = input("Nhập loại giao dịch (Tiền/Vang): ").capitalize()
        ngay = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        so_tien = float(input("Nhập số tiền: "))
        so_vang = float(input("Nhập số vàng: "))

        giao_dich = GiaoDich(loai, ngay, so_tien, so_vang)
        giao_dich_list.append(giao_dich)

        tiep_tuc = input("Tiếp tục giao dịch? (1: Có, 0: Không): ")
        if tiep_tuc != '1':
            break

    if giao_dich_list:
        ghi_tep_tin = input("Bạn có muốn ghi vào tệp tin không? (1: Có, 0: Không): ")
        if ghi_tep_tin == '1':
            ngay_hien_tai = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            ghi_giao_dich_vao_tep_tin(ngay_hien_tai, giao_dich_list)
            print(f"Ghi vào tệp tin {ngay_hien_tai}.json thành công.")

if __name__ == "__main__":
    main()
