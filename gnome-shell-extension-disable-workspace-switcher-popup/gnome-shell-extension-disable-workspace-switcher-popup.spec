%global extuuid    gnome-shell-extension-disable-workspace-switcher-popup@github.com
%global extdir     %{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir %{_datadir}/glib-2.0/schemas
%global gitname    disable-workspace-switcher-popup
%global giturl     https://github.com/windsorschmidt/%{gitname}
%global gitcommit  cf509c41ae52e7eee85afb6f90397f416a6926ab
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global gitsnapinfo .20211004git%{gitshortcommit}

Name:           gnome-shell-extension-disable-workspace-switcher-popup
Version:        0
Release:        0%{?gitsnapinfo}%{?dist}
Summary:        Gnome-Shell Extension Disable Window Switcher Popup

License:        BSD-2-Clause
URL:            %{giturl}
%undefine       _disable_source_fetch
Source0:        %{giturl}/archive/%{gitcommit}.tar.gz#/%{name}-%{release}.tar.gz
%define         SHA256SUM0 30bdea6918de977d5d2a251ba360c1aa1decb8742e8e92bf7f99a5eee5b7b239

BuildArch:      noarch

BuildRequires:  %{_bindir}/glib-compile-schemas

Requires:       gnome-shell-extension-common
Requires:       gnome-shell >= 3.34.0


%description
This extension disables the overlay displayed when switching between workspaces.


%prep
echo "%SHA256SUM0  %SOURCE0" | sha256sum -c -
%autosetup -n %{gitname}-%{gitcommit} -p 1


%build


%install
mkdir -p %{buildroot}%{extdir}
cp -pr disable-workspace-switcher-popup@github.com/* %{buildroot}%{extdir}

%files
%doc README.md
%{extdir}


%changelog
