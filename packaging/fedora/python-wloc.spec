%global srcname wloc

%global _description %{expand:
WLoc is a simple command-line Wi-Fi geolocation tool, which can be used to
locate user by using global Wi-Fi database (no GPS required).}

Name: python-%{srcname}
Version: 0.5.0
Release: 1%{?dist}

# Main code - GPLv3+.
# pywifi - MIT.
# Icon - Apache 2.0.
License: GPLv3+ and MIT and ASL 2.0
Summary: Simple Wi-Fi geolocation library and tool
URL: https://github.com/xvitaly/%{srcname}
Source0: %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: doxygen
BuildRequires: python3-devel
BuildRequires: %{py3_dist python-networkmanager}
BuildRequires: %{py3_dist requests}
BuildRequires: %{py3_dist setuptools}

BuildArch: noarch

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

# Buidling documentation...
doxygen

# Building manpage...
pandoc packaging/assets/manpage.md -s -t man > packaging/assets/%{name}.1

%install
%py3_install

# Installing manpage...
install -d %{buildroot}%{_mandir}/man1/
install -m 0644 -p packaging/assets/%{name}.1 %{buildroot}%{_mandir}/man1/

%files -n python3-%{srcname}
%doc docs/*
%license COPYING licenses/*
%{_bindir}/%{srcname}
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/
%{_mandir}/man1/%{name}.1*

%changelog
* Sat May 15 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.0-1
- Updated to version 0.5.0.
