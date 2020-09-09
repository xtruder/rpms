%global extuuid    workspace-switcher@tomha.github.com
%global extdir     %{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir %{_datadir}/glib-2.0/schemas
%global gitname    gnome-shell-extension-workspace-switcher
%global giturl     https://github.com/Tomha/%{gitname}
%global gitcommit b3d65528a3a1eb5aba55d12af174f854b4bf4cc5
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global gitsnapinfo .20190119git%{gitshortcommit}

Name:           gnome-shell-extension-workspace-switcher
Version:        0
Release:        0%{?gitsnapinfo}%{?dist}
Summary:        A Gnome workspace switcher

# The entire source code is GPLv3+ except convenience.js, which is BSD
License:        GPLv3+
URL:            %{giturl}
Source0:        %{giturl}/archive/%{gitcommit}.tar.gz#/%{name}-%{version}-%{gitshortcommit}.tar.gz

BuildArch:      noarch

BuildRequires:  %{_bindir}/glib-compile-schemas

Requires:       gnome-shell-extension-common
Requires:       gnome-shell >= 3.24.0

# CentOS 7 build environment doesn't support Suggests tag.
%if 0%{?fedora} || 0%{?rhel} >= 8
Suggests:       gnome-tweaks
%endif


%description
Display system information in gnome shell status bar, such as memory usage,
CPU usage, and network rate...


%prep
%autosetup -n %{gitname}-%{gitcommit} -p 1


%build


%install
mkdir -p %{buildroot}%{extdir}
cp -pr * %{buildroot}%{extdir}

# Cleanup unused files.
rm -fr %{buildroot}%{extdir}/{LICENSE,README*,schemas}

# Install schema.
mkdir -p %{buildroot}%{gschemadir}
cp -pr schema/*gschema.xml %{buildroot}%{gschemadir}


# CentOS 7 doesn't compile gschemas automatically, Fedora does.
%if 0%{?rhel} && 0%{?rhel} <= 7
%postun
if [ $1 -eq 0 ] ; then
  %{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
fi

%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
%endif


%files
%doc README.md
%license LICENSE
%{extdir}
%{gschemadir}/*gschema.xml


%changelog
