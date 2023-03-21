from flask import session

# This is a very basic dictionary with information for logging in
# Simulating our database
thisDict = {
    "email": "john.doe@upr.edu",
    "password": "1",
    "user": "John"
}


def loginmodel(email, password):
    # Receive email and password to check in the "database"
    if email in thisDict.values() and password in thisDict.values():
        # If it found the email and pass in the dictionary
        session['customer'] = thisDict['user']
        # Create the session['customer']
        return "true"
    else:
        # If it didn't find user
        return "false"
