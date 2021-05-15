%global appname wloc

%global appsum Simple Wi-Fi geolocation library and tool
%global appdesc Simple Wi-Fi geolocation library and tool by EasyCoding Team

Name: python-%{appname}
Version: 0.5.0
Release: 1%{?dist}

License: GPLv3+ and MIT
Summary: %{appsum}
URL: https://github.com/xvitaly/%{appname}
Source0: %{url}/archive/v%{version}/%{appname}-%{version}.tar.gz

BuildRequires: python3dist(python-networkmanager)
BuildRequires: python3dist(requests)
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: doxygen

BuildArch: noarch

%description
%{appdesc}.

%package -n python3-%{appname}
Summary: %{appsum}
Requires: python3dist(python-networkmanager)
%{?python_provide:%python_provide python3-%{appname}}

%description -n python3-%{appname}
%{appdesc}.

%prep
%autosetup -n %{appname}-%{version} -p1

%build
doxygen
%py3_build

%install
%py3_install

%files -n python3-%{appname}
%doc docs/*
%license COPYING licenses/*
%{_bindir}/%{appname}
%{python3_sitelib}/%{appname}/
%{python3_sitelib}/%{appname}-*.egg-info/

%changelog
* Sat May 15 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.0-1
- Updated to version 0.5.0.
