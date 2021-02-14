#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Amazon S3 Transfer Manager
Summary(pl.UTF-8):	Zarządca transferu danych Amazon S3
Name:		python-s3transfer
Version:	0.3.4
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/s3transfer/
Source0:	https://files.pythonhosted.org/packages/source/s/s3transfer/s3transfer-%{version}.tar.gz
# Source0-md5:	b0145fc2087107262b6c4d0f077ad3e2
Patch0:		%{name}-mock.patch
Patch1:		%{name}-tests.patch
URL:		https://pypi.org/project/s3transfer/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-botocore >= 1.12.36
BuildRequires:	python-futures >= 2.2.0
BuildRequires:	python-mock >= 1.3.0
BuildRequires:	python-nose >= 1.3.3
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-botocore >= 1.12.36
BuildRequires:	python3-nose >= 1.3.3
BuildRequires:	python3-six
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
S3transfer is a Python library for managing Amazon S3 transfers.

%description -l pl.UTF-8
S3transfer to pythonowa biblioteka do zarządzania przesyłami danych
Amazon S3.

%package -n python3-s3transfer
Summary:	Amazon S3 Transfer Manager
Summary(pl.UTF-8):	Zarządca transferu danych Amazon S3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-s3transfer
S3transfer is a Python library for managing Amazon S3 transfers.

%description -n python3-s3transfer -l pl.UTF-8
S3transfer to pythonowa biblioteka do zarządzania przesyłami danych
Amazon S3.

%prep
%setup -q -n s3transfer-%{version}
%patch0 -p1
%patch1 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover -s tests/unit
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s tests/unit
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/s3transfer
%{py_sitescriptdir}/s3transfer-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-s3transfer
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/s3transfer
%{py3_sitescriptdir}/s3transfer-%{version}-py*.egg-info
%endif
