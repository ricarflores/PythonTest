# PythonTest

Requeriments

Python 3, 
Pip

To Run:

Intall Dependencies

- pip install -r requeriments.txt

Run server:

- python run server.py

Test

Open collection (PythonTest.postman_collection.json) in postman to access to the endpoint

GET /wather/time

URL: http://localhost:5050/wather/time

Correct Response

{
    "data": [
        {
            "date": "1/2/20",
            "was_rainy": true
        },
        {
            "date": "1/6/20",
            "was_rainy": true
        },
        {
            "date": "1/8/20",
            "was_rainy": true
        }
    ],
    "error": false,
    "success": true
}

Error Response 

{
    "data": [],
    "error": true,
    "success": false
}

GET /season/ordes

URL http://localhost:5050/season/ordes

Correct Response

{
    "data": [
        {
            "ORD_ID": 1,
            "SEASON": "Fall"
        },
        {
            "ORD_ID": 2,
            "SEASON": "Winter"
        },
        {
            "ORD_ID": 3,
            "SEASON": "Fall"
        },
        {
            "ORD_ID": 4,
            "SEASON": "Fall"
        },
        {
            "ORD_ID": 5,
            "SEASON": "Winter"
        },
        {
            "ORD_ID": 6,
            "SEASON": "Spring"
        },
        {
            "ORD_ID": 7,
            "SEASON": "Spring"
        },
        {
            "ORD_ID": 8,
            "SEASON": "Fall"
        }
    ],
    "error": false,
    "success": true
}

Error Response

{
    "data": "Error Proces",
    "error": true,
    "success": false
}

GET /costume/ordes

URL http://localhost:5050/costume/ordes

Correct Response 
{
    "data": [
        {
            "order_number": "ORD_1567",
            "status": "PENDING"
        },
        {
            "order_number": "ORD_1234",
            "status": "SHIPPED"
        },
        {
            "order_number": "ORD_9834",
            "status": "SHIPPED"
        },
        {
            "order_number": "ORD_7654",
            "status": "CANCELLED"
        }
    ],
    "error": false,
    "success": true
}

Error Response

{
    "data": "Error Proces",
    "error": true,
    "success": false
}
