%global         github_name linux-gui
%global         srcname linux_gui

Name:           protonvpn-gui
Version:        2.1.1
Release:        3%{?dist}
Summary:        Linux GUI for ProtonVPN, written in Python.

License:        GPLv3
%undefine       _disable_source_fetch
URL:            https://github.com/ProtonVPN/%{github_name}
Source0:         %{url}/archive/v%{version}.tar.gz#/%{github_name}-%{version}.tar.gz
Patch0:         relax-required-versions.patch
Source1:        protonvpn-gui.desktop
Source2:        protonvpn-tray.desktop
%define         SHA256SUM0 de7f6501bd051d3eeda731edf5ed932dd0e23555f5f39ec6ff2b6ce99de83338

BuildArch:      noarch
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ImageMagick

Requires:       openvpn
Requires:       hicolor-icon-theme
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

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2} 

mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps

convert -scale 32 linux_gui/resources/img/logo/protonvpn_logo.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

for i in 16 32 48
do
   convert -scale $i linux_gui/resources/img/logo/protonvpn_logo.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

%post
update-desktop-database /usr/share/applications &> /dev/null || :

%postun
update-desktop-database /usr/share/applications &> /dev/null || :


%files
%license LICENSE
%doc README.md
%{python3_sitelib}/protonvpn_gui-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/applications/*.desktop
%{_bindir}/protonvpn-gui
%{_bindir}/protonvpn-tray


%changelog
