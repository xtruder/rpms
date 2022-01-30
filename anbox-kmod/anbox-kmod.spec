%define buildforkernels akmod
%global debug_package %{nil}
%global gitname    anbox-modules
%global giturl     https://github.com/choff/%{gitname}
%global gitcommit  8148a162755bf5500a07cf41a65a02c8f3eb0af9
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global gitsnapinfo .20220130git%{gitshortcommit}

Name:			anbox-kmod

Version:		0
Release:		0%{?gitsnapinfo}%{?dist}
Summary:        Anbox Kernel Modules

Group:			System Environment/Kernel

License:        GPLv2+
URL:            %{giturl}
%undefine       _disable_source_fetch
Source0:        %{giturl}/archive/%{gitcommit}.tar.gz#/%{name}-%{release}.tar.gz
%define         SHA256SUM0 82dc872b6d80d5f461b2485ba68223d3fbdced03d749562febfb8e9ba383f0ec
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{_bindir}/kmodtool

%{!?kernels:BuildRequires: buildsys-build-rpmfusion-kerneldevpkgs-%{?buildforkernels:%{buildforkernels}}%{!?buildforkernels:current}-%{_target_cpu} }

# kmodtool does its magic here
%{expand:%(kmodtool --target %{_target_cpu} --repo rpmfusion --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }


%description
Linux kernel modules necessary to run the Anbox Android container runtime

%package common
Summary: Anbox Kernel Modules user package

%description common
Linux kernel modules necessary to run the Anbox Android container runtime, user package

%prep
echo "%SHA256SUM0  %SOURCE0" | sha256sum -c -
%autosetup -n %{gitname}-%{gitcommit} -p 1

# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool  --target %{_target_cpu}  --repo rpmfusion --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

for kernel_version in %{?kernel_versions} ; do
	mkdir -p _kmod_build_${kernel_version%%___*}
	cp -a ashmem _kmod_build_${kernel_version%%___*}/ashmem
	cp -a binder _kmod_build_${kernel_version%%___*}/binder
done


%build
for kernel_version in %{?kernel_versions}; do
	make %{?_smp_mflags} -C "${kernel_version##*___}" V=0 M=${PWD}/_kmod_build_${kernel_version%%___*}/ashmem
	make %{?_smp_mflags} -C "${kernel_version##*___}" V=0 M=${PWD}/_kmod_build_${kernel_version%%___*}/binder
done


%install
rm -rf ${RPM_BUILD_ROOT}

for kernel_version in %{?kernel_versions}; do
	install -D -m 755 _kmod_build_${kernel_version%%___*}/ashmem/ashmem_linux.ko  ${RPM_BUILD_ROOT}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/ashmem_linux.ko
	install -D -m 755 _kmod_build_${kernel_version%%___*}/binder/binder_linux.ko  ${RPM_BUILD_ROOT}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/binder_linux.ko
done

install -D -m 644 anbox.conf  ${RPM_BUILD_ROOT}%{_sysconfdir}/modules-load.d/anbox.conf
install -D -m 644 99-anbox.rules ${RPM_BUILD_ROOT}%{_sysconfdir}/udev/rules.d/99-anbox.rules
%{?akmod_install}

%files common
%{_sysconfdir}/modules-load.d/anbox.conf
%{_sysconfdir}/udev/rules.d/99-anbox.rules


%clean
rm -rf $RPM_BUILD_ROOT


%changelog