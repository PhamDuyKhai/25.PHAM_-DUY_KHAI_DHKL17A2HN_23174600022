import json
obj_py = {
    "Alice": {
        "address": "123 Elm St",
        "phone": "0123456789",
        "exam_score": 85
    },
    "Bob": {
        "address": "456 Oak St",
        "phone": "0987654321",
        "exam_score": 90
    },
    "Charlie": {
        "address": "789 Pine St",
        "phone": "0112233445",
        "exam_score": 78
    },
    "David": {
        "address": "321 Maple St",
        "phone": "0223344556",
        "exam_score": 88
    },
    "Eve": {
        "address": "654 Cedar St",
        "phone": "0334455667",
        "exam_score": 92
    },
    "Frank": {
        "address": "987 Birch St",
        "phone": "0445566778",
        "exam_score": 76
    },
    "Grace": {
        "address": "123 Spruce St",
        "phone": "0556677889",
        "exam_score": 95
    },
    "Hannah": {
        "address": "456 Willow St",
        "phone": "0667788990",
        "exam_score": 82
    },
    "Ivy": {
        "address": "789 Ash St",
        "phone": "0778899001",
        "exam_score": 88
    },
    "Jack": {
        "address": "321 Poplar St",
        "phone": "0889900112",
        "exam_score": 91
    }
}


obj_json = json.dumps(obj_py,indent = 4, sort_keys = True)
print(obj_json)