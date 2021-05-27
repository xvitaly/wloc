%global appname wloc

%global _description %{expand:
WLoc is a simple command-line Wi-Fi geolocation tool, which can be used to
locate user by using global Wi-Fi database (no GPS required).}

Name: python-%{appname}
Version: 0.5.0
Release: 1%{?dist}

License: GPLv3+ and MIT and ASL 2.0
Summary: Simple Wi-Fi geolocation library and tool
URL: https://github.com/xvitaly/%{appname}
Source0: %{url}/archive/v%{version}/%{appname}-%{version}.tar.gz

BuildRequires: doxygen
BuildRequires: python3-devel
BuildRequires: %{py3_dist setuptools}
BuildRequires: %{py3_dist requests}
BuildRequires: %{py3_dist python-networkmanager}

BuildArch: noarch

%description %_description

%package -n python3-%{appname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{appname}}

%description -n python3-%{appname} %_description

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
