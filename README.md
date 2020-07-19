#API TESTS WITH PYTHON AND BEHAVE

I tried to create simple api testing framework for https://developer.todoist.com/rest/v1/ using python requests package and BDD framework behave.
In my opinion using BDD for API tests helps to make tests more readable and business logic more understandable.

In order to run tests:
1. Clone repo
2. Install requirements `pip install -r requirements.txt`
3. Register on https://todoist.com/app/ to get API token
4. Paste your token in steps module
5. Simply run `behave`