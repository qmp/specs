#requires x264-libs from rpmfusion
Name:           kazam
Version:        1.3.0
Release:        2%{?dist}
Summary:        A screencasting program created with design in mind

License:        GPLv3
URL:            https://launchpad.net/kazam
Source0:        %{name}-%{version}.tar.gz
Patch0:         kazam.usrmove.patch

BuildArch:      noarch
BuildRequires:  python-distutils-extra
BuildRequires:  python2-devel
BuildRequires:  intltool
#BuildRequires:  desktop-file-utils
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
%setup -q -n %{name}-%{version}-0ubuntu1
%patch0 -p1


%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
#%{__rm} -rf %{buildroot}/%{_datadir}/locale/kazam*
# desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop



%files
%doc AUTHORS COPYING COPYING.LGPL README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}
%{python_sitelib}/%{name}
%{python_sitelib}/*egg-info


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
* Fri Jun 08 2012 qmp <glang@lavabit.com> - 1.3.0-2
- Fix symlink problem (/bin -> /usr/bin)
* Fri Jun 08 2012 qmp <glang@lavabit.com> - 1.3.0-1
- New upstream version
- Disable check for the desktop file
- Disable i18n

* Mon Jun 13 2011 qmp <glang@lavabit.com> - 0-unstable.r103.1
- Add : %{name}.desktop
- Add : icons

* Mon Jun 13 2011 qmp <glang@lavabit.com> - 0-stable.r100.1
- Initial packaging
