=============================
oneAPI Specification Web Site
=============================

.. image:: https://github.com/uxlfoundation/oneapi-spec-site/actions/workflows/checks.yaml/badge.svg
   :target: https://github.com/uxlfoundation/oneapi-spec-site/actions/workflows/checks.yaml

.. image:: https://github.com/uxlfoundation/oneapi-spec-site/actions/workflows/publish.yaml/badge.svg
   :target: https://github.com/uxlfoundation/oneapi-spec-site/actions/workflows/publish.yaml

.. image:: https://api.scorecard.dev/projects/github.com/uxlfoundation/oneapi-spec-site/badge
   :target: https://scorecard.dev/viewer/?uri=github.com/uxlfoundation/oneapi-spec-site

This repository contains the source files for the oneAPI Specification web
site.

Adding a New Release
====================

To add a new release to the site, follow these steps:

* Create a release in the `oneAPI Specification`_ repository. Attach a build of
  the spec (html & PDF) to the release. Follow the naming convention and
  contents for previous releases.
* Update `site.yaml`_ to include the URL for the release. Do not forget to
  update the ``latest`` key.
* Update releases page in `src/index.rst`_. Add a new section for the release
  with a link to the release notes and the spec.
* Submit a PR with the changes. As part of the checks, the site will be built
  and deployed for preview. Submit the PR from a branch in this repo, not a
  fork. Preview requires access to GitHub secrets that are not available in a
  fork. Look in the log for the Publish job to find the URL of the preview. It
  will look like this::

   Website draft URL: https://662cecf4606617cb73f85378--oneapi-spec.netlify.app

* If everything looks good, merge the PR. To deploy to production, manually
  trigger the publish workflow by clicking on the "Run workflow" button in the
  `GitHub Actions tab`_.

Site Layout
===========

The site layout is determined by the `site.yaml`_ file. A nested set of
directories is described by a nested set of dictionaries. When a key is not a
dictionary, it is assumed to be a URL for a release.

Web Site Hosting
================

We are using Netlify because GitHub pages cannot handle sites > 1 Gbyte. Robert
has the Netlify account. If you want to do a manual deploy (development or
production), follow the procedure in `.github/workflows/publish.yaml`_. You
will need to provide a token::

   export NETLIFY_AUTH_TOKEN=your_token

Get a token from Robert if you need to deploy to production. Otherwise, create
your own site under your own account in Netlify.

.. _`src/index.rst`: src/index.rst
.. _`site.yaml`: site.yaml
.. _GitHub Actions tab: https://github.com/uxlfoundation/oneapi-spec-site/actions/workflows/publish.yaml
.. _oneAPI Specification: https://github.com/uxlfoundation/oneAPI-spec
.. _`.github/workflows/publish.yaml`: .github/workflows/publish.yaml
