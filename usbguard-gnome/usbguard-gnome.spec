%{?python_disable_dependency_generator}
%global debug_package %{nil}

Name:           gnome-usbguard
Summary:        USBGuard configuration interface for gnome
Version:        0.1.2
Release:        1%{?dist}
License:        GPLv2+
Group:          Applications/Security
%undefine       _disable_source_fetch
Source0:        https://github.com/drahnr/usbguard-gnome/archive/v%{version}.tar.gz
%define         SHA256SUM0 2c9baab6ab0b0e9e57efa5b60f26046c4a7e36a1db9501d548c92bd9b7fed1b4
Url:            https://github.com/drahnr/usbguard-gnome

BuildRequires: gtk3-devel
BuildRequires: gtksourceview3-devel
BuildRequires: intltool
BuildRequires: glib2-devel
BuildRequires: desktop-file-utils
Requires: gtksourceview3
Requires: gtk3
Requires: glib2 >= 2.24
Provides: %{name} = %{version}-%{release}

%description
USBGuard configuration interface for gnome

%prep
%setup -q -n usbguard-gnome-%{version}

%build

%install

install -d -D -m0755 ${RPM_BUILD_ROOT}%{_datadir}/glib-2.0/schemas/
install -m0644 -T src/org.gnome.usbguard.gschema.xml ${RPM_BUILD_ROOT}%{_datadir}/glib-2.0/schemas/io.ahoi.%{name}.gschema.xml

install -d -D -m0755 ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/scalable/
install -m0644 -T src/*.svg ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/scalable/%{name}.svg
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications usbguard*.desktop

install -d -D -m0755 ${RPM_BUILD_ROOT}%{_datadir}/%{name}/
install -m0755 src/*.py ${RPM_BUILD_ROOT}%{_datadir}/%{name}/


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


%clean
rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root)

%doc README.md

%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/*
%{_datadir}/icons/hicolor/scalable/*
%{_datadir}/glib-2.0/schemas/io.ahoi.%{name}.gschema.xml

%changelog
* Thu Sep 10 2020 Jaka Hudoklin <jaka@x-truder.net> 0.1.2-1
 - update to 0.1.2

* Thu Feb 20 2020 Bernhard Schuster <bernhard@ahoi.io> 0.1.0-1
 - Initial release