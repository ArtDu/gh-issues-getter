import os

from datetime import datetime
from github import Github

USERS_FILE = os.getenv('USERS_FILE') or 'users.txt'
REPOS_FILE = os.getenv('REPOS_FILE') or 'repos.txt'
OUTPUT_FILE = os.getenv('OUTPUT_FILE') or 'issues.csv'
STATE = state=os.getenv('STATE') or 'all'

# using token
g = Github(os.environ['TOKEN'])

with open(REPOS_FILE, 'r') as repos_file, \
        open(OUTPUT_FILE, 'w') as output:
    # for csv title
    print("repo", "title", "state", "created_at", "user_name", "html_url", sep=',', file=output)

    for repo_name in repos_file:
        if repo_name[-1] == "\n":
            repo_name = repo_name[:-1]
        repo = g.get_repo(repo_name)

        with open(USERS_FILE, 'r') as users_file:

            for user in users_file:
                if user[-1] == "\n":
                    user = user[:-1]
                BEGIN_DATE = datetime.strptime(os.environ['BEGIN_DATE'], "%m/%d/%y")
                END_DATE = datetime.strptime(os.environ['END_DATE'], "%m/%d/%y")
                # print(os.environ['STATE'])
                issues = repo.get_issues(state=STATE, creator=user)

                for issue in issues:
                    if BEGIN_DATE <= issue.created_at <= END_DATE:
                        print(repo_name, issue.title, issue.state, issue.created_at, issue.user.name, issue.html_url, sep=',',
                              file=output)

        print("done for repo {0}".format(repo_name))
