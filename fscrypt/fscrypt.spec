# do not remove, as fscrypt is statically linked, and find-debuginfo.sh will fail
%global debug_package %{nil} 

Name:       fscrypt
Version:    0.3.4
Release:    0%{?dist}
Summary:    High-level tool for the management of linux filesystem encryption.
License:    ASL 2.0
URL:        https://github.com/google/fscrypt
%undefine   _disable_source_fetch
Source0:    https://github.com/google/fscrypt/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%define     SHA256SUM0 fe3c51ecb936226087bb3a62dddda5b7f5cd77dd3be7bf1feb270e1c55eddfa3

BuildArch:  x86_64

BuildRequires: gcc
BuildRequires: m4
BuildRequires: golang >= 1.16
BuildRequires: pam-devel
BuildRequires: git

Requires: pam

%description
High-level tool for the management of linux filesystem encryption.


%prep
echo "%SHA256SUM0  %SOURCE0" | sha256sum -c 
%autosetup -n %{name}-%{version}


%build
%make_build TAG_VERSION=v%{version}


%install
%make_install \
    PREFIX=%{_prefix} \
    PAM_MODULE_DIR=%{_libdir}/security \
    PAM_CONFIG_DIR=%{_datadir}/pam-configs


%files
%doc README.md NEWS.md
%license LICENSE
%{_bindir}/fscrypt
%{_libdir}/security/pam_fscrypt.so
%{_datadir}/pam-configs/fscrypt
%{_datadir}/bash-completion/completions/fscrypt


%changelog
