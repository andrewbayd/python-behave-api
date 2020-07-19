# API TESTS WITH PYTHON AND BEHAVE

I tried to create simple api testing framework for https://developer.todoist.com/rest/v1/ using python requests package and BDD framework behave.
In my opinion using BDD for API tests helps to make tests more readable and business logic more clear to new QAs in the team and business users.

In order to run tests:
1. Clone repo
2. Create virtual environment https://docs.python.org/3/library/venv.html
3. Install requirements `pip install -r requirements.txt`
4. Register on https://todoist.com/app/ to get API token
5. Run `apitoken=your_api_token behave`
