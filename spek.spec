#Built for rpmfusion-free
Name:           spek
Version:        0.6
Release:        1%{?dist}
Summary:        Spectrum analyzer
Group:          Applications/Multimedia
License:        GPLv3
URL:            http://www.spek-project.org/
Source0:        http://spek.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildRequires:  gtk2-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  intltool
BuildRequires:  desktop-file-utils

%description
Spek helps to analyze your audio files by showing their spectrogram.
Spectrograms are used to analyze the quality of audio files, you can easily
detect lossy re-encodes, web-rips and other badness by just looking at the
spectrogram. 
%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} INSTALL="install -p" CP="cp -p" install
#Used to add missing semicolons in the desktop file
desktop-file-install \
 --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%defattr(-,root,root,-)
#Don't include the empty README
%doc COPYING AUTHORS NEWS INSTALL
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*/*/apps/%{name}.*

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
* Tue Sep 21 2010 build@rnd - 0.6-1
- Initial packaging
