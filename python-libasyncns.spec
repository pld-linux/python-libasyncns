%define 	module	libasyncns
Summary:	A python binding for the libasyncns asynchronous name service query library
Name:		python-%{module}
Version:	0.7.1
Release:	2
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://launchpadlibrarian.net/21625760/libasyncns-python-%{version}.tar.bz2
# Source0-md5:	99c6595915efaf2309d52bed3c17f13d
URL:		https://launchpad.net/libasyncns-python
BuildRequires:	libasyncns-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libasyncns-python is a python binding for the libasyncns asynchronous
name service query library.

%description -l pl.UTF-8

%prep
%setup -q -n %{module}-python-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/libasyncns-*.egg-info
