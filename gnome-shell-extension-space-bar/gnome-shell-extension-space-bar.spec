%global extuuid    space-bar@luchrioh
%global extdir     %{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir %{_datadir}/glib-2.0/schemas

Name:           gnome-shell-extension-space-bar
Version:        23
Release:        0
Summary:        GNOME Shell workspace switcher extension

License:        GPLv2+
URL:            https://github.com/christopher-l/space-bar
%undefine       _disable_source_fetch
Source0:        https://extensions.gnome.org/extension-data/space-barluchrioh.v%{version}.shell-extension.zip#/%{name}-%{version}.zip
%define         SHA256SUM0 fdb942e6ca84e7875ab4e5643b1f7b941bf5ee7e25613ebb97a5d4ba3f6b50ed

BuildArch:      noarch

BuildRequires:  %{_bindir}/glib-compile-schemas

Requires:       gnome-shell-extension-common
Requires:       gnome-shell >= 4.45.0


%description
GNOME Shell extension that shows workspaces buttons in top panel


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
rm -fr %{buildroot}%{extdir}/{README*,schemas}


%files
%doc README.md
%{extdir}
%{gschemadir}/*gschema.xml


%changelog
