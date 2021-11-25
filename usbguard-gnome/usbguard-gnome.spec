%global gschemadir %{_datadir}/glib-2.0/schemas
%global gitname    usbguard-gnome
%global giturl     https://github.com/6E006B/%{gitname}
%global gitcommit  ce90c7a8db4b1429adc772816e23520818c865c4
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global gitsnapinfo .20201027git%{gitshortcommit}

Name:       usbguard-gnome
Summary:    USBGuard configuration interface for gnome
Version:    0
Release:    4%{?gitsnapinfo}%{?dist}
License:    GPLv2+
Group:      Applications/Security
URL:        %{giturl}
%undefine   _disable_source_fetch
Source0:    %{url}/archive/%{gitcommit}.tar.gz#/%{name}-%{release}.tar.gz
Source1:    usbguard.desktop
Source2:    usbguard_applet.desktop
Source3:    usbguard-icon.svg
%define     SHA256SUM0 4034d99753f7a5aa5a048b4dc0db02f97a401579294cdf99619e4d1ef9f3a800

BuildArch:      noarch

BuildRequires: desktop-file-utils
BuildRequires: python3
Requires: usbguard-dbus
Requires: python3
Requires: python3-gobject
Requires: python3-dbus
Requires: python3-pyparsing
Requires: python3-cairo
Requires: gtk3
Requires: pango
Requires: glib2 >= 2.24
Requires: hicolor-icon-theme

%description
USBGuard configuration interface for gnome

%prep
echo "%SHA256SUM0  %SOURCE0" | sha256sum -c -
%autosetup -n %{gitname}-%{gitcommit} -p 1


%build
python3 -m compileall -b src


%install
install -d -D -m0755 %{buildroot}%{_libexecdir}/%{name}/
install -m0755 src/*.pyc %{buildroot}%{_libexecdir}/%{name}/

install -d -D -m0755 %{buildroot}%{gschemadir}
install -m0644 -T src/org.gnome.usbguard.gschema.xml %{buildroot}%{gschemadir}/org.gnome.usbguard.gschema.xml

install -d -D -m0755 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -m0644 -T %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}


%post
update-desktop-database /usr/share/applications &> /dev/null || :


%postun
/usr/bin/update-desktop-database &> /dev/null || :


%files
%doc README.md
%{_datadir}/applications/*.desktop
%{_libexecdir}/%{name}/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{gschemadir}/*gschema.xml

%changelog
