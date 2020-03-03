#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyquery
Version  : 1.4.1
Release  : 50
URL      : https://files.pythonhosted.org/packages/6b/94/4663206f709ac32446e995227cc5be34d5e2aa74ba8f92b8083c2740d3d7/pyquery-1.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/6b/94/4663206f709ac32446e995227cc5be34d5e2aa74ba8f92b8083c2740d3d7/pyquery-1.4.1.tar.gz
Summary  : A jquery-like library for python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pyquery-license = %{version}-%{release}
Requires: pyquery-python = %{version}-%{release}
Requires: pyquery-python3 = %{version}-%{release}
Requires: cssselect
Requires: lxml
BuildRequires : PasteDeploy
BuildRequires : WSGIProxy2
BuildRequires : WebOb
BuildRequires : WebTest
BuildRequires : beautifulsoup4
BuildRequires : buildreq-distutils3
BuildRequires : coverage
BuildRequires : cssselect
BuildRequires : lxml
BuildRequires : nose
BuildRequires : pyquery
BuildRequires : python-mock
BuildRequires : six
BuildRequires : waitress

%description
pyquery: a jquery-like library for python
=========================================

.. image:: https://travis-ci.org/gawel/pyquery.svg
   :alt: Build Status
   :target: https://travis-ci.org/gawel/pyquery

pyquery allows you to make jquery queries on xml documents.
The API is as much as possible the similar to jquery. pyquery uses lxml for fast
xml and html manipulation.

This is not (or at least not yet) a library to produce or interact with
javascript code. I just liked the jquery API and I missed it in python so I
told myself "Hey let's make jquery in python". This is the result.

The `project`_ is being actively developped on a git repository on Github. I
have the policy of giving push access to anyone who wants it and then to review
what they do. So if you want to contribute just email me.

Please report bugs on the `github
<https://github.com/gawel/pyquery/issues>`_ issue
tracker.

.. _deliverance: http://www.gawel.org/weblog/en/2008/12/skinning-with-pyquery-and-deliverance
.. _project: https://github.com/gawel/pyquery/

I've spent hours maintaining this software, with love.
Please consider tiping if you like it:

BTC: 1PruQAwByDndFZ7vTeJhyWefAghaZx9RZg

ETH: 0xb6418036d8E06c60C4D91c17d72Df6e1e5b15CE6

LTC: LY6CdZcDbxnBX9GFBJ45TqVj8NykBBqsmT


Quickstart
==========

You can use the PyQuery class to load an xml document from a string, a lxml
document, from a file or from an url::

    >>> from pyquery import PyQuery as pq
    >>> from lxml import etree
    >>> import urllib
    >>> d = pq("<html></html>")
    >>> d = pq(etree.fromstring("<html></html>"))
    >>> d = pq(url=your_url)
    >>> d = pq(url=your_url,
    ...        opener=lambda url, **kw: urlopen(url).read())
    >>> d = pq(filename=path_to_html_file)

Now d is like the $ in jquery::

    >>> d("#hello")
    [<p#hello.hello>]
    >>> p = d("#hello")
    >>> print(p.html())
    Hello world !
    >>> p.html("you know <a href='http://python.org/'>Python</a> rocks")
    [<p#hello.hello>]
    >>> print(p.html())
    you know <a href="http://python.org/">Python</a> rocks
    >>> print(p.text())
    you know Python rocks

You can use some of the pseudo classes that are available in jQuery but that
are not standard in css such as :first :last :even :odd :eq :lt :gt :checked
:selected :file::

    >>> d('p:first')
    [<p#hello.hello>]



See http://pyquery.rtfd.org/ for the full documentation

News
====

1.4.1 (2019-10-26)
------------------

- This is the latest release with py2 support

- Remove py33, py34 support

- web scraping improvements: default timeout and session support

- Add API methods to serialize form-related elements according to spec

- Include HTML markup when querying textarea text/value


1.4.0 (2018-01-11)
------------------

- Refactoring of `.text()` to match firefox behavior.


1.3.0 (2017-10-21)
------------------

- Remove some unmaintained modules: ``pyquery.ajax`` and ``pyquery.rules``

- Code cleanup. No longer use ugly hacks required by python2.6/python3.2.

- Run tests with python3.6 on CI

- Add a ``method`` argument to ``.outer_html()``


1.2.17 (2016-10-14)
-------------------

- ``PyQuery('<input value="">').val()`` is ``''``
- ``PyQuery('<input>').val()`` is ``''``


1.2.16 (2016-10-14)
-------------------

- ``.attr('value', '')`` no longer removes the ``value`` attribute

- ``<input type="checkbox">`` without ``value="..."`` have a ``.val()`` of
  ``'on'``

- ``<input type="radio">`` without ``value="..."`` have a ``.val()`` of
  ``'on'``

- ``<select>`` without ``<option selected>`` have the value of their first
  ``<option>`` (or ``None`` if there are no options)


1.2.15 (2016-10-11)
-------------------

- .val() should never raise

- drop py26 support

- improve .extend() by returning self


1.2.14 (2016-10-10)
-------------------

- fix val() for <textarea> and <select>, to match jQuery behavior


1.2.13 (2016-04-12)
-------------------

- Note explicit support for Python 3.5

1.2.12 (2016-04-12)
-------------------

- make_links_absolute now take care of whitespaces

- added pseudo selector :has()

- add cookies arguments as allowed arguments for requests


1.2.11 (2016-02-02)
-------------------

- Preserve namespaces attribute on PyQuery copies.

- Do not raise an error when the http response code is 2XX

1.2.10 (2016-01-05)
-------------------

- Fixed #118: implemented usage ``lxml.etree.tostring`` within ``outer_html`` method

- Fixed #117: Raise HTTP Error if HTTP status code is not equal to 200

- Fixed #112: make_links_absolute does not apply to form actions

- Fixed #98: contains act like jQuery


1.2.9 (2014-08-22)
------------------

- Support for keyword arguments in PyQuery custom functions

- Fixed #78: items must take care or the parent

- Fixed #65 PyQuery.make_links_absolute() no longer creates 'href' attribute
  when it isn't there

- Fixed #19. ``is_()`` was broken.

- Fixed #9. ``.replaceWith(PyQuery element)`` raises error

- Remove official python3.2 support (mostly because of 3rd party semi-deps)


1.2.8 (2013-12-21)
------------------

- Fixed #22: Open by filename fails when file contains invalid xml

- Bug fix in .remove_class()


1.2.7 (2013-12-21)
------------------

- Use pep8 name for methods but keep an alias for camel case method.
  Eg: remove_attr and removeAttr works
  Fix #57

- .text() now return an empty string instead of None if there is no text node.
  Fix #45

- Fixed #23: removeClass adds class attribute to elements which previously
  lacked one


1.2.6 (2013-10-11)
------------------

- README_fixt.py was not include in the release. Fix #54.


1.2.5 (2013-10-10)
------------------

- cssselect compat. See https://github.com/SimonSapin/cssselect/pull/22

- tests improvments. no longer require a eth connection.

- fix #55

1.2.4
-----

- Moved to github. So a few files are renamed from .txt to .rst

- Added .xhtml_to_html() and .remove_namespaces()

- Use requests to fetch urls (if available)

- Use restkit's proxy instead of Paste (which will die with py3)

- Allow to open https urls

- python2.5 is no longer supported (may work, but tests are broken)

1.2.3
-----

- Allow to pass this in .filter() callback

- Add .contents() .items()

- Add tox.ini

- Bug fixes: fix #35 #55 #64 #66

1.2.2
-----

- Fix cssselectpatch to match the newer implementation of cssselect. Fixes issue #62, #52 and #59 (Haoyu Bai)

- Fix issue #37 (Caleb Burns)

1.2.1
-----

- Allow to use a custom css translator.

- Fix issue 44: case problem with xml documents

1.2
---

- PyQuery now uses `cssselect <http://pypi.python.org/pypi/cssselect>`_. See issue 43.

- Fix issue 40: forward .html() extra arguments to ``lxml.etree.tostring``

1.1.1
-----

- Minor release. Include test file so you can run tests from the tarball.


1.1
---

- fix issues 30, 31, 32 - py3 improvements / webob 1.2+ support


1.0
---

- fix issues 24

0.7
---

- Python 3 compatible

- Add __unicode__ method

- Add root and encoding attribute

- fix issues 19, 20, 22, 23 

0.6.1
------

- Move README.txt at package root

- Add CHANGES.txt and add it to long_description

0.6
----

- Added PyQuery.outerHtml

- Added PyQuery.fn

- Added PyQuery.map

- Change PyQuery.each behavior to reflect jQuery api

%package license
Summary: license components for the pyquery package.
Group: Default

%description license
license components for the pyquery package.


%package python
Summary: python components for the pyquery package.
Group: Default
Requires: pyquery-python3 = %{version}-%{release}

%description python
python components for the pyquery package.


%package python3
Summary: python3 components for the pyquery package.
Group: Default
Requires: python3-core
Provides: pypi(pyquery)

%description python3
python3 components for the pyquery package.


%prep
%setup -q -n pyquery-1.4.1
cd %{_builddir}/pyquery-1.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583208857
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
nosetests || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyquery
cp %{_builddir}/pyquery-1.4.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/pyquery/0c3c925b54baa8fb36678f14b695f694affdf611
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyquery/0c3c925b54baa8fb36678f14b695f694affdf611

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
