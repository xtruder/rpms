%global extuuid    nightthemeswitcher@romainvigier.fr
%global extdir     %{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir %{_datadir}/glib-2.0/schemas

Name:           gnome-shell-extension-night-theme-switcher
Version:        75
Release:        0%{dist}
Summary:        Night Theme Switcher GNOME Shell extension

License:        GPLv3+
URL:            https://nightthemeswitcher.romainvigier.fr/
%undefine       _disable_source_fetch
Source0:        https://extensions.gnome.org/extension-data/nightthemeswitcherromainvigier.fr.v%{version}.shell-extension.zip#/%{name}-%{version}.zip
%define         SHA256SUM0 df9080db76ad8d8b6bee0b0e65fab5419376e740ee78d521b1aad016a60dc661

BuildArch:      noarch

BuildRequires:  %{_bindir}/glib-compile-schemas

Requires:       gnome-shell-extension-common
Requires:       gnome-shell >= 4.45.0


%description
Automatically toggle your light and dark GTK, GNOME Shell, icon and
cursor themes variants, switch backgrounds and run custom commands at sunset and sunrise.


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
rm -fr %{buildroot}%{extdir}/schemas


%files
%{extdir}
%{gschemadir}/*gschema.xml


%changelog
