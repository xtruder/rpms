%global extuuid    workspaces-bar@fthx
%global extdir     %{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir %{_datadir}/glib-2.0/schemas
%global gitname    workspaces-bar
%global giturl     https://github.com/fthx/%{gitname}
%global gitcommit  5983c756673051e08ccc37cfed8efb92383c4cfa
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global gitsnapinfo .20211125git%{gitshortcommit}

Name:           gnome-shell-extension-workspaces-bar
Version:        0
Release:        0%{?gitsnapinfo}%{?dist}
Summary:        A Gnome workspace switcher

# The entire source code is GPLv3+ except convenience.js, which is BSD
License:        GPLv3+
URL:            %{giturl}
%undefine       _disable_source_fetch
Source0:        %{giturl}/archive/%{gitcommit}.tar.gz#/%{name}-%{release}.tar.gz
%define         SHA256SUM0 1ca177646dc2bb6244e9e3928b096f1a2edc9293ffb33c3bf375d480d388945f

BuildArch:      noarch

BuildRequires:  %{_bindir}/glib-compile-schemas

Requires:       gnome-shell-extension-common
Requires:       gnome-shell >= 3.36.0


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
