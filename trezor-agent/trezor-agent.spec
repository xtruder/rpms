%undefine _disable_source_fetch

# Created by pyp2rpm-3.3.8
%global pypi_name trezor_agent
%global pypi_version 0.12.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        3%{?dist}
Summary:        Using Trezor as hardware SSH/GPG agent
License:        None

URL:            http://github.com/romanz/trezor-agent
Source0:        %{pypi_source}
Source1:        trezor-gpg-agent.service
Source2:        trezor-gpg-agent.socket
Patch0:         setup-remove-unneeded-deps.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  systemd-rpm-macros

%description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(libagent) >= 0.14
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}



%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
install -D -m 644 %SOURCE1 %{buildroot}%{_userunitdir}/trezor-gpg-agent.service
install -D -m 644 %SOURCE2 %{buildroot}%{_userunitdir}/trezor-gpg-agent.socket

%files -n python3-%{pypi_name}
%{_bindir}/trezor-agent
%{_bindir}/trezor-gpg
%{_bindir}/trezor-gpg-agent
%{_bindir}/trezor_agent.py
%{_bindir}/age-plugin-trezor
%{_bindir}/trezor-signify
%ghost %{python3_sitelib}/trezor_agent.py
%ghost %{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info
%{_userunitdir}/trezor-gpg-agent.service
%{_userunitdir}/trezor-gpg-agent.socket

%changelog
* Tue May 24 2022 vscode - 0.11.0-1
- Initial package.
