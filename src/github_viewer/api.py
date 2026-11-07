import requests


class GithubRequests:
    def __init__(self, username):
        self.username = username
    
    def profile(self) -> dict | None:
        try:
            response = requests.get(
                f'https://api.github.com/users/{self.username}',
                timeout=20
            )
            response.raise_for_status()
            return response.json()

        except requests.RequestException:
            return None
