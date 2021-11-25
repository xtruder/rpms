Name:       fscrypt
Version:    0.3.1
Release:    0%{?dist}
Summary:    High-level tool for the management of linux filesystem encryption.
License:    ASL 2.0
URL:        https://github.com/google/fscrypt
%undefine   _disable_source_fetch
Source0:    https://github.com/google/fscrypt/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%define     SHA256SUM0 7ed190ac9a53a0c378620f226da4e700375a055a99b888beef1c4efa3ff7f0e6

BuildArch:  x86_64

BuildRequires: gcc
BuildRequires: m4
BuildRequires: golang >= 1.11
BuildRequires: pam-devel
BuildRequires: git

Requires: pam

%description
High-level tool for the management of linux filesystem encryption.


%prep
echo "%SHA256SUM0  %SOURCE0" | sha256sum -c 
%autosetup -n %{name}-%{version}


%build
%make_build TAG_VERSION=v%{version} GO111MODULE=on


%install
%make_install \
    PREFIX=%{_prefix} \
    PAM_MODULE_DIR=%{_libdir}/security \
    PAM_CONFIG_DIR=%{_datadir}/pam-configs


%files
%doc README.md
%license LICENSE
%{_bindir}/fscrypt
%{_libdir}/security/pam_fscrypt.so
%{_datadir}/pam-configs/fscrypt


%changelog
