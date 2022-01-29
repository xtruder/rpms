%define modname ashmem

Name:           %{modname}-kmod-common

Version:		1
Release:		1%{?dist}.1
Summary:        Common files for ashmem linux driver

Group:          System Environment/Kernel

License:        GPL
Source0:        ashmem.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
Userland pacakge for ashmem-kmod kernel module

%prep
%setup -q -c -T -a 0

%build

%install
install -D -m 755 ashmem/README.md  ${RPM_BUILD_ROOT}/usr/share/doc/ashmem-kmod-common/README.md

%files
%doc README.md

%changelog
