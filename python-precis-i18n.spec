%define pname precis_i18n

Name: python-%(echo %{pname} | tr 'A-Z' 'a-z')
Version: 1.0.1
Release: 1%{?dist}
Summary: Internationalized Usernames and Passwords
Group: Development/Libraries
License: MIT
URL: https://github.com/byllyfish/%{pname}
Source: https://github.com/byllyfish/%{pname}/archive/v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-buildroot
BuildArch: noarch


%description
This module implements the PRECIS Framework as described in:

PRECIS Framework: Preparation, Enforcement, and Comparison of Internationalized
  Strings in Application Protocols (RFC 8264)
Preparation, Enforcement, and Comparison of Internationalized Strings
  Representing Usernames and Passwords (RFC 8265)
Preparation, Enforcement, and Comparison of Internationalized Strings
  Representing Nicknames (RFC 8266)


%package -n python2-%(echo %{pname} | tr 'A-Z' 'a-z')
Summary: Internationalized Usernames and Passwords
BuildRequires: python2-devel
BuildRequires: python2-setuptools

%description -n python2-%(echo %{pname} | tr 'A-Z' 'a-z')
This module implements the PRECIS Framework as described in:

PRECIS Framework: Preparation, Enforcement, and Comparison of Internationalized
  Strings in Application Protocols (RFC 8264)
Preparation, Enforcement, and Comparison of Internationalized Strings
  Representing Usernames and Passwords (RFC 8265)
Preparation, Enforcement, and Comparison of Internationalized Strings
  Representing Nicknames (RFC 8266)

Python 2 version.


%package -n python3-%(echo %{pname} | tr 'A-Z' 'a-z')
Summary: Internationalized Usernames and Passwords
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description -n python3-%(echo %{pname} | tr 'A-Z' 'a-z')
This module implements the PRECIS Framework as described in:

PRECIS Framework: Preparation, Enforcement, and Comparison of Internationalized
  Strings in Application Protocols (RFC 8264)
Preparation, Enforcement, and Comparison of Internationalized Strings
  Representing Usernames and Passwords (RFC 8265)
Preparation, Enforcement, and Comparison of Internationalized Strings
  Representing Nicknames (RFC 8266)

Python 3 version.


%prep
%setup -q -n %{pname}-%{version}


%build
%py2_build
%py3_build


%install
[ '%{buildroot}' != '/' ] && rm -rf %{buildroot}
%py2_install
%py3_install


%clean
[ '%{buildroot}' != '/' ] && rm -rf %{buildroot}


%files -n python2-%(echo %{pname} | tr 'A-Z' 'a-z')
%defattr(-,root,root)
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%{python2_sitelib}/%{pname}/
%{python2_sitelib}/*.egg-info/


%files -n python3-%(echo %{pname} | tr 'A-Z' 'a-z')
%defattr(-,root,root)
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%{python3_sitelib}/%{pname}/
%{python3_sitelib}/*.egg-info/


%changelog
* Tue Nov  5 2019 Philippe Kueck <projects@unixadm.org> - 1.0.1-1
- new upstream version

* Fri Mar  9 2018 Philippe Kueck <projects@unixadm.org> - 1.0-1
- initial packaging
