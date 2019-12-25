Name:		qmidictl
Version:	0.6.1
Release:	1
Summary:	A MIDI Remote Controller via UDP/IP Multicast
License:	GPLv2+
Group:		Sound/Utilities
URL:		https://qmidictl.sourceforge.io/
Source0:	http://downloads.sourceforge.net/qmidictl/%{name}-%{version}.tar.gz

BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	qt5-qttools
BuildRequires:  qt5-qtchooser
BuildRequires:	qt5-linguist
BuildRequires:	qt5-linguist-tools
BuildRequires:  qmake5

%description
QmidiCtl is a MIDI remote controller application that sends MIDI
data over the network, using UDP/IP multicast.

%prep
%setup -q
%autopatch -p1

%build
%configure \
	--enable-debug

%make_build

%install
%make_install

#menu
desktop-file-install \
  --remove-key="X-Osso-Type" \
  --remove-key="Version" \
  --remove-key="Encoding" \
  --add-category="X-OpenMandriva-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/hildon/%{name}.desktop

%files
%doc AUTHORS ChangeLog README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_iconsdir}/hicolor/*/hildon/qmidictl.png
%{_mandir}/man1/%{name}*.1*
