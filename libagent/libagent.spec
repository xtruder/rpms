# Created by pyp2rpm-3.3.8
%global pypi_name libagent
%global pypi_version 0.14.5

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Using hardware wallets as SSH/GPG agent

License:        None
URL:            http://github.com/romanz/trezor-agent
Source0:        %{pypi_source}
Patch0:         setup-remove-unneeded-deps.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(bech32) >= 1.2
Requires:       python3dist(configargparse) >= 0.12.1
Requires:       python3dist(cryptography) >= 3.4.6
Requires:       python3dist(docutils) >= 0.14
Requires:       python3dist(ecdsa) >= 0.13
Requires:       python3dist(mnemonic) >= 0.18
Requires:       python3dist(pynacl) >= 1.4
Requires:       python3dist(python-daemon) >= 2.1.2
Requires:       python3dist(python-daemon) >= 2.3
Requires:       python3dist(semver) >= 2.2
Requires:       python3dist(unidecode) >= 0.4.20
Requires:       python3dist(wheel) >= 0.32.3
%description -n python3-%{pypi_name}



%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Wed Oct 05 2022 Jaka Hudoklin <jaka@x-truder.net> - 0.14.5-1
- Initial package.
