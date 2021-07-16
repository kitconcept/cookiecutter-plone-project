# {{ cookiecutter.project_title }}

    Dev Instance: https://{{ cookiecutter.repository }}.kitconcept.io/de
    Trello:

## Development Setup

### Prerequisites

- Python 3.8 (Ubuntu: "sudo apt install python3")
- Node 14 (Ubuntu: "sudo apt install nodejs")
- Yarn (Ubuntu: "npm install -g yarn")

### System Dependencies

```
# Make & Build
apt install build-essential
# VCS
apt install git-core
# Python 3
apt install python3-dev
apt install python3-virtualenv
# Python
apt install python3-pip
apt install python-tk
# Pillow
apt install zlib1g-dev
apt install libfreetype6
apt install libfreetype6-dev
apt install libjpeg62-dev
# Lxml
apt install python-lxml
apt install libxslt1-dev
apt install libxml2-dev
apt install libxml2-utils
apt install libssl-dev
```

### Setup

Git Checkout:

```git checkout git@github.com:kitconcept/{{ cookiecutter.repository }}.git```

Local setup:

```make```

Run Static Code Analysis:

```make code-Analysis```

Run Unit / Integration Tests:

```make test```

Run Acceptance Tests:

```make test-acceptance```


# Code

    Code Repository: https://github.com/kitconcept/{{ cookiecutter.repository }}
    Continous Integration: https://jenkins.kitconcept.io/job/kitconcept/job/{{ cookiecutter.repository }}/


# Project Management

    Trello: https://trello.com/
    Harvest: https://kitconcept.harvestapp.com/


# Server

    Live: www.example.com
    Staging: www.example.com
    Dev: {{ cookiecutter.repository }}.kitconcept.io (automatically deployed and set up via CI)
    
# Changelog Format

* Use present tense (Adding -> Add, Added -> Add, Fixing -> Fix, Fixed -> Fix, Removed -> Remove, etc.)
* Use simple sentences (e.g. "Fix adding a new icon")
* Always provide your gh username at the end (e.g. "Fix adding a new icon @tisto")
* Always provide a ticket number (e.g. "Fix adding a new icon (#2343) @tisto")

## Bad

````
- Fixed an issue with the icon because it did not work for the client
````

## Good

````
- Fix adding a new icon in the Icon Grid Block (#8328) @tisto
````

