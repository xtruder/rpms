%define buildforkernels current
%define _unpackaged_files_terminate_build 0
%global debug_package %{nil}

Name:           tuxedo-drivers-kmod

Version:        4.4.3
Release:        0%{?dist}
Summary:        Tuxedo drivers kmod package

Group:          System Environment/Kernel

License:        GPLv2+
URL:            https://github.com/tuxedocomputers/tuxedo-drivers
Source0:        https://github.com/tuxedocomputers/tuxedo-drivers/archive/refs/tags/v%{version}.tar.gz#/tuxedo-drivers-%{version}.tar.gz
%define	        SHA256SUM0 65950b8c1e81da6d2583a2612b2a4f4d7390af20d73ef772309fb19008323561
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{_bindir}/kmodtool
ExclusiveArch:  x86_64

%{!?kernels:BuildRequires: buildsys-build-rpmfusion-kerneldevpkgs-%{?buildforkernels:%{buildforkernels}}%{!?buildforkernels:current}-%{_target_cpu} }

# kmodtool does its magic here
%{expand:%(kmodtool --target %{_target_cpu} --repo rpmfusion --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Linux kernel modules for tuxedo laptops

%package common
Summary: Tuxedo Kernel Modules user package

# this is here to make tuxedo-control-center install, without installing dkms drivers
Provides:       tuxedo-drivers = %{version}

%description common
Tuxedo kernel Modules user package

%prep
echo "%SHA256SUM0 %SOURCE0" | sha256sum -c -

# print kmodtool output for debugging purposes:
kmodtool --target %{_target_cpu} --repo rpmfusion --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

# error out if there was something wrong with kmodtool
%{?kmodtool_check}

%setup -q -c -T -a 0

for kernel_version in %{?kernel_versions} ; do
    cp -a tuxedo-drivers-%{version} _kmod_build_${kernel_version%%___*}
done


%build
echo versions %{?kernel_versions}
for kernel_version in %{?kernel_versions}; do
    make %{?_smp_mflags} -C "${kernel_version##*___}" M=${PWD}/_kmod_build_${kernel_version%%___*} modules
done


%install
rm -rf ${RPM_BUILD_ROOT}

for kernel_version in %{?kernel_versions}; do
    make -C "${kernel_version##*___}" M=${PWD}/_kmod_build_${kernel_version%%___*}/src INSTALL_MOD_PATH=${RPM_BUILD_ROOT} INSTALL_MOD_DIR=%{kmodinstdir_postfix} modules_install
done

install -D -m 644 tuxedo-drivers-%{version}/tuxedo_keyboard.conf ${RPM_BUILD_ROOT}%{_sysconfdir}/modprobe.d/tuxedo_keyboard.conf
install -D -m 644 tuxedo-drivers-%{version}/99-z-tuxedo-systemd-fix.rules ${RPM_BUILD_ROOT}%{_sysconfdir}/udev/rules.d/99-z-tuxedo-systemd-fix.rules
%{?akmod_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%{_sysconfdir}/modprobe.d/tuxedo_keyboard.conf
%{_sysconfdir}/udev/rules.d/99-z-tuxedo-systemd-fix.rules

%changelog
* Mon May 13 2024 offlinehq
- Update to version 4.4.3
* Fri Mar 15 2024 offlinehq
- Add Provides for tuxedo-drivers
* Fri Mar 15 2024 offlinehq
- Update to version 4.3.2
* Mon Feb 05 2024 offlinehq
- Initial Fedora build
