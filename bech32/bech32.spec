# Created by pyp2rpm-3.3.8
%global pypi_name bech32
%global pypi_version 1.2.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Reference implementation for Bech32 and segwit addresses

License:        MIT
URL:            https://github.com/fiatjaf/bech32
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Since this implementation wasn't in a place that was easy to use for Python
programmers I took it from from and published [on GitHub]( and [on PyPI](
original version of this package is probably the one at but apparently Rusty
Russel commented out the 90-length limit of bech32-encoded stuff so it could be
used for Lightning invoices. Let's keep that change.Installpip install bech32

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Since this implementation wasn't in a place that was easy to use for Python
programmers I took it from from and published [on GitHub]( and [on PyPI](
original version of this package is probably the one at but apparently Rusty
Russel commented out the 90-length limit of bech32-encoded stuff so it could be
used for Lightning invoices. Let's keep that change.Installpip install bech32


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Wed Oct 05 2022 Jaka Hudoklin <jaka@x-truder.net> - 1.2.0-1
- Initial package.
