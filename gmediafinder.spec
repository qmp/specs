#Pulled from : git://github.com/smolleyes/gmediafinder.git
#git archive --format=tar --prefix=gmediafinder-0.9.7.5/ 678b032 | gzip > gmediafinder-0.9.7.5-678b032.tar.gz
%define githead 678b032

Name:           gmediafinder
Version:        0.9.7.5
Release:        2011.08.05%githead%{?dist}
Summary:        Media scanner for Google, skreemr.com, findmp3s.com, etc

License:        GPLv2
URL:            https://github.com/smolleyes/gmediafinder
Source0:        gmediafinder-%{version}-%{githead}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python-distutils-extra
BuildRequires:  python-setuptools
BuildRequires:  python-xlib
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
Requires:       pygtk2
Requires:       python-gdata
Requires:       gstreamer-python
Requires:       gstreamer-ffmpeg
Requires:       gstreamer-plugins-good
Requires:       python-configobj
Requires:       ffmpeg
Requires:       python-mechanize
Requires:       pygtk2-libglade

BuildArch:      noarch

%description
Web media browser for YouTube videos and some mp3 search engines websites for
the sounds You can stream or download files play in continue or loop mode and
download files too directly from the GUI.


%prep
%setup -q -n %{name}-%{version}
sed -i -e 's/Categories=AudioVideo/Categories=AudioVideo;/' %{name}.desktop


%build
%{__python} setup.py build


%install
%{__python} setup.py install --root %{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
#No idea what is this dir
rm -rf %{buildroot}/%{_datadir}/pyshared/

install -d %{buildroot}/%{_defaultdocdir}/%{name}-%{version}
install -D -m644 CHANGELOG %{buildroot}/%{_defaultdocdir}/%{name}-%{version}/
install -D -m644 TODO %{buildroot}/%{_defaultdocdir}/%{name}-%{version}/
install -D -m644 README %{buildroot}/%{_defaultdocdir}/%{name}-%{version}/
install -D -m644 VERSION %{buildroot}/%{_defaultdocdir}/%{name}-%{version}/

%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}
%{python_sitelib}/GmediaFinder
%{python_sitelib}/%{name}-%{version}*egg-info
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*/*/apps/%{name}.*
%{_defaultdocdir}/%{name}-%{version}
%{_defaultdocdir}/%{name}-%{version}/CHANGELOG
%{_defaultdocdir}/%{name}-%{version}/TODO
%{_defaultdocdir}/%{name}-%{version}/README
%{_defaultdocdir}/%{name}-%{version}/VERSION


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
* Fri Aug 05 2011 qmp <glang@lavabit.com> - 0.9.7.5-2011.08.05678b032
- Initial packaging
