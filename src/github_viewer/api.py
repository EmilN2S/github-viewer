import requests


def profile(username: str) -> dict | None:
    try:
        response = requests.get(
            f'https://api.github.com/users/{username}',
            timeout=20
        )
        response.raise_for_status()
        return response.json()

    except requests.RequestException:
        return None
