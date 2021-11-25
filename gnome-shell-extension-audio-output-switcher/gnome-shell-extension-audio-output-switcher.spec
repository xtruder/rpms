%global extuuid    audio-output-switcher@anduchs
%global extdir     %{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir %{_datadir}/glib-2.0/schemas
%global gitname    audio-output-switcher
%global giturl     https://github.com/adaxi/%{gitname}
%global gitcommit  232a12281db967ecbee66f6df52ba3f205536722
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global gitsnapinfo .20211004git%{gitshortcommit}

Name:           gnome-shell-extension-audio-output-switcher
Version:        0
Release:        0%{?gitsnapinfo}%{?dist}
Summary:        Gnome-Shell Extension Audio-Output-Switcher

License:        BSD-2-Clause
URL:            %{giturl}
%undefine       _disable_source_fetch
Source0:        %{giturl}/archive/%{gitcommit}.tar.gz#/%{name}-%{release}.tar.gz
%define         SHA256SUM0 23a24ada5bbe8b7dcf1167c43320e365aca765732211e623c9ddf989f7a3f4c4

BuildArch:      noarch

BuildRequires:  %{_bindir}/glib-compile-schemas

Requires:       gnome-shell-extension-common
Requires:       gnome-shell >= 3.34.0


%description
This extension adds a little entry to the status-menu that shows the currently
selected pulse-audio-output device. Clicking on that will open a submenu with all
available output devices and let's you choose which one to use.


%prep
echo "%SHA256SUM0  %SOURCE0" | sha256sum -c -
%autosetup -n %{gitname}-%{gitcommit} -p 1


%build


%install
mkdir -p %{buildroot}%{extdir}
cp -pr * %{buildroot}%{extdir}

# Cleanup unused files.
rm -fr %{buildroot}%{extdir}/{LICENSE,README*,Makefile,schemas}

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
