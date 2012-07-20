%global githash db3873b17e
%global gitdate 20120716
Name:           hotot
Version:        0.9.8.7
Release:        1.%{gitdate}git%{githash}%{?dist}
Summary:        Lightweight & open source micro blogging client
Group:          Applications/Internet
License:        LGPLv3+ and LGPLv3 and BSD and GPLv2
URL:            http://hotot.org

Source0:        hotot-%{version}-%{githash}.tar.xz
BuildArch:      noarch
BuildRequires:  webkitgtk3-devel
BuildRequires:  gtk3-devel
BuildRequires:  python-devel
BuildRequires:  cmake
BuildRequires:  intltool
BuildRequires:  desktop-file-utils

%description
Hotot, is a lightweight & open source micro blogging client, coding using 
Python language and designed for Linux.  It depends less but supports more. 

Features:
   * OAuth and Basic Auth is supported.
   * Socks Proxy and Http Proxy.
   * Support API Proxy.
   * Support Twitter Search and content filter.
   * Keyboard shortcuts.
   * Extension System.
   * Native notify system. it supports Gnome & KDE SC. 

%prep
%setup -q -n shellex-Hotot-%{githash}
sed -i -e '/^#!\//, 1d'  hotot/*.py

%build
mkdir build
pushd build
%cmake -DWITH_GIR=on -DWITH_QT=off -DWITH_KDE=off ..
popd


%install
pushd build
make DESTDIR=%{buildroot} install
mv %{buildroot}/usr/lib64 %{buildroot}/usr/lib
popd
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog SPONSERS README.md
%{_bindir}/%{name}
%{python_sitelib}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/status/%{name}*.svg

%changelog
* Mon Jul 16 2012 qmp <glang@lavabit.com> - 0.9.8.7-1.20120716gitdb3873b17e
- New upstream git version
- Use cmake instead of setup.py

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-2.20111121gitfe857cb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 21 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.9.7-1.20111121gitfe857cb
- update to 0.9.7 snapshot
- spec update from Willington Vega <wvega@wvega.com>

* Mon Aug 15 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.9.6-2.20110815hg
- update to 0.9.6 snapshot

* Sun Jul 23 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.9.6-1.20110717hg
- update to 0.9.6 snapshot
- Spec update from Heiko Adams <fedora-updates@heiko-adams.de>

* Fri Apr 01 2011 Rahul Sundaram  <sundaram@fedoraproject.org> - 0.9.5-3.20110331hg
- Fix permissions for a couple of javascript files

* Thu Mar 31 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.9.5-2.20110331hg
- Adding missing build requires
- Include additional licensing info
- Make package noarch

* Thu Mar 31 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.9.5-1.20110331hg
- Initial release
- Based on the spec from upstream

