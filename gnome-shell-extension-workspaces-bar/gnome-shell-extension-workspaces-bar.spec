%global extuuid    workspaces-bar@fthx
%global extdir     %{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir %{_datadir}/glib-2.0/schemas
%global gitname    workspaces-bar
%global giturl     https://github.com/fthx/%{gitname}
%global gitcommit 1a28afae7db9d924867b022f30049590f1170add
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global gitsnapinfo .20210408git%{gitshortcommit}

Name:           gnome-shell-extension-workspaces-bar
Version:        0
Release:        0%{?gitsnapinfo}%{?dist}
Summary:        A Gnome workspace switcher

# The entire source code is GPLv3+ except convenience.js, which is BSD
License:        GPLv3+
URL:            %{giturl}
%undefine       _disable_source_fetch
Source0:        %{giturl}/archive/%{gitcommit}.tar.gz#/%{name}-%{release}.tar.gz
%define         SHA256SUM0 577f1424cd663f58bcfa313f598f563b1a5e2f148cff4a314097a27c720efb07

BuildArch:      noarch

BuildRequires:  %{_bindir}/glib-compile-schemas

Requires:       gnome-shell-extension-common
Requires:       gnome-shell >= 3.24.0

# CentOS 7 build environment doesn't support Suggests tag.
%if 0%{?fedora} || 0%{?rhel} >= 8
Suggests:       gnome-tweaks
%endif


%description
GNOME Shell extension that shows workspaces buttons in top panel


%prep
echo "%SHA256SUM0  %SOURCE0" | sha256sum -c -
%autosetup -n %{gitname}-%{gitcommit} -p 1


%build


%install
mkdir -p %{buildroot}%{extdir}
cp -pr * %{buildroot}%{extdir}

# Cleanup unused files.
rm -fr %{buildroot}%{extdir}/{README*}


%files
%doc README.md
%{extdir}


%changelog
