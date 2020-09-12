%global gitname    code-nautilus
%global giturl     https://github.com/harry-cpp/%{gitname}
%global gitcommit  37ff018ee4d8d917b6da094a513da1f622b11bcb
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global gitsnapinfo .20191114git%{gitshortcommit}

Name:       %{gitname}
Summary:    Visual studio code extension for Nautilus.
Version:    0
Release:    1%{?gitsnapinfo}%{?dist}
License:    Unilicense
URL:        %{giturl}
%undefine   _disable_source_fetch
Source0:    %{url}/archive/%{gitcommit}.tar.gz#/%{name}-%{release}.tar.gz
%define     SHA256SUM0 e20c39bc7fe3f2986e04ae7912e9bfe743c3289122ab75a1359e06174a029d13

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
