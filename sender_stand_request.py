import requests
import configuration


def post_new_user(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body
    )


def post_new_kit(body, auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
        json=body,
        headers=headers
    )