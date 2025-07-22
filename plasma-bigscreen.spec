%global commit 046d404e34aa04f4deddddd40e8bdf40dfa43d05
%global shortcommit 046d404
%global gitdate 20240204.214319

Name:          plasma-bigscreen
Version:       6.4.80
Release:       1horizon
License:       BSD-2-Clause and BSD-3-Clause and CC0-1.0 and GPL-2.0-or-later and CC-BY-SA-4.0
Summary:       A big launcher giving you access to any installed apps and skills
Url:           https://plasma-bigscreen.org/
Source0:       https://raw.githubusercontent.com/horizonlinux/plasma-bigscreen-rpms/refs/heads/main/%{name}-%{version}.tar.gz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6Svg)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6Screen)

BuildRequires: cmake(Plasma)
BuildRequires: cmake(PlasmaActivities)
BuildRequires: cmake(PlasmaActivitiesStats)

BuildRequires: cmake(LibKWorkspace)

BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Multimedia)


Requires:   %{name}-wayland = %{version}-%{release}
Requires:   plasma-nano

%package  wayland
Summary:   Wayland support for %{name}
BuildArch: noarch
Requires:  %{name} = %{version}-%{release}
Requires:  plasma-workspace-wayland >= %{version}
# Transition users upgrading from F39 and before to the wayland session
Obsoletes: %{name}-x11 < %{version}-%{release}
Conflicts: %{name}-x11 < %{version}-%{release}

%description wayland
%{summary}



%description
%{summary}


%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake_kf6
%cmake_build


%install
%cmake_install
# F40: Remove the X11 Launcher
#rm -v %{buildroot}%{_kf6_bindir}/plasma-bigscreen-x11
#rm -v %{buildroot}%{_kf6_datadir}/xsessions/plasma-bigscreen-x11.desktop
%find_lang plasma-bigscreen --with-man --with-qt --all-name

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/kcm_mediacenter_{audiodevice,bigscreen_settings,kdeconnect,wifi}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%{buildroot}/usr/bin/*
%{buildroot}/usr/lib/debug/usr/bin/*
%{buildroot}/usr/lib/debug/usr/lib64/qt6/plugins/plasma/*
%{buildroot}/usr/lib/debug/usr/lib64/qt6/qml/org/kde/bigscreen/*
%{buildroot}/usr/lib64/qt6/plugins/plasma/applets/*
%{buildroot}/usr/lib64/qt6/plugins/plasma/kcms/systemsettings/*
%{buildroot}/usr/lib64/qt6/qml/org/kde/bigscreen/*
%{buildroot}/usr/share/applications/*
%{buildroot}/usr/share/metainfo/*
%{buildroot}/usr/share/plasma/look-and-feel/org.kde.plasma.bigscreen/contents/*
%{buildroot}/usr/share/plasma/look-and-feel/org.kde.plasma.bigscreen/*
%{buildroot}/usr/share/plasma/plasmoids/org.kde.bigscreen.homescreen/contents/*
%{buildroot}/usr/share/plasma/plasmoids/org.kde.bigscreen.homescreen/*
%{buildroot}/usr/share/plasma/shells/org.kde.plasma.bigscreen/contents/*
%{buildroot}/usr/share/plasma/shells/org.kde.plasma.bigscreen/*

%files -f plasma-bigscreen.lang
%license LICENSES/*
%{_kf6_datadir}/sounds/plasma-bigscreen/
%{_kf6_datadir}/applications/kcm_mediacenter_*.desktop

%files wayland
%{_kf6_bindir}/plasma-bigscreen-wayland
%{_kf6_datadir}/wayland-sessions/plasma-bigscreen-wayland.desktop


%changelog
* Mon Jul 21 2025 Microwave <micro.mail88@gmail.com> - 6.4.80
- Rebuilt for Horizon's Project Fernsehen, as a bonus added polish translation fix by Microwave and his brother.

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.80~20240204.214319.046d404-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.80~20240204.214319.046d404-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 21 2024 Jan Grulich <jgrulich@redhat.com> - 5.27.80~20240204.214319.046d404-4
- Rebuild (qt6)

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 5.27.80~20240204.214319.046d404-3
- Rebuild (qt6)

* Mon Mar 18 2024 Steve Cossette <farchord@gmail.com> - 5.27.80~20240204.214319.046d404-2
- Building to accomodate new depend library sonames

* Mon Feb 05 2024 Steve Cossette <farchord@gmail.com> - 5.27.80~20240204.214319.046d404-1
- Updated to Qt6

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 05 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.9-1
- 5.27.9

* Sun Oct 15 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.8-1
- Update to 5.27.8

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.2-4
- Fixes on the spec file

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.2-3
- Add plasma-workspace requirements.

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.2-2
- Create wayland/x11 subpackages

* Wed Mar 01 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.2-1
- Update to 5.27.2

* Sun Jan 22 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.26.90-1
- Initial Package
