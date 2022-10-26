%global gitname    code-nautilus
%global giturl     https://github.com/harry-cpp/%{gitname}
%global gitcommit  12538b3a4d3bffe361da230c6eaddd80206bd444
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global gitsnapinfo .20221024git%{gitshortcommit}

Name:       %{gitname}
Summary:    Visual studio code extension for Nautilus.
Version:    0
Release:    0%{?gitsnapinfo}%{?dist}
License:    Unilicense
URL:        %{giturl}
%undefine   _disable_source_fetch
Source0:    %{url}/archive/%{gitcommit}.tar.gz#/%{name}-%{release}.tar.gz
%define     SHA256SUM0 973ab107fb75a173a508d35bd0dc30fa80cdd3a20b172288204ff5ea4621378c

BuildArch:      noarch

Requires: nautilus-python

%description
This extensions provides nautilus action to open folder in Visual Studio Code.

%prep
echo "%SHA256SUM0  %SOURCE0" | sha256sum -c -
%autosetup -n %{gitname}-%{gitcommit} -p 1


%install
install -d -D -m0755 %{buildroot}%{_datadir}/nautilus-python/extensions
install -m0644 -T code-nautilus.py %{buildroot}%{_datadir}/nautilus-python/extensions/code-nautilus.py


%files
%doc README.md
%license LICENSE
%{_datadir}/nautilus-python/extensions/*

%changelog
