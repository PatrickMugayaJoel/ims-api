# ims-api
[![Build Status](https://travis-ci.com/wewillneverfail/ims-api.svg?branch=ch-integrate-travis-ci-with-api)](https://travis-ci.com/wewillneverfail/ims-api)
[![Maintainability](https://api.codeclimate.com/v1/badges/3ab15ace0008cb929379/maintainability)](https://codeclimate.com/github/wewillneverfail/ims-api/maintainability) [![Coverage Status](https://coveralls.io/repos/github/wewillneverfail/ims-api/badge.svg?branch=develop)](https://coveralls.io/github/wewillneverfail/ims-api?branch=develop)

ims is a trip management system that is used to schedule and create itineraries, track the progress of an individual trip, predict trip actions to help tour operators make clear and informed business decisions.

### Tech Stacks
- Python
- Django
- djangorestframework
- postgresql

## Installation

### Pre-requirements.
- Install [python](https://www.python.org/downloads/)
- install [Postgresql](https://www.postgresql.org/download/)

### Installation steps.
- Clone the [repository](https://github.com/wewillneverfail/ims-api)
- Create a `.env` file. See the `.env_example` in the root directory.
- Install a [virtual environment](https://virtualenv.pypa.io/en/latest/installation/).
- Activate the virtual environment and export the environment variables.
- Run `$ pip3 install -r requirements.txt` to install dependencies.
- Run `$ python3 manage.py makemigrations` to generate migrations.
- Run `$ python3 manage.py migrate` to add database tables.
- Run `$ python3 manage.py runserver` to start the local server.

### Testing

### Changes
See [CHANGELOG.md](https://github.com/wewillneverfail/ims-api/blob/master/docs/CHANGELOG.md) for detailed list of changes between releases.

### Upgrade
See [UPGRADE.md](https://github.com/wewillneverfail/ims-api/blob/master/docs/UPGRADE.md) for information about actions needed when upgrading.

For production use we recommend you to upgrade only when new version is released and not to follow the master branch.

### Release
See [RELEASE.md](https://github.com/wewillneverfail/ims-api/blob/master/docs/RELEASE.md) for information about how to make a new release.

### Bug Tracker
Browse open issues and submit new ones in [Github Issues](https://github.com/wewillneverfail/ims-api/issues).

We are dedicating the Github Issue only for bugs in our codebase. For general questions, start a new thread in the [Community forum]() instead of opening a new Issue.

After you have opened a new issue, the team will handle it according to these instructions: [How to handle Github Issues](https://github.com/wewillneverfail/ims-api/blob/master/docs/how-to-handle-github-issues.md)
