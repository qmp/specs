Name:           flashplayer
Version:        11.0.r1.129
Release:        1%{?dist}
Summary:        Adobe Flash player plugin

Group:          Applications/Internet
License:        Proprietary
URL:            http://labs.adobe.com/downloads/flashplayer11.html
Source0:        http://download.macromedia.com/pub/labs/flashplatformruntimes/flashplayer11/flashplayer11_rc1_install_lin_64_090611.tar.gz
ExclusiveArch:  x86_64
Requires:       mozilla-filesystem
BuildRequires:  desktop-file-utils

%description
Adobe flash player plugin, 64 bit version


%prep
%setup -q -c %{name}-%{version}


%build
#nothing to do

%install
%{__install} -D -m 644 libflashplayer.so %{buildroot}/%{_libdir}/mozilla/plugins/libflashplayer.so
%{__install} -D -m 755 usr/bin/flash-player-properties %{buildroot}/%{_bindir}/flash-player-properties
for resolution in {"16x16","22x22","24x24","32x32","48x48"}
do
 %{__install} -D -m 644 usr/share/icons/hicolor/${resolution}/apps/flash-player-properties.png \
  %{buildroot}/%{_datadir}/icons/hicolor/${resolution}/apps/flash-player-properties.png
done

desktop-file-install \
 --dir=%{buildroot}%{_datadir}/applications \
usr/share/applications/flash-player-properties.desktop

%clean


%files
%defattr(-,root,root,-)
%{_bindir}/flash-player-properties
%{_libdir}/mozilla/plugins/libflashplayer.so
%{_datadir}/icons/hicolor/*/apps/flash-player-properties.png
%{_datadir}/applications/flash-player-properties.desktop

%post
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%changelog
* Thu Sep 22 2011 build@rnd - 11.0.r1.129
- New upstream version

* Sun Aug 21 2011 build@rnd - 11.0.1.98-0.beta.2
- New upstream version

* Thu Jul 14 2011 build@rnd - 11.0.1.60-0.beta.1
- New upstream version

* Mon Dec 27 2010 build@rnd - 10.2-p3.3
- ExclusiveArch: x86_64

* Fri Dec 24 2010 build@rnd - 10.2-p3.2
- Replace all memcpy calls with memmove calls in libflashplayer.so (#638477)

* Thu Dec 23 2010 build@rnd - 10.2-p3.1
- Initial packaging
