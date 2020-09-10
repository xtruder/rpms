%global extuuid    wsmatrix@martin.zurowietz.de
%global extdir     %{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir %{_datadir}/glib-2.0/schemas

Name:           gnome-shell-extension-workspace-matrix
Version:        4.0.1
Release:        1%{?dist}
Summary:        A Gnome workspace matrix extension

# The entire source code is GPLv3+ except convenience.js, which is BSD
License:        GPLv3+
URL:            https://github.com/mzur/gnome-shell-wsmatrix
%undefine       _disable_source_fetch
Source0:        %{url}/archive/v%{version}.tar.gz
%define         SHA256SUM0 c319278e950da2794c1aec84effee5cae00e71ac6533929c3d356f6b8bd68ef1

BuildArch:      noarch

BuildRequires:  %{_bindir}/glib-compile-schemas

Requires:       gnome-shell-extension-common
Requires:       gnome-shell >= 3.36.0

# CentOS 7 build environment doesn't support Suggests tag.
%if 0%{?fedora} || 0%{?rhel} >= 8
Suggests:       gnome-tweaks
%endif


%description
GNOME shell extension to arrange workspaces in a two dimensional grid with
workspace thumbnails.


%prep
echo "%SHA256SUM0  %SOURCE0" | sha256sum -c -
%autosetup -n gnome-shell-wsmatrix-%{version} -p 1


%build


%install
mkdir -p %{buildroot}%{extdir}
cp -pr %{extuuid}/* %{buildroot}%{extdir}

# Cleanup unused files.
rm -fr %{buildroot}%{extdir}/schemas

# Install schema.
mkdir -p %{buildroot}%{gschemadir}
cp -pr %{extuuid}/schemas/*gschema.xml %{buildroot}%{gschemadir}


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
