%global extuuid    unsafe-mode@ramottamado.dev
%global extdir     %{_datadir}/gnome-shell/extensions/%{extuuid}
%global gitname    unsafe-mode
%global giturl     https://github.com/ramottamado/%{gitname}
%global gitcommit  950775a3fdec59942e6812d43557bbdb94af64bd
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global gitsnapinfo .20211017git%{gitshortcommit}

Name:           gnome-shell-extension-unsafe-mode
Version:        0
Release:        0%{?gitsnapinfo}%{?dist}
Summary:        Unsafe Mode GNOME Shell Extension

License:        GPLv2
URL:            %{giturl}
%undefine       _disable_source_fetch
Source0:        %{giturl}/archive/%{gitcommit}.tar.gz#/%{name}-%{release}.tar.gz
%define         SHA256SUM0 d92eff0a0a386ff9c6d50c93aa3ac878264fcc5e42545642e7056f37a2beaf72

BuildArch:      noarch

Requires:       gnome-shell-extension-common
Requires:       gnome-shell >= 4.41.0


%description
Since GNOME 41, GNOME's private D-Bus APIs are now restricted to a few caller only (see this merge request).
This change also brings unsafe-mode in Mutter's MetaContext, to override the restriction and lift the caller restrictions,
and showing an icon in the top bar area to indicate that unsafe-mode is on.
This extension provides easy switch to turn on unsafe-mode.


%prep
echo "%SHA256SUM0  %SOURCE0" | sha256sum -c -
%autosetup -n %{gitname}-%{gitcommit} -p 1


%build


%install
mkdir -p %{buildroot}%{extdir}
cp -pr unsafe-mode@ramottamado.dev/* %{buildroot}%{extdir}


%files
%doc README.md
%license LICENSE
%{extdir}


%changelog
