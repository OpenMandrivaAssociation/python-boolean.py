Name:		python-boolean.py
Version:	5.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/b/boolean.py/boolean_py-%{version}.tar.gz
Summary:	Define boolean algebras, create and parse boolean expressions and create custom boolean DSL.
URL:		https://pypi.org/project/boolean.py/
License:	BSD-2-Clause
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Define boolean algebras, create and parse boolean expressions and create custom boolean DSL.

%files
%{py_sitedir}/boolean
%{py_sitedir}/boolean.py-*.*-info
