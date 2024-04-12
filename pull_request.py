import requests


def create_pull_request(token, owner, repo, title, head, base):
    url = f'https://api.github.com/repos/{owner}/{repo}/pulls'
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'title': title,
        'head': head,
        'base': base
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print("Pull request created successfully!")
        return response.json()
    else:
        print(f"Failed to create pull request: {response.status_code}")
        print(response.text)
        return None


# Example usage:
token = 'token'
owner = 'ANoska'
repo = 'sandbox'
title = 'My Pull Request'
head = 'test-branch'
base = 'main'

result = create_pull_request(token, owner, repo, title, head, base)
if result:
    print("Pull request URL:", result['html_url'])
