Summary:	A MIDI Remote Controller via UDP/IP Multicast
Name:	qmidictl
Version:	1.0.2
Release:	1
License:	GPLv2+
Group:	Sound
Url:	https://qmidictl.sourceforge.io/
Source0:	https://downloads.sourceforge.net/qmidictl/%{name}-%{version}.tar.gz
BuildRequires:	desktop-file-utils
BuildRequires:	cmake
BuildRequires:	qmake-qt6
BuildRequires:	qt6-qtbase-theme-gtk3
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core) >= 6.8
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	pkgconfig(xkbcommon-x11)

%description
QmidiCtl is a MIDI remote controller application that sends MIDI data over
the network, using UDP/IP multicast.

%files
%doc ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/org.rncbc.%{name}.desktop
%{_datadir}/metainfo/org.rncbc.%{name}.metainfo.xml
%{_iconsdir}/hicolor/32x32/apps/org.rncbc.%{name}.png
%{_iconsdir}/hicolor/scalable/apps/org.rncbc.%{name}.svg
%{_mandir}/man1/%{name}*.1*
%{_mandir}/*/man1/%{name}.1.*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%cmake -DCONFIG_QT6=yes

%make_build


%install
%make_install -C build

# Fix .desktop file
desktop-file-edit \
	--remove-key="X-Osso-Type" \
	--remove-key="Version" \
	--remove-key="Encoding" \
	--add-category="X-OpenMandriva-CrossDesktop" \
	%{buildroot}%{_datadir}/applications/org.rncbc.%{name}.desktop
