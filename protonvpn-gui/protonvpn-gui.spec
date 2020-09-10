%global         github_name linux-gui
%global         srcname linux_gui

Name:           protonvpn-gui
Version:        2.1.1
Release:        2%{?dist}
Summary:        Linux GUI for ProtonVPN, written in Python.

License:        GPLv3
%undefine       _disable_source_fetch
URL:            https://github.com/ProtonVPN/%{github_name}
Source:         %{url}/archive/v%{version}.tar.gz#/%{github_name}-%{version}.tar.gz
Patch0:         relax-required-versions.patch
%define         SHA256SUM0 de7f6501bd051d3eeda731edf5ed932dd0e23555f5f39ec6ff2b6ce99de83338

BuildArch:      noarch
BuildRequires:  python3
BuildRequires:  python3-devel

Requires:       openvpn
%if 0%{?fedora} || 0%{?.el8}
Recommends:     dialog
Recommends:     NetworkManager-openvpn
Suggests:       NetworkManager-openvpn-gnome
%else
Requires:       dialog
%endif

%description
Linux GUI for ProtonVPN, written in Python


%prep
echo "%SHA256SUM0  %SOURCE0" | sha256sum -c 
%autosetup -n %{github_name}-%{version}

%build
%py3_build

%install
%py3_install


%files
%license LICENSE
%doc README.md
%{python3_sitelib}/protonvpn_gui-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/protonvpn-gui
%{_bindir}/protonvpn-tray


%changelog
