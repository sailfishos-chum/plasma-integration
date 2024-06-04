%global kf5_version 5.105.0

Name:    opt-plasma-integration
Summary: Qt Platform Theme integration plugin for Plasma
Version: 5.27.4
Release: 2%{?dist}

# KDE e.V. may determine that future LGPL versions are accepted
License: LGPLv2 or LGPLv3
URL:     https://invent.kde.org/plasma/%{name}

Source0: %{name}-%{version}.tar.bz2

Patch1: 0001-Allow-to-use-without-X11-libs.patch

%{?opt_kf5_default_filter}

BuildRequires:  opt-kf5-rpm-macros
BuildRequires:  opt-extra-cmake-modules
BuildRequires:  wayland-devel
BuildRequires:  plasma-wayland-protocols-devel >= 1.6.0

BuildRequires:  opt-qt5-qtwayland-devel
BuildRequires:  opt-qt5-qtbase-devel
BuildRequires:  opt-qt5-qtquickcontrols2-devel
# Qt5PlatformSupport
BuildRequires: opt-qt5-qtbase-static

BuildRequires:  opt-kf5-kconfig-devel
BuildRequires:  opt-kf5-kconfigwidgets-devel
BuildRequires:  opt-kf5-kcoreaddons-devel
BuildRequires:  opt-kf5-ki18n-devel
BuildRequires:  opt-kf5-kiconthemes-devel
BuildRequires:  opt-kf5-kio-devel
BuildRequires:  opt-kf5-knotifications-devel
BuildRequires:  opt-kf5-kwidgetsaddons-devel
BuildRequires:  opt-kf5-kwindowsystem-devel
BuildRequires:  opt-kf5-kwayland

## TODO: verify this is needed, not 100% sure -- rex
BuildRequires: opt-qt5-qtbase-private-devel

%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires:  opt-kf5-kcompletion
Requires:  opt-kf5-kconfig-gui
Requires:  opt-kf5-kconfigwidgets
Requires:  opt-kf5-kcoreaddons
Requires:  opt-kf5-ki18n
Requires:  opt-kf5-kiconthemes
Requires:  opt-kf5-kjobwidgets
Requires:  opt-kf5-kio-gui
Requires:  opt-kf5-kio-file-widgets
Requires:  opt-kf5-kio-widgets
Requires:  opt-kf5-knotifications
Requires:  opt-kf5-kwidgetsaddons
Requires:  opt-kf5-kwindowsystem
Requires:  opt-kf5-kxmlgui
Requires:  opt-qt5-qtbase-gui
Requires:  opt-qt5-qtdeclarative
Requires:  opt-qt5-qtquickcontrols2
Requires:  opt-qt5-qtwayland

# BuildRequires:  plasma-breeze-devel >= %{majmin_ver}
# Requires:       plasma-breeze >= %{majmin_ver}
# Requires:       breeze-cursor-theme >= %{majmin_ver}
# Requires:       breeze-icon-theme
# Recommends:     plasma-workspace >= %{majmin_ver}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires: opt-qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

%_opt_cmake_kf5
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES
%{_opt_kf5_qtplugindir}/platformthemes/KDEPlasmaPlatformTheme.so
%{_opt_kf5_datadir}/kconf_update/fonts_*
%{_opt_qt5_plugindir}/platforminputcontexts/plasmaimplatforminputcontextplugin.so
%{_opt_kf5_datadir}/locale/

%files devel
%{_opt_kf5_includedir}/PlasmaKeyData/
%{_opt_qt5_libdir}/pkgconfig/plasma-key-data.pc
