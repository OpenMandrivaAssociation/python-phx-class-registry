Name:		python-phx-class-registry
Version:	5.1.1
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/p/phx-class-registry/phx_class_registry-%{version}.tar.gz
Summary:	Factory+Registry pattern for Python classes
URL:		https://pypi.org/project/phx-class-registry/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(poetry-core)
BuildArch:	noarch

%description
Factory+Registry pattern for Python classes

%files
%{py_sitedir}/class_registry
%{py_sitedir}/phx_class_registry-*.*-info
