%global extuuid    disable-workspace-switcher-popup@github.com
%global extdir     %{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir %{_datadir}/glib-2.0/schemas
%global gitname    disable-workspace-switcher-popup
%global giturl     https://github.com/windsorschmidt/%{gitname}
%global gitcommit  7b04d732616a1422a1490f23b302a71466331bff
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global gitsnapinfo .20221006git%{gitshortcommit}

Name:           gnome-shell-extension-disable-workspace-switcher-popup
Version:        0
Release:        1%{?gitsnapinfo}%{?dist}
Summary:        Gnome-Shell Extension Disable Window Switcher Popup

License:        BSD-2-Clause
URL:            %{giturl}
%undefine       _disable_source_fetch
Source0:        %{giturl}/archive/%{gitcommit}.tar.gz#/%{name}-%{release}.tar.gz
%define         SHA256SUM0 34b09c8bafa6905a31622020bc6a60b68de712f87ad19e53ade7166b43c2f635

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
