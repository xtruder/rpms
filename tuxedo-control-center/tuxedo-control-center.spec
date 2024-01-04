Name:               tuxedo-control-center
Version:            2.1.2
Release:            1%{?dist}
Summary:            TUXEDO Control Center Application

License:            GPL-3.0
URL:                https://www.tuxedocomputers.com
Source0:            %{name}-%{version}.tar.gz

Group:              default
Vendor:             TUXEDO Computers GmbH <tux@tuxedocomputers.com>
Packager:           TUXEDO Computers GmbH <tux@tuxedocomputers.com>

Requires:           ((tuxedo-keyboard >= 3.1.2) or (tuxedo-drivers >= 3.1.2))
Requires:           libappindicator
Requires(post):     bash
Requires(preun):    bash
Obsoletes:          tuxedofancontrol <= 0.1.9

%define __os_install_post %{nil}
%define _build_id_links none
%global tccdir opt/tuxedo-control-center

%description
TUXEDO Control Center Application

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_datadir}/icons
cp -r usr/share/icons/* %{buildroot}%{_datadir}/icons/

mkdir -p %{buildroot}/%{tccdir}
cp -r %{tccdir}/* %{buildroot}/%{tccdir}/

mkdir -p %{buildroot}/%{tccdir}/resources/dist/tuxedo-control-center/data/service
cp %{tccdir}/resources/dist/tuxedo-control-center/data/service/tccd %{buildroot}/%{tccdir}/resources/dist/tuxedo-control-center/data/service/tccd

DIST_DATA=%{tccdir}/resources/dist/tuxedo-control-center/data/dist-data

mkdir -p %{buildroot}%{_datadir}/applications
cp ${DIST_DATA}/tuxedo-control-center.desktop %{buildroot}%{_datadir}/applications/tuxedo-control-center.desktop

mkdir -p %{buildroot}%{_sysconfdir}/skel/.config/autostart
cp ${DIST_DATA}/tuxedo-control-center-tray.desktop %{buildroot}%{_sysconfdir}/skel/.config/autostart/tuxedo-control-center-tray.desktop

mkdir -p %{buildroot}%{_datadir}/polkit-1/actions
cp ${DIST_DATA}/com.tuxedocomputers.tccd.policy %{buildroot}%{_datadir}/polkit-1/actions/com.tuxedocomputers.tccd.policy

mkdir -p %{buildroot}%{_datadir}/dbus-1/system.d
cp ${DIST_DATA}/com.tuxedocomputers.tccd.conf %{buildroot}%{_datadir}/dbus-1/system.d/com.tuxedocomputers.tccd.conf

mkdir -p %{buildroot}%{_sysconfdir}/systemd/system
cp ${DIST_DATA}/tccd.service %{buildroot}%{_sysconfdir}/systemd/system/tccd.service
cp ${DIST_DATA}/tccd-sleep.service %{buildroot}%{_sysconfdir}/systemd/system/tccd-sleep.service

mkdir -p %{buildroot}%{_sysconfdir}/udev/rules.d
cp ${DIST_DATA}/99-webcam.rules %{buildroot}%{_sysconfdir}/udev/rules.d/99-webcam.rules

mkdir -p %{buildroot}%{_bindir}
ln -sf /%{tccdir}/tuxedo-control-center %{buildroot}%{_bindir}/tuxedo-control-center

%files
%defattr(-,root,root,-)
/%{tccdir}/LICENSE.electron.txt
/%{tccdir}/LICENSES.chromium.html
/%{tccdir}/chrome-sandbox
/%{tccdir}/chrome_100_percent.pak
/%{tccdir}/chrome_200_percent.pak
/%{tccdir}/icudtl.dat
/%{tccdir}/libEGL.so
/%{tccdir}/libGLESv2.so
/%{tccdir}/libffmpeg.so
/%{tccdir}/libvk_swiftshader.so
/%{tccdir}/libvulkan.so.1
/%{tccdir}/locales/am.pak
/%{tccdir}/locales/ar.pak
/%{tccdir}/locales/bg.pak
/%{tccdir}/locales/bn.pak
/%{tccdir}/locales/ca.pak
/%{tccdir}/locales/cs.pak
/%{tccdir}/locales/da.pak
/%{tccdir}/locales/de.pak
/%{tccdir}/locales/el.pak
/%{tccdir}/locales/en-GB.pak
/%{tccdir}/locales/en-US.pak
/%{tccdir}/locales/es-419.pak
/%{tccdir}/locales/es.pak
/%{tccdir}/locales/et.pak
/%{tccdir}/locales/fa.pak
/%{tccdir}/locales/fi.pak
/%{tccdir}/locales/fil.pak
/%{tccdir}/locales/fr.pak
/%{tccdir}/locales/gu.pak
/%{tccdir}/locales/he.pak
/%{tccdir}/locales/hi.pak
/%{tccdir}/locales/hr.pak
/%{tccdir}/locales/hu.pak
/%{tccdir}/locales/id.pak
/%{tccdir}/locales/it.pak
/%{tccdir}/locales/ja.pak
/%{tccdir}/locales/kn.pak
/%{tccdir}/locales/ko.pak
/%{tccdir}/locales/lt.pak
/%{tccdir}/locales/lv.pak
/%{tccdir}/locales/ml.pak
/%{tccdir}/locales/mr.pak
/%{tccdir}/locales/ms.pak
/%{tccdir}/locales/nb.pak
/%{tccdir}/locales/nl.pak
/%{tccdir}/locales/pl.pak
/%{tccdir}/locales/pt-BR.pak
/%{tccdir}/locales/pt-PT.pak
/%{tccdir}/locales/ro.pak
/%{tccdir}/locales/ru.pak
/%{tccdir}/locales/sk.pak
/%{tccdir}/locales/sl.pak
/%{tccdir}/locales/sr.pak
/%{tccdir}/locales/sv.pak
/%{tccdir}/locales/sw.pak
/%{tccdir}/locales/ta.pak
/%{tccdir}/locales/te.pak
/%{tccdir}/locales/th.pak
/%{tccdir}/locales/tr.pak
/%{tccdir}/locales/uk.pak
/%{tccdir}/locales/vi.pak
/%{tccdir}/locales/zh-CN.pak
/%{tccdir}/locales/zh-TW.pak
/%{tccdir}/resources.pak
/%{tccdir}/resources/app.asar
/%{tccdir}/resources/dist/tuxedo-control-center/data/camera/cameractrls.py
/%{tccdir}/resources/dist/tuxedo-control-center/data/camera/v4l2_kernel_names.json
/%{tccdir}/resources/dist/tuxedo-control-center/data/dist-data/99-webcam.rules
/%{tccdir}/resources/dist/tuxedo-control-center/data/dist-data/com.tuxedocomputers.tccd.conf
/%{tccdir}/resources/dist/tuxedo-control-center/data/dist-data/com.tuxedocomputers.tccd.policy
/%{tccdir}/resources/dist/tuxedo-control-center/data/dist-data/tccd-sleep.service
/%{tccdir}/resources/dist/tuxedo-control-center/data/dist-data/tccd.service
/%{tccdir}/resources/dist/tuxedo-control-center/data/dist-data/tuxedo-control-center-tray.desktop
/%{tccdir}/resources/dist/tuxedo-control-center/data/dist-data/tuxedo-control-center.desktop
/%{tccdir}/resources/dist/tuxedo-control-center/data/dist-data/tuxedo-control-center_256.svg
/%{tccdir}/resources/dist/tuxedo-control-center/data/service/tccd
/%{tccdir}/snapshot_blob.bin
/%{tccdir}/swiftshader/libEGL.so
/%{tccdir}/swiftshader/libGLESv2.so
/%{tccdir}/tuxedo-control-center
/%{tccdir}/v8_context_snapshot.bin
/%{tccdir}/vk_swiftshader_icd.json
%{_datadir}/applications/tuxedo-control-center.desktop
%{_datadir}/icons/hicolor/scalable/apps/tuxedo-control-center.svg
%{_sysconfdir}/skel/.config/autostart/tuxedo-control-center-tray.desktop
%{_datadir}/polkit-1/actions/com.tuxedocomputers.tccd.policy
%{_datadir}/dbus-1/system.d/com.tuxedocomputers.tccd.conf
%{_sysconfdir}/systemd/system/tccd.service
%{_sysconfdir}/systemd/system/tccd-sleep.service
%{_sysconfdir}/udev/rules.d/99-webcam.rules
%{_bindir}/tuxedo-control-center

%changelog
* Fri Dec 22 2023 kallepm
- Update to release v2.1.2
* Mon Dec 18 2023 kallepm
- Update to release v2.1.1
* Wed Nov 15 2023 kallepm
- Update to release v2.0.11
* Tue Oct 31 2023 kallepm
- Update to release v2.0.10
* Thu Oct 5 2023 kallepm
- Update to release v2.0.9
* Sat Aug 12 2023 kallepm
- Update to release v2.0.8
* Mon Jun 12 2023 kallepm
- Update to release v2.0.7
* Sun May 7 2023 kallepm
- Spec file rewrite
* Sat May 6 2023 kallepm
- Update to release v2.0.5
* Thu Mar 23 2023 kallepm
- Update to release v2.0.0
* Tue Jan 17 2023 kallepm
- Update to release v1.2.4
* Thu Dec 22 2022 kallepm
- Update to release v1.2.3
* Thu Nov 24 2022 kallepm
- Update to release v1.2.2
* Tue Jun 21 2022 kallepm
- Update to release v1.1.4
* Fri Apr 15 2022 kallepm
- Update to release v1.1.3
* Wed Dec 08 2021 kallepm
- Update to release v1.1.2
* Sun Nov 28 2021 kallepm
- Update to release v1.1.1
* Mon Aug 30 2021 kallepm
- Update to release v1.1.0
* Fri May 21 2021 kallepm
- Update to release v1.0.14
* Sun Apr 25 2021 kallepm
- Update to release v1.0.13
* Sun Apr 11 2021 kallepm
- Update to release v1.0.12
* Fri Apr 09 2021 kallepm
- Initial Fedora build
