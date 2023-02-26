# iou_tracker
tracking api for money transfers

The IOU Tracker is a simple web application that allows users to track how much money they owe each other. The application is built using Django and provides a RESTful API that allows users to create and manage IOUs.

Features
The IOU Tracker includes the following features:

Users can be created and deleted.
IOUs can be created and deleted between users.
The application calculates the balance for each user, which is the difference between the amount owed to them and the amount they owe to others.
Installation
To install and run the IOU Tracker, follow these steps:

Clone the repository:

```git clone https://github.com/simran-singh-1902/iou_tracker.git```

```cd iou-tracker```

Download requirements:

```pip install -r requirements.txt```

Create the database tables:

```python manage.py migrate```

Start the development server:

```python manage.py runserver```

Access the application by visiting http://localhost:8000 in your web browser.

<h3>API Reference</h3>

The IOU Tracker provides a RESTful API that allows users to create and manage IOUs. The following endpoints are available:

<h4>Returns a list of all users in the system.</h4>

GET /users/

Response

```json
{
    "name": "Simran"
},
{
    "name": "Muskan"
}
```


<h4>Creates a new user.</h4>

POST /add/

Payload format:

```json
{
    "name": "Simran"
}
```

<h4>Creates a new IOU between two users.</h4>

POST /iou/

Payload format:

```json
{
    "id": 1,
    "from": "Ankit",
    "to": "Sachin",
    "amount": 30.0
}
```


<h4>Returns all the user data:</h4>

GET /ledger/

Response

```json
[
    {
        "id": 11,
        "name": "Simran",
        "owes": {},
        "owed_by": {
            "Muskan": 1000
        },
        "balance": {
            "owed": 1000,
            "owes": 0,
            "net_balance": 1000
        }
    },
    {
        "id": 12,
        "name": "Muskan",
        "owes": {
            "Simran": 1000
        },
        "owed_by": {},
        "balance": {
            "owed": 0,
            "owes": 1000,
            "net_balance": -1000
        }
    }
]
