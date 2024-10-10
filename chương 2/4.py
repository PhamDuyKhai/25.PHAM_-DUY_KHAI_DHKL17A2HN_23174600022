import xml.dom.minidom

def main():
    # Đọc và phân tích file 'sample.xml'
    doc = xml.dom.minidom.parse("sample.xml")
    
    # Lấy danh sách tất cả các phần tử trong file
    elements = doc.getElementsByTagName("*")
    
    # In ra tên của từng phần tử
    print("Tên các phần tử trong file sample.xml:")
    for element in elements:
        print(element.tagName)

if __name__ == "__main__":
    main()
