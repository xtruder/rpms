%global extuuid    nightthemeswitcher@romainvigier.fr
%global extdir     %{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir %{_datadir}/glib-2.0/schemas

Name:           gnome-shell-extension-night-theme-switcher
Version:        v54
Release:        1%{dist}
Summary:        Night Theme Switcher GNOME Shell extension

License:        GPLv3+
URL:            https://nightthemeswitcher.romainvigier.fr/
%undefine       _disable_source_fetch
Source0:        https://extensions.gnome.org/extension-data/nightthemeswitcherromainvigier.fr.v54.shell-extension.zip#/%{name}-%{version}.zip
%define         SHA256SUM0 3529ac417410a64add7eba56c545c3785bbdf0b9b8ac71f074dfe521fba30912

BuildArch:      noarch

BuildRequires:  %{_bindir}/glib-compile-schemas

Requires:       gnome-shell-extension-common
Requires:       gnome-shell >= 4.41.0


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


# CentOS 7 doesn't compile gschemas automatically, Fedora does.
%if 0%{?rhel} && 0%{?rhel} <= 7
%postun
if [ $1 -eq 0 ] ; then
  %{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
fi

%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
%endif



%files
%{extdir}
%{gschemadir}/*gschema.xml


%changelog
