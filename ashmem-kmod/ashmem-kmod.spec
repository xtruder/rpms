%define buildforkernels akmod
%global debug_package %{nil}

Name:			ashmem-kmod

Version:		1
Release:		1%{?dist}.1
Summary:        Ashmem Kernel module

Group:			System Environment/Kernel

License:        GPLv2+
URL:            https://github.com/torvalds/linux/tree/master/drivers/staging/android
Source0:        ashmem.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{_bindir}/kmodtool

%{!?kernels:BuildRequires: buildsys-build-rpmfusion-kerneldevpkgs-%{?buildforkernels:%{buildforkernels}}%{!?buildforkernels:current}-%{_target_cpu} }

# kmodtool does its magic here
%{expand:%(kmodtool --target %{_target_cpu} --repo rpmfusion --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }


%description
Ashmem kernel module needed for running waydroid

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool  --target %{_target_cpu}  --repo rpmfusion --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null


%setup -q -c -T -a 0
for kernel_version in %{?kernel_versions} ; do
	cp -a ashmem _kmod_build_${kernel_version%%___*}
done


%build
for kernel_version in %{?kernel_versions}; do
	make %{?_smp_mflags} -C "${kernel_version##*___}" V=0 M=${PWD}/_kmod_build_${kernel_version%%___*}
done


%install
rm -rf ${RPM_BUILD_ROOT}

for kernel_version in %{?kernel_versions}; do
	install -D -m 755 _kmod_build_${kernel_version%%___*}/ashmem_linux.ko  ${RPM_BUILD_ROOT}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/ashmem_linux.ko
done
%{?akmod_install}


%clean
rm -rf $RPM_BUILD_ROOT


%changelog