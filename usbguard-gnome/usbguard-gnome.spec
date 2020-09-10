%global gschemadir %{_datadir}/glib-2.0/schemas

Name:			usbguard-gnome
Summary:		USBGuard configuration interface for gnome
Version:		0.1.1
Release:		1%{?dist}
License:		GPLv2+
Group:			Applications/Security
URL:			https://github.com/drahnr/usbguard-gnome
%undefine		_disable_source_fetch
Source0:		%{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%define			SHA256SUM0 aa704d9fd30a7110fc209dd5cb1258f0b72ed3a9e3e18c7ef377068891a3fc16

BuildArch:      noarch

BuildRequires: desktop-file-utils
Requires: python3
Requires: python3-gobject
Requires: python3-dbus
Requires: gtksourceview3
Requires: gtk3
Requires: glib2 >= 2.24

%description
USBGuard configuration interface for gnome

%prep
echo "%SHA256SUM0  %SOURCE0" | sha256sum -c -
%setup -q -n %{name}-%{version}

%build

%install

install -d -D -m0755 %{buildroot}%{_datadir}/glib-2.0/schemas/
install -m0644 -T src/org.gnome.usbguard.gschema.xml %{buildroot}%{gschemadir}/org.gnome.usbguard.gschema.xml

install -d -D -m0755 %{buildroot}%{_datadir}/icons/hicolor/scalable/
install -m0644 -T src/*.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/%{name}.svg
desktop-file-install --dir=%{buildroot}%{_datadir}/applications usbguard*.desktop

install -d -D -m0755 %{buildroot}%{_datadir}/%{name}/
install -m0755 src/*.py %{buildroot}%{_datadir}/%{name}/


%post
/bin/touch --no-create %{_datadir}/icons/hicolor/scalable &>/dev/null || :
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
    /bin/touch --no-create %{_datadir}/icons/hicolor/scalable &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor/scalable &>/dev/null || :
fi
/usr/bin/update-desktop-database &> /dev/null || :


%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor/scalable &>/dev/null || :


%files
%doc README.md
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/*
%{_datadir}/icons/hicolor/scalable/*
%{gschemadir}/*gschema.xml

%changelog
* Thu Feb 20 2020 Bernhard Schuster <bernhard@ahoi.io> 0.1.0-1
 - Initial release