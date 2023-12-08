%global extuuid    ddterm@amezin.github.com
%global extdir     %{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir %{_datadir}/glib-2.0/schemas

Name:           gnome-shell-extension-ddterm
Version:        v48
Release:        1%{dist}
Summary:        Another drop down terminal extension for GNOME Shell.

License:        GPLv3+
URL:            https://github.com/ddterm/gnome-shell-extension-ddterm
%undefine       _disable_source_fetch
Source0:        https://extensions.gnome.org/extension-data/ddtermamezin.github.com.%{version}.shell-extension.zip#/%{name}-%{version}.zip
%define         SHA256SUM0 f3c91163cc0b73bb32fabdebdeda350bd758350d50037746ecddf591a19e9d14

BuildArch:      noarch

BuildRequires:  %{_bindir}/glib-compile-schemas

Requires:       gnome-shell-extension-common
Requires:       gnome-shell >= 3.45.0


%description
Another drop down terminal extension for GNOME Shell. With tabs. Works on Wayland natively.


%prep
echo "%SHA256SUM0  %SOURCE0" | sha256sum -c -
%autosetup -c -n %{name}-%{version} -p 1


%build


%install
mkdir -p %{buildroot}%{extdir}
cp -pr * %{buildroot}%{extdir}

# Install schema.
mkdir -p %{buildroot}%{gschemadir}
cp -pr schemas/*gschema.xml %{buildroot}%{gschemadir}

# Cleanup unused files.
rm -r %{buildroot}%{extdir}/{LICENSE,schemas}


%files
%license LICENSE
%{extdir}
%{gschemadir}/*gschema.xml


%changelog
