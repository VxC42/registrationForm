import re

NAME = re.compile(r'^[a-zA-z]+$')
EMAIL = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

def formIsValid(client):
    errors=[]
    isValid=True
    if len(client['first_name'])<1:
        errors.append("Please enter a first name.")
        isValid = False
    if len(client['last_name'])<1:
        errors.append("Please enter a last name.")
        isValid = False
    if len(client['email'])<1:
        errors.append("Please enter an email.")
        isValid = False
    if len(client['pw'])<1:
        errors.append("Please enter a password.")
        isValid = False
    if len(client['confirm_pw'])<1:
        errors.append("Please confirm your password.")
        isValid = False
    if not re.match(NAME, client['first_name']) and not re.match(NAME, client['last_name']):
        errors.append("Names must only include letters.")
        isValid=False
    if not re.match(EMAIL, client['email']):
        errors.append("Not a valid Email address.")
        isValid = False
    if client['pw'] != client['confirm_pw']:
        errors.append("Passwords do not match.")
        isValid = False
    if not re.match(PASSWORD, client['pw']):
        errors.append("Passwords must have at least one uppercase and one numerical value")
        isValid = False
    return {"isValid":isValid, "errors":errors}
