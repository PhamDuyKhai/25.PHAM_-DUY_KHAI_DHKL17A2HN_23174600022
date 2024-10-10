import xml.dom.minidom

def main():
    # Sử dụng phương thức parse() để đọc và phân tích file 'DOM.xml'
    doc = xml.dom.minidom.parse("DOM.xml")
    
    # In ra tên của node gốc và tag name của node đầu tiên trong file .xml
    print("Node gốc:", doc.nodeName)  # In ra tên node gốc
    print("Tag đầu tiên:", doc.firstChild.tagName)  # In ra tag name của node đầu tiên

    # Lấy danh sách các phần tử 'staff' trong file xml
    staff_elements = doc.getElementsByTagName("staff")
    print("%d nhân viên:" % staff_elements.length)  # In ra số lượng phần tử 'staff'
    
    # Duyệt danh sách các phần tử 'staff'
    for staff in staff_elements:
        print("ID nhân viên:", staff.getAttribute("id"))  # In ra thuộc tính 'id' của từng phần tử 'staff'
        name = staff.getElementsByTagName("name")[0].childNodes[0].nodeValue
        salary = staff.getElementsByTagName("salary")[0].childNodes[0].nodeValue
        print("Tên:", name)
        print("Lương:", salary)
     
if __name__ == "__main__":
    main()
    