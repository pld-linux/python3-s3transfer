#
# Conditional build:
%bcond_without	tests	# unit/functional tests

Summary:	Amazon S3 Transfer Manager
Summary(pl.UTF-8):	Zarządca transferu danych Amazon S3
Name:		python3-s3transfer
Version:	0.10.2
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/s3transfer/
Source0:	https://files.pythonhosted.org/packages/source/s/s3transfer/s3transfer-%{version}.tar.gz
# Source0-md5:	891737ce35aeb23b02a47a72c7f9b639
URL:		https://pypi.org/project/s3transfer/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-botocore >= 1.12.36
BuildRequires:	python3-botocore < 2
BuildRequires:	python3-nose >= 1.3.3
BuildRequires:	python3-six
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
S3transfer is a Python library for managing Amazon S3 transfers.

%description -l pl.UTF-8
S3transfer to pythonowa biblioteka do zarządzania przesyłami danych
Amazon S3.

%prep
%setup -q -n s3transfer-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s tests/unit
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/s3transfer
%{py3_sitescriptdir}/s3transfer-%{version}-py*.egg-info
