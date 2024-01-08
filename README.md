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
| POST   | http://127.0.0.1:8000/deposit_to_card                  | To deposit an amount to a card                                        |

## Documentation

To create this api i have done some steps:

- Step 1: I have created a folder
- Step 2: I have created a python environment

```
python3.11 -m venv env
```

and I have activated it

```
source env/bin/activate
```

- Step 3: I have installed all the packages needed for this project in the `requirements.txt`
- Step 4: I have created the `app` folder
- Step 5: I have created under it the `main` file that contains the api endpoint and logic
- Step 6: I have created the `database` file that contains the connexion with the database
- Step 7: I have created the `model` file that contains all the models
- Step 8: I have created the `schemas` file that contains the schemas
- Step 9: I have run the project

```
uvicorn app.main:app --reload
```

after run this command the server will start and i get the models will be created in the database

# Automating the git commands

creating a bash script that automate this repetitive task [git-automation.sh](git-automation.sh)
and I need to add execute permission to it

```
chmod +x git-automation.sh
```

and then run it

```
./git-automation.sh "Commit message" branch
```

example:

```
./git-automation.sh "modifying the readme file" main
```
