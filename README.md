# InvoiceAPI
A simple API using Django REST Framework. The API will manage invoices and their details.It involves creating a nested serializer and an endpoint to create and update an invoice along with its details through a single request.

## Setup Instructions

### Requirements
- Python 3.x
- Django 4.x
- Django REST Framework

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/jumanapa07/InvoiceAPI
    cd InvoiceAPI
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv env
    env\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

6. Start the Django development server:
    ```bash
    python manage.py runserver
    ```

### Endpoints

- **POST** `/api/invoices/` - Create a new invoice with details.
- **PUT** `/api/invoices/<id>/` - Update an existing invoice and its details.

### Sample Payload

#### POST Request
```json
{
    "invoice_number": "INV001",
    "customer_name": "John Doe",
    "date": "2024-11-12",
    "details": [
        {
            "description": "Item A",
            "quantity": 2,
            "price": 50.00
        },
        {
            "description": "Item B",
            "quantity": 1,
            "price": 100.00
        }
    ]
}
  
