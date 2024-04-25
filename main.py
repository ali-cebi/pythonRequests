import json
import requests
import random

# CONSTANTS
base_url = "https://gorest.co.in"
auth_token = "Bearer ACCESS TOKEN"


# RANDOM EMAIL ADDRESS GENERATOR
def create_random_email():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
               "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ]
    i = 0
    while i < 6:
        random_letter = random.choice(letters)
        if i == 0:
            email = random_letter
        else:
            email += random_letter
        i += 1

    return email + '@alimail.com'


# GET REQUEST
def get_all_users():
    url = base_url + "/public/v2/users"
    headers = {"Authorization": auth_token}

    r = requests.get(url, headers=headers)
    assert r.status_code == 200
    response_body = r.json()
    response_str = json.dumps(response_body, indent=4)
    print(response_str)


# POST REQUEST
def create_user():
    user_email = create_random_email()
    url = base_url + "/public/v2/users"
    headers = {"Authorization": auth_token}
    data = {
        "name": "John Cebi",
        "email": user_email,
        "gender": "male",
        "status": "active"
    }
    r = requests.post(url, json=data, headers=headers)
    assert r.status_code == 201
    response_body = r.json()
    user_id = response_body["id"]
    data["id"] = user_id
    return data


# GET REQUEST
def get_specific_user():
    user = create_user()
    url = base_url + "/public/v2/users/" + str(user["id"])
    headers = {"Authorization": auth_token}

    r = requests.get(url, headers=headers)
    assert r.status_code == 200
    response_body = r.json()
    response_str = json.dumps(response_body, indent=4)
    print(response_str)


# PUT REQUEST
def update_user():
    user = create_user()
    url = base_url + "/public/v2/users/" + str(user["id"])
    headers = {"Authorization": auth_token}

    print("First version: \n" + str(user))

    user["email"] = create_random_email()

    r = requests.put(url, json=user, headers=headers)
    assert r.status_code == 200
    response_body = r.json()

    print("Final version: \n" + str(response_body))


# DELETE REQUEST
def delete_user():
    user = create_user()
    url = base_url + "/public/v2/users/" + str(user["id"])
    headers = {"Authorization": auth_token}

    print("User: \n" + str(user))

    r = requests.delete(url, headers=headers)
    assert r.status_code == 204
    if r.status_code == 204:
        print("user deleted")


# get_all_users()
# post_request()
# get_specific_user()
# update_user()
delete_user()
