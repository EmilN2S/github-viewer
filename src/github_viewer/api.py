import httpx


class GithubViewer:
    def __init__(self, username: str) -> None:
        self.username = username
    
    def profile(self) -> dict | None:
        response = httpx.get(
            f'https://api.github.com/users/{self.username}',
            timeout=20
        )
        response.raise_for_status()
        return response.json()
