%global appname wloc

%global appsum Simple Wi-Fi geolocation library and tool
%global appdesc Simple Wi-Fi geolocation library and tool by EasyCoding Team

Name: python-%{appname}
Version: 0.4.0
Release: 1%{?dist}

BuildArch: noarch
Summary: %{appsum}
License: GPLv3+
URL: https://github.com/xvitaly/%{appname}
Source0: %{url}/archive/%{version}/%{appname}-%{version}.tar.gz

BuildRequires: python3dist(python-networkmanager)
BuildRequires: python3dist(requests)
BuildRequires: python3-devel
BuildRequires: doxygen

%description
%{appdesc}.

%package -n python3-%{appname}
Summary: %{appsum}
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
%license COPYING
%doc README.md docs/*.md docs/html
%{_bindir}/%{appname}
%{python3_sitelib}/%{appname}
%{python3_sitelib}/%{appname}-*.egg-info

%changelog
* Sat Dec 14 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.0-1
- Updated to version 0.4.0.
