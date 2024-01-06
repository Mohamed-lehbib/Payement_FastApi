# Payement System

A Simulation of a payement gateway

## How to use this api ?

1. Install the requirements

```
pip install -r requirements.txt
```

2. Check the [database.py](app/database.py) the database url if it matches yours
3. Run the server

```
uvicorn app.main:app --reload
```

4. Navigate To the Swagger interface to see all the endpoint that this api offer and what is the format required ([click here](http://127.0.0.1:8000/docs#/) )
5. Make requests using curl or any other tool that can make http request like Postman,
6. Enjoy now u have an api that u can use just integrate it wherever u want

## Endpoints affored by this api

| Method | Endpoint url                                           | Description                                                           |
| ------ | ------------------------------------------------------ | --------------------------------------------------------------------- |
| POST   | http://127.0.0.1:8000/create_client                    | To create a Client that can have a Banque account                     |
| POST   | http://127.0.0.1:8000/create_account                   | To create a Banque account for a client                               |
| POST   | http://127.0.0.1:8000/create_card                      | To create a Card like credit card or visa or master                   |
| GET    | http://127.0.0.1:8000/account_balance/{account_number} | To check the account balance                                          |
| GET    | http://127.0.0.1:8000/card_balance/{card_number}       | To check the card balance                                             |
| POST   | http://127.0.0.1:8000/make_payement                    | To do a transaction using the card info and account number and amount |
