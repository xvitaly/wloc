%global appname wloc

%global appsum Simple Wi-Fi geolocation library and tool
%global appdesc Simple Wi-Fi geolocation library and tool by EasyCoding Team

Name: python-%{appname}
Version: 0.3
Release: 1%{?dist}
Summary: %{appsum}

License: GPLv3+
URL: https://github.com/xvitaly/%{appname}
Source0: %{url}/archive/v%{version}.tar.gz#/%{appname}-%{version}.tar.gz
Patch0: %{appname}-api-keys.patch
BuildArch: noarch

BuildRequires: python2-devel
BuildRequires: python3-devel
BuildRequires: python2-networkmanager
BuildRequires: python3-networkmanager
BuildRequires: python2dist(requests)
BuildRequires: python3dist(requests)

%description
%{appdesc}.

%package -n python2-%{appname}
Summary: %{appsum}
Requires: python2-networkmanager
Requires: python2dist(requests)
%{?python_provide:%python_provide python2-%{appname}}

%description -n python2-%{appname}
%{appdesc}.

%package -n python3-%{appname}
Summary: %{appsum}
Requires: python3-networkmanager
Requires: python3dist(requests)
%{?python_provide:%python_provide python3-%{appname}}

%description -n python3-%{appname}
%{appdesc}.

%prep
%autosetup -n %{appname}-%{version} -p1

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{appname}
%license COPYING
%doc README.md
%{python2_sitelib}/*

%files -n python3-%{appname}
%license COPYING
%doc README.md
%{_bindir}/%{appname}
%{python3_sitelib}/*

%changelog
* Fri Feb 23 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3-1
- Initial SPEC release.
