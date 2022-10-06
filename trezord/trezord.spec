Name:           trezord
Version:        2.0.32
Release:        1%{?dist}
Summary:        Trezor Communication Daemon
License:        GPLv3.0

URL:            https://github.com/trezor/trezord-go
Source0:        https://github.com/trezor/trezord-go/archive/refs/tags/v%{version}.tar.gz#/trezord-go-%{version}.tar.gz

Requires(pre):  shadow-utils
BuildRequires:  golang
BuildRequires:  git
BuildRequires:  systemd-rpm-macros

Provides:       %{name} = %{version}

%description
Trezor Communication Daemon (also called trezor bridge)

%global debug_package %{nil}

%prep
%autosetup -n trezord-go-%{version}


%build
GO111MODULE=on go build -v ./


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
