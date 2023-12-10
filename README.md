# CA349-Project

Jira:
https://nadishwara.atlassian.net/browse/KAN-29


# Prototype application of ca349.

### Create virtual environment:

##### Windows: 
create: `py -m venv venv`

activate: `venv\Scripts\activate.bat`

##### MacOS:
create: `python3 -m venv venv`

activate: `source venv/bin/activate`

### install requirements:
`pip install -r requirements.txt`

### Payment test

| Brand      | Card Number      | CVV              | Expired Date    |
|------------|------------------|------------------|-----------------|
| Visa       | 4242424242424242 | Any three digits | Any future date |
| Mastercard | 5555555555554444 | Any three digits | Any future date |

### Administrator Account
superuser: `admin`

password: `student349`

### Keep Django run on ec2
```shell
screen
sudo python3 manage.py runserver 0.0.0.0:80
```
Then:

Press `Ctrl+A` then `D`

## Group member:
Jervis Chen

Nadishwara Dalevadoo

Beibei Pan

Anzhe Yuan
