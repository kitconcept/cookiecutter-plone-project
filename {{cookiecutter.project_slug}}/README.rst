.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
{{cookiecutter.project_name}}
==============================================================================

.. image:: https://raw.githubusercontent.com/kitconcept/{{cookiecutter.project_slug}}.core/master/kitconcept.png
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


Code
----

Code Repository: https://github.com/kitconcept/{{cookiecutter.project_slug}}
Continous Integration: https://jenkins.kitconcept.io/job/kitconcept/job/{{cookiecutter.project_slug}}/


Project Management
------------------

Trello: https://trello.com/...
Harvest: https://kitconcept.harvestapp.com/projects/...


Server
------

Live: www.example.com
Staging: {{cookiecutter.project_slug}}.kitconcept.io (Deploy automatically from master branch)

