%global extuuid    nightthemeswitcher@romainvigier.fr
%global extdir     %{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir %{_datadir}/glib-2.0/schemas

Name:           gnome-shell-extension-night-theme-switcher
Version:        v74
Release:        2%{dist}
Summary:        Night Theme Switcher GNOME Shell extension

License:        GPLv3+
URL:            https://nightthemeswitcher.romainvigier.fr/
%undefine       _disable_source_fetch
Source0:        https://extensions.gnome.org/extension-data/nightthemeswitcherromainvigier.fr.v74.shell-extension.zip#/%{name}-%{version}.zip
%define         SHA256SUM0 efcb981580ec3853386bb5ef3acf38dd19051ea1f6717ac5b07b84bebc1fbd76

BuildArch:      noarch

BuildRequires:  %{_bindir}/glib-compile-schemas

Requires:       gnome-shell-extension-common
Requires:       gnome-shell >= 4.44.0


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


%files
%{extdir}


%changelog
