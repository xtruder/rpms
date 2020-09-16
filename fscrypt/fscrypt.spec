%define     debug_package %{nil}
%undefine   _disable_source_fetch

Name:       fscrypt
Version:    0.2.9
Release:    1%{dist}
Summary:    High-level tool for the management of linux filesystem encryption.
License:    ASL 2.0
URL:        https://github.com/google/fscrypt
Source0:    https://github.com/google/fscrypt/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%define     SHA256SUM0 36f1166d9886548b0d72beeeffb9ca8fb5b28b63a42b369923bc3f0bea78bb3d

BuildArch: noarch

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
%autosetup -n %{name}-%{version} x


%build
%make_build TAG_VERSION=v%{version}


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
