<h1 align="center">Welcome to Frost_Fashion 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

> Django ecommerce app for online shopping

## Author

👤 **FrodenZ Labs**

* Website: stephen-kibe.netlify.app
* LinkedIn: [@stephen-kibe](https://linkedin.com/in/stephen-kibe)
  
## UX

The website was created to be eye-catching and user-friendly. The user is given plenty of choices to choose from when they are shopping. The emphasis is on the user experience; the user can navigate the website easily to fulfill users' goals. The website is designed to be easy to use and easy to understand. Additionally, the website attracts customers to become a part of loyalty programs by giving them additional discounts on their purchases.
It also handles all personnel functionality moving from admin to manager to logistics to other personnel.
Business goals were to make the website as scalable as possible and reusable in the real world so that the store personnel could use it according to their position in the company.

## Features of this Project

### A. Admin Users Can
1. Manage Category (Add, Update, Filter and Delete)
2. Manage Products (Add, Update, Filter and Delete)
3. Manage Users (Update, Filter and Delete)
4. Manage Orders (View and Process)

### B. Non-Registered Users Can
1. View Products (Can filter based on category)
2. Explore Product Details and Related Products


### C. Registered Users Can Can
1. All ot Non-Registered Users
2. Add to Cart
3. Pay with PayPal or Debit/Credit Card and Order
4. See the Order Status
5. See Order History
6. Update Profile 
7. Change Password
8. Reset Password

## How to Install and Run this project?

### Pre-Requisites:
1. Install Git Version Control
[ https://git-scm.com/ ]

2. Install Python Latest Version
[ https://www.python.org/downloads/ ]

3. Install Pip (Package Manager)
[ https://pip.pypa.io/en/stable/installing/ ]

*Alternative to Pip is Homebrew*

### Installation
**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

For Windows
```
$  python -m venv venv
```
For Mac
```
$  python3 -m venv venv
```

Activate Virtual Environment

For Windows
```
$  source venv/scripts/activate
```

For Mac
```
$  source venv/bin/activate
```

**3. Clone this project**
```
$  git clone https://github.com/Dispenser254/Frost_Fashion.git
```

Then, Enter the project
```
$  cd Frost_Fashion
```

**4. Install Requirements from 'requirements.txt'**
```python
$  pip install -r requirements.txt
```

**5. Add the hosts**

- Got to settings.py file 
- Then, On allowed hosts, Add [‘*’]. 
```python
ALLOWED_HOSTS = ['*']
```
*No need to change on Mac.*


**6. Now Run Server**

Command for PC:
```python
$ python manage.py runserver
```

Command for Mac:
```python
$ python3 manage.py runserver
```

**7. Login Credentials**

Create Super User (Admin)

Command for PC:
```
$  python manage.py createsuperuser
```

Command for MAC:
```
$  python3 manage.py createsuperuser
```
Then Add Email, Username and Password

## Contribute to the Project

Your contributions play a crucial role in enhancing this platform. I invite developers of all levels to get involved:

1. Fork the repository.
2. Create a feature branch: `git checkout -b your-feature-name`.
3. Commit your changes: `git commit -m 'Added feature XYZ'`.
4. Push to your branch: `git push origin your-feature-name`.
5. Open a pull request to share your enhancements and engage in discussions.
## Show your support

Give a ⭐️ if this project helped you!

***
