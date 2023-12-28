Name:		qmidictl
Version:	0.9.11
Release:	1
Summary:	A MIDI Remote Controller via UDP/IP Multicast
License:	GPLv2+
Group:		Sound/Utilities
URL:		https://qmidictl.sourceforge.io/
Source0:	https://downloads.sourceforge.net/qmidictl/%{name}-%{version}.tar.gz

BuildRequires:	desktop-file-utils
BuildRequires:	cmake
BuildRequires:	cmake(Qt6)
BuildRequires:	qmake-qt6
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6Core)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	qt6-qtbase-theme-gtk3
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(vulkan)

%description
QmidiCtl is a MIDI remote controller application that sends MIDI
data over the network, using UDP/IP multicast.

%prep
%autosetup -p1

%build
%cmake \
        -DCONFIG_QT6=yes

%make_build

%install
%make_install -C build

#menu
desktop-file-install \
  --remove-key="X-Osso-Type" \
  --remove-key="Version" \
  --remove-key="Encoding" \
  --add-category="X-OpenMandriva-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/hildon/org.rncbc.qmidictl.desktop

%files
%doc ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/hildon/org.rncbc.qmidictl.desktop
%{_datadir}/applications/qmidictl.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_iconsdir}/hicolor/*/hildon/qmidictl.png
%{_iconsdir}/hicolor/scalable/apps/qmidictl.svg
%{_mandir}/man1/%{name}*.1*
%{_mandir}/*/man1/qmidictl.1.*
