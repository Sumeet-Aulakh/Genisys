import github
from github import Github, GithubException, UnknownObjectException
from github import Auth
from dotenv import dotenv_values, load_dotenv
import subprocess

def githubInit():
    load_dotenv()
    github_token = dotenv_values().get("GITHUB_TOKEN")
    if github_token == None:
        print("Github token not found")
        return Exception("Github token not found")
    auth = Auth.Token(github_token)
    return Github(auth=auth)

def getRepos():
   for repo in githubInit().get_user().get_repos():
       print(repo.name)

def createRepo(title: str, repoName: str, description: str):
    print("Creating new repo")
    user = githubInit().get_user()
    try:
        repo = user.get_repo(repoName)  # Assuming 'title' is the repo name
        print(f"Repo '{title}' already exists.")
    except UnknownObjectException:
        # Repo doesn't exist, create it
        print(f"Creating repo '{repoName}'...")
        repo = user.create_repo(
            name=repoName,
            description=description,
            private=False,
        )
        print(f"Created repo '{repoName}'")
    print("Repo created: ", repo)
    return repo



def doGitStuff(title, repoName, description) -> None:

    githubInit()

    username = dotenv_values().get("GITHUB_USERNAME")
    token = dotenv_values().get("GITHUB_SIGNIN_TOKEN")
    remote_url = f"https://{username}:{token}@github.com/{username}/{repoName}.git"
    project_dir = "project"

    createRepo(title, repoName, description)

    subprocess.run(["git", "init"], cwd=project_dir)
    git_user_name = dotenv_values().get("GIT_USER_NAME") or "Genisys User"
    git_user_email = dotenv_values().get("GIT_USER_EMAIL") or "user@example.com"
    subprocess.run(["git", "config", "user.name", git_user_name], cwd=project_dir)
    subprocess.run(["git", "config", "user.email", git_user_email], cwd=project_dir)
    subprocess.run(["git", "checkout", "-b", "main"], cwd=project_dir)
    subprocess.run(["git", "remote", "add", "origin", remote_url], cwd=project_dir)

    # Add, commit, push
    subprocess.run(["git", "add", "."], cwd=project_dir)
    subprocess.run(["git", "commit", "-m", "Auto commit via script"], cwd=project_dir)
    subprocess.run(["git", "push", "-u", "origin", "main", "--force"], cwd=project_dir)

    print("Created repo: ", repoName)
    print('Go to https://github.com/{username}/{repoName} to view your new repository.')
    # getRepos()