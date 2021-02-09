import os

from datetime import datetime
from github import Github

# using token
g = Github(os.environ['TOKEN'])

with open(os.environ['REPOS_FILE'], 'r') as repos_file, \
        open(os.environ['OUTPUT_FILE'], 'w') as output:
    # for csv title
    print("title", "state", "created_at", "user_name", "html_url", sep=',', file=output)

    for repo_name in repos_file:
        if repo_name[-1] == "\n":
            repo_name = repo_name[:-1]
        repo = g.get_repo(repo_name)

        with open(os.environ['USERS_FILE'], 'r') as users_file:

            for user in users_file:
                if user[-1] == "\n":
                    user = user[:-1]
                BEGIN_DATE = datetime.strptime(os.environ['BEGIN_DATE'], "%m/%d/%y")
                END_DATE = datetime.strptime(os.environ['END_DATE'], "%m/%d/%y")
                # print(os.environ['STATE'])
                open_issues = repo.get_issues(state=os.environ['STATE'], creator=user)

                for issue in open_issues:
                    if BEGIN_DATE <= issue.created_at <= END_DATE:
                        print(issue.title, issue.state, issue.created_at, issue.user.name, issue.html_url, sep=',',
                              file=output)
