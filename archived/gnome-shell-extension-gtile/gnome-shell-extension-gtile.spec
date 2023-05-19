%global extuuid    gTile@vibou
%global extdir     %{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir %{_datadir}/glib-2.0/schemas
%global gitname    gTile
%global giturl     https://github.com/gTile/%{gitname}
%global gitcommit d7aa9ff5f4bcf5ac69302003c080573ff780b282
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global gitsnapinfo .20200809git%{gitshortcommit}


Name:           gnome-shell-extension-gtile
Version:        35
Release:        2%{?gitsnapinfo}%{?dist}
Summary:        Gnome-shell extension that improves window tiling capabilities of stock gnome-shell

License:        GPLv2+
URL:            %{giturl}
%undefine       _disable_source_fetch
Source0:        %{url}/archive/%{gitcommit}.tar.gz#/%{name}-%{release}.tar.gz
%define         SHA256SUM0 7db0b498f635498c5b5139052c9d65f712e0e503411159298889e4e047213049

BuildArch:      noarch

BuildRequires:  %{_bindir}/glib-compile-schemas
BuildRequires:  bazel3
BuildRequires:  gcc
BuildRequires:  python3

Requires:       gnome-shell-extension-common
Requires:       gnome-shell >= 3.14

# CentOS 7 build environment doesn't support Suggests tag.
%if 0%{?fedora} || 0%{?rhel} >= 8
Suggests:       gnome-tweaks
%endif


%description
Gnome-shell extension that improves window tiling capabilities of stock gnome-shell.


%prep
echo "%SHA256SUM0  %SOURCE0" | sha256sum -c -
%autosetup -n %{gitname}-%{gitcommit} -p 1


%build
bazel build :dist


%install
mkdir -p %{buildroot}%{extdir}
tar -xzf "bazel-bin/dist.tar.gz" --directory "%{buildroot}%{extdir}"

# Cleanup unused files.
rm -fr %{buildroot}%{extdir}/LICENSE

# Install schema.
mkdir -p %{buildroot}%{gschemadir}
cp -pr schemas/*gschema.xml %{buildroot}%{gschemadir}


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
