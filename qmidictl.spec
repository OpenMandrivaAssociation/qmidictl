Name:		qmidictl
Version:	0.6.1
Release:	%mkrel 1
Summary:	A MIDI Remote Controller via UDP/IP Multicast
License:	GPLv2+
Group:		Sound/Utilities
URL:		https://qmidictl.sourceforge.io/
Source0:	http://downloads.sourceforge.net/qmidictl/%{name}-%{version}.tar.gz
Patch0:		qmidictl-0.5.1-mga-fix-install-path.patch
BuildRequires:	desktop-file-utils
BuildRequires:	qttools5
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)

%description
QmidiCtl is a MIDI remote controller application that sends MIDI
data over the network, using UDP/IP multicast.

%prep
%setup -q
%autopatch -p1

%build
%configure2_5x \
	--enable-debug

%make_build

%install
%make_install

#menu
desktop-file-install \
  --remove-key="X-Osso-Type" \
  --remove-key="Version" \
  --remove-key="Encoding" \
  --add-category="X-Mageia-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS ChangeLog README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_iconsdir}/*/*/*/%{name}.png
%{_mandir}/man1/%{name}*.1*