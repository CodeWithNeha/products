# Product Management REST APIs

This project provides a set of REST APIs built using Django REST Framework for managing products. It includes APIs for creating, deleting, editing, listing all products, and retrieving details about a single product. Additionally, it provides an API to fetch the top 5 products that were retrieved the maximum number of times.

## Installation

1. Clone the repository: `git clone https://github.com/CodeWithNeha/products.git`
2. Change to the project directory: `cd products`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
5. Install the dependencies: `pip install -r requirements.txt`
6. Run database migrations: `python manage.py migrate`

## Usage

1. Start the development server: `python manage.py runserver`
2. The APIs will be accessible at `http://localhost:8000/`.

## API Endpoints

### Product Management APIs

- **Create a Product:**
  - Endpoint: `POST /products/`
  - Request body: JSON object containing product details (e.g., name)
  - Response: JSON object representing the created product
  - curl --location 'http://127.0.0.1:8000/api/products/' \
        --form 'title="\"12389458686866\""' \
        --form 'description="\"details\""' \
        --form 'price="12.90"'

- **Delete a Product:**
  - Endpoint: `DELETE /products/{id}/`
  - Path parameter: `{id}` represents the ID of the product to be deleted
  - Response: JSON object indicating the success of the deletion operation
  - curl --location --request DELETE 'http://127.0.0.1:8000/api/products/1/'

- **Edit a Product:**
  - Endpoint: `PUT /products/{id}/`
  - Path parameter: `{id}` represents the ID of the product to be edited
  - Request body: JSON object containing updated product details
  - Response: JSON object representing the updated product
  - curl --location --request PUT 'http://127.0.0.1:8000/api/products/1/' \
    --form 'title="123 Product"' \
    --form 'description="details"' \
    --form 'price="12.90"'

- **List all Products:**
  - Endpoint: `GET /products/`
  - Response: JSON array containing all products
  - curl --location 'http://127.0.0.1:8000/api/products/'

- **Retrieve Details about a single Product:**
  - Endpoint: `GET /products/{id}/`
  - Path parameter: `{id}` represents the ID of the product to be retrieved
  - Response: JSON object representing the product details
  - curl --location 'http://127.0.0.1:8000/api/products/3/'

### Top 5 Products APIs

- **Top 5 Products (All Time):**
  - Endpoint: `GET /fetchMostSearched/?filterBy=all`
  - Response: JSON array containing the top 5 products retrieved the maximum number of times (based on `retrieval_count`)
  - curl --location 'http://127.0.0.1:8000/api/fetchMostSearched/?filterBy=all'


- **Top 5 Products (Last Day):**
  - Endpoint: `GET /fetchMostSearched/?filterBy=lastDay`
  - Response: JSON array containing the top 5 products retrieved the maximum number of times in the last day
  - curl --location 'http://127.0.0.1:8000/api/fetchMostSearched/?filterBy=lastDay'

- **Top 5 Products (Last Week):**
  - Endpoint: `GET /fetchMostSearched/?filterBy=lastWeek`
  - Response: JSON array containing the top 5 products retrieved the maximum number of times in the last week
  - curl --location 'http://127.0.0.1:8000/api/fetchMostSearched/?filterBy=lastWeek'

