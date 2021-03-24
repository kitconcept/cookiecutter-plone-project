.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
{{cookiecutter.project_title}}
==============================================================================

.. image:: https://kitconcept.com/logo.svg
   :alt: kitconcept
   :target: https://kitconcept.com/


Development
-----------

Requirements:

- Python 2.7
- Virtualenv

Setup::

  make

Run Static Code Analysis::

  make code-Analysis

Run Unit / Integration Tests::

  make test

Run Robot Framework based acceptance tests::

  make test-acceptance


Theme
------

In case that the build contains a theme, in order to develop it, move to the
project root, then::

  yarn

then for start the watcher::

  yarn start


Code
----

Code Repository: https://github.com/kitconcept/{{cookiecutter.project_namespace}}
Continous Integration: https://jenkins.kitconcept.io/job/kitconcept/job/{{cookiecutter.project_namespace}}/


Project Management
------------------

Trello: https://trello.com/...
Harvest: https://kitconcept.harvestapp.com/projects/...


Server
------

Live: www.example.com
Staging: {{cookiecutter.project_namespace}}.kitconcept.io (Deploy automatically from main branch)

