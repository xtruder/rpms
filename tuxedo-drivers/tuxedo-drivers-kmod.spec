%define buildforkernels current
%define _unpackaged_files_terminate_build 0
%global debug_package %{nil}

Name:           tuxedo-drivers-kmod

Version:        4.3.2
Release:        1%{?dist}
Summary:        Tuxedo drivers kmod package

Group:          System Environment/Kernel

License:        GPLv2+
URL:            https://github.com/tuxedocomputers/tuxedo-drivers
Source0:        https://github.com/tuxedocomputers/tuxedo-drivers/archive/refs/tags/v%{version}.tar.gz#/tuxedo-drivers-%{version}.tar.gz
%define	        SHA256SUM0 b7bfe2905df7e37d92704363b9b0adb550dc9f8449b70c9dbdb40dc5075bc8e4
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{_bindir}/kmodtool
ExclusiveArch:  x86_64

Provides:       tuxedo-drivers = %{version}

%{!?kernels:BuildRequires: buildsys-build-rpmfusion-kerneldevpkgs-%{?buildforkernels:%{buildforkernels}}%{!?buildforkernels:current}-%{_target_cpu} }

# kmodtool does its magic here
%{expand:%(kmodtool --target %{_target_cpu} --repo rpmfusion --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Linux kernel modules for tuxedo laptops

%package common
Summary: Tuxedo Kernel Modules user package

%description common
Tuxedo kernel Modules user package

%prep
echo "%SHA256SUM0 %SOURCE0" | sha256sum -c -

# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool  --target %{_target_cpu}  --repo rpmfusion --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

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
* Fri Mar 15 2024 offlinehq
- Update to version 4.3.2
* Mon Feb 05 2024 offlinehq
- Initial Fedora build
