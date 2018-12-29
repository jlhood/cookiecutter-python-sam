"""Post create hook that pushes initial app skeleton to new GitHub repository.
"""

import os
import subprocess

TERMINATOR = "\x1b[0m"
INFO = "\x1b[1;33m [INFO]: "
SUCCESS = "\x1b[1;32m [SUCCESS]: "
HINT = "\x1b[3;33m"


def main():
    project_name = '{{ cookiecutter.project_name }}'
    push_to_github = '{{ cookiecutter.push_to_github }}' == 'y'
    git_fullname = '{{ cookiecutter.git_fullname }}'
    github_username = '{{ cookiecutter.github_username }}'
    github_email = '{{ cookiecutter.github_email }}'

    print(INFO + "Bootstrapping project." + TERMINATOR)
    rc = subprocess.call(['make', 'bootstrap'])
    if rc != 0:
        raise RuntimeError('Bootstrap failed')

    print(INFO + "Initializing git repo." + TERMINATOR)
    subprocess.call(['git', 'init'])

    print(INFO + "Configuring user.name to {}".format(git_fullname) + TERMINATOR)
    subprocess.call(['git', 'config', 'user.name', git_fullname])
    print(INFO + "Configuring user.email to {}".format(github_email) + TERMINATOR)
    subprocess.call(['git', 'config', 'user.email', github_email])

    subprocess.call(['git', 'add', '.'])
    subprocess.call(['git', 'commit', '-m', 'Initial app from template'])

    if push_to_github:
        print(INFO + "Pushing to GitHub." + TERMINATOR)
        remote = 'https://github.com/{}/{}.git'.format(github_username, project_name)
        subprocess.call(['git', 'remote', 'add', 'origin', remote])
        rc = subprocess.call(['git', 'push', '-u', 'origin', 'master'])
        if rc != 0:
            raise RuntimeError('Failed to push to GitHub remote: {}'.format(remote))
        print(SUCCESS + 'https://github.com/{}/{} updated.'.format(github_username, project_name) + TERMINATOR)

    print(SUCCESS + "cd to {} and start coding!".format(project_name) + TERMINATOR)


if __name__ == '__main__':
    main()
