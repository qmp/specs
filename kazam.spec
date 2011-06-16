#snapshot from lp:kazam/stable r100
#requires x264-libs from rpmfusion
%define revision r103
%define branch unstable
Name:           kazam
Version:        0
Release:        %{branch}.%{revision}.1%{?dist}
Summary:        A screencasting program created with design in mind

License:        GPLv3
URL:            https://launchpad.net/kazam
Source0:        kazam-%{version}.%{branch}.%{revision}.tar.bz2

BuildArch:      noarch
BuildRequires:  python-distutils-extra
BuildRequires:  python2-devel
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
Requires:       pyxdg
Requires:       pygtk2
Requires:       pycairo
Requires:       gnome-python2-rsvg
Requires:       python-keybinder
Requires:       python-xlib
Requires:       ffmpeg
Requires:       gnome-python2-gnomedesktop
Requires:       python-gdata
Requires:       python-pycurl

%description
Easy to use application for recording on-screen action A program that
lets you record action on-screen into one video file.  It's special
features include a well designed interface, the ability to record
audio playing on your computer and built-in exporting capabilities to
upload screencasts to popular videosharing websites - such as YouTube.

%prep
%setup -q -n kazam-%{version}.%{branch}.%{revision}


%build
#%{__python} setup.py build


%install
%{__python} setup.py install --root $RPM_BUILD_ROOT
%{__rm} -rf %{buildroot}/%{_datadir}/locale/kazam*
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING COPYING.LGPL README TODO VIDEO_STUFF
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*/*/apps/%{name}.*
%{_datadir}/icons/*/*/apps/youtube.*
%{_datadir}/icons/*/*/status/%{name}*
%{python_sitelib}/kazam-0.1-py2.7.egg-info
%{python_sitelib}/%{name}


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
* Mon Jun 13 2011 qmp <glang@lavabit.com> - 0-unstable.r103.1
- Add : %{name}.desktop
- Add : icons

* Mon Jun 13 2011 qmp <glang@lavabit.com> - 0-stable.r100.1
- Initial packaging
