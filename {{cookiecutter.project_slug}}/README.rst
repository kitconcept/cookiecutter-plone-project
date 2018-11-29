.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
DPG - Deutsche Physikalische Gesellschaft (www.dpg-physik.de)
==============================================================================

.. image:: https://raw.githubusercontent.com/kitconcept/dpg.core/master/kitconcept.png
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

Code Repository: https://github.com/kitconcept/dpg
Continous Integration: https://jenkins.kitconcept.io/job/kitconcept/job/dpg/


Project Management
------------------

Trello: https://trello.com/b/FXLiZirx/dpg-relaunch-2018
Harvest: https://kitconcept.harvestapp.com/projects/17649167


Server
------

Live: www.dpg-physik.de
Staging: dpg.kitconcept.io (Deploy automatically from master branch)

