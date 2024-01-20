import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name}
        )
        body = r.json()

        return body

    def search_users_repo(self, name):
        r = requests.get(
            f"https://api.github.com/users/{name}/repos"
        )
        body = r.json()

        return body

    def get_emojis_list(self):
        response = requests.get("https://api.github.com/emojis")
        body = response.json()

        return body

    def get_commit_list(self):
        response = requests.get(
            "https://api.github.com/repos/sergii-butenko/become-qa-auto-oct/commits",
            params={"per_page": 50}
        )
        body = response.json()

        return body

    def get_branch_list(self):
        response = requests.get(
            "https://api.github.com/repos/sergii-butenko/become-qa-auto-oct/branches"
        )
        body = response.json()

        return body
