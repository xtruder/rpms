%global gitname    trezord-go
%global giturl     https://github.com/trezor/%{gitname}
%global gitcommit  db03d99230f5b609a354e3586f1dfc0ad6da16f7
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global gitsnapinfo .20240531git%{gitshortcommit}

Name:           trezord
Version:        2.0.33
Release:        0%{?gitsnapinfo}%{?dist}
Summary:        Trezor Communication Daemon
License:        GPLv3.0
URL:            %{giturl}

Source0:        %{giturl}/archive/%{gitcommit}.tar.gz#/%{name}-%{version}-%{gitshortcommit}.tar.gz
%define         SHA256SUM0 9d02711e6c495793316775526ca93df860741ce7748641a662fb877ec0ef00ba

Requires(pre):  shadow-utils
BuildRequires:  golang
BuildRequires:  git
BuildRequires:  systemd-rpm-macros

Provides:       %{name} = %{version}

%description
Trezor Communication Daemon (also called trezor bridge)

%global debug_package %{nil}

%prep
echo "%SHA256SUM0  %SOURCE0" | sha256sum -c -
%autosetup -n %{gitname}-%{gitcommit} -p 1


%build
go build -v ./


%install
install -Dpm 0755 trezord-go %{buildroot}%{_bindir}/trezord
install -Dpm 644 release/linux/trezord.service %{buildroot}%{_unitdir}/trezord.service


%pre
getent group trezord >/dev/null || groupadd -r trezord
getent group plugdev >/dev/null || groupadd -r plugdev
getent passwd trezord >/dev/null || useradd -r -g trezord -d /var -s /bin/false -c "Trezor Bridge" trezord
usermod -a -G plugdev trezord
touch /var/log/trezord.log
chown trezord:trezord /var/log/trezord.log
chmod 660 /var/log/trezord.log
exit 0

%post
%systemd_post trezord.service

%preun
%systemd_preun trezord.service

%files
%license COPYING
%{_bindir}/trezord
%{_unitdir}/trezord.service


%changelog
* Fri May 31 2024 offlinehq
- Initial Fedora build
