%define module phx-class-registry
%define oname phx_class_registry

Name:		python-phx-class-registry
Version:	5.2.1
Release:	1
Summary:	Factory+Registry pattern for Python classes
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/phx-class-registry/
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
Factory+Registry pattern for Python classes

%files
%{py_sitedir}/class_registry
%{py_sitedir}/%{oname}-%{version}.dist-info
