#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyquery
Version  : 1.4.0
Release  : 36
URL      : https://pypi.python.org/packages/e4/46/596311bb390c902b61499ff9fd5a355cdf85c8455737cb0f08c6c2c13e22/pyquery-1.4.0.tar.gz
Source0  : https://pypi.python.org/packages/e4/46/596311bb390c902b61499ff9fd5a355cdf85c8455737cb0f08c6c2c13e22/pyquery-1.4.0.tar.gz
Summary  : A jquery-like library for python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pyquery-python3
Requires: pyquery-python
Requires: cssselect
Requires: lxml
BuildRequires : PasteDeploy
BuildRequires : WSGIProxy2
BuildRequires : WebOb
BuildRequires : WebTest
BuildRequires : beautifulsoup4
BuildRequires : coverage
BuildRequires : cssselect
BuildRequires : lxml
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyquery

BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : waitress

%description
import os
from webtest import http
from webtest.debugapp import debug_app
try:
from urllib import urlopen
except ImportError:
from urllib.request import urlopen

%package python
Summary: python components for the pyquery package.
Group: Default
Requires: pyquery-python3

%description python
python components for the pyquery package.


%package python3
Summary: python3 components for the pyquery package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pyquery package.


%prep
%setup -q -n pyquery-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526262659
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
nosetests || :
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
