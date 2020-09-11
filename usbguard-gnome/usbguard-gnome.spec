%global gschemadir %{_datadir}/glib-2.0/schemas
%global gitname    usbguard-gnome
%global giturl     https://github.com/6E006B/%{gitname}
%global gitcommit c9fff56bdd985c61082e829aac09601fb086f76c
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global gitsnapinfo .20190713git%{gitshortcommit}

Name:       usbguard-gnome
Summary:    USBGuard configuration interface for gnome
Version:    0
Release:    3%{?gitsnapinfo}%{?dist}
License:    GPLv2+
Group:      Applications/Security
URL:        %{giturl}
%undefine   _disable_source_fetch
Source0:    %{url}/archive/%{gitcommit}.tar.gz#/%{name}-%{release}.tar.gz
Source1:    usbguard.desktop
Source2:    usbguard_applet.desktop
Source3:    usbguard-icon.svg
Patch0:     dbus-connection-strings.patch
%define     SHA256SUM0 086f5fe65c96b165ce0ba0749e575b058fba3eb5c1109d7d4310fdd8ae518463

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

install -d -D -m0755 %{buildroot}%{_datadir}/icons/hicolor/scalable/
install -m0644 -T %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/scalable/%{name}.svg
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}


%postun
/usr/bin/update-desktop-database &> /dev/null || :


%files
%doc README.md
%{_datadir}/applications/*.desktop
%{_libexecdir}/%{name}/*
%{_datadir}/icons/hicolor/scalable/*
%{gschemadir}/*gschema.xml

%changelog
