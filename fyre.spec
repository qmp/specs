Name:      fyre
Summary:   gtk2-based explorer for iterated chaotic functions
Requires:  OpenEXR
BuildRequires:  gtk2-devel gnet2-devel OpenEXR-devel libglade2-devel desktop-file-utils
Version:   1.0.1
Release:   1%{?dist}
License:   GPLv2
Vendor:    David Trowbridge <trowbrds@cs.colorado.edu> Micah Dowty <micah@navi.cx>
Group:     System Environment/Libraries
Source:    http://releases.navi.cx/fyre/%{name}-%{version}.tar.bz2
URL:       http://fyre.navi.cx

%description
Fyre is a tool for producing computational artwork based on histograms
of iterated chaotic functions. At the moment, it implements the Peter
de Jong map in a fixed-function pipeline with an interactive GTK+
frontend and a command line interface for easy and efficient rendering
of high-resolution, high quality images.

%prep
%setup -q

%build
./configure --prefix=/usr --libdir=%{_libdir} --enable-gnet --enable-openexr
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean

%post
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
update-mime-database %{_datadir}/mime || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%{_bindir}/fyre
%{_datadir}/applications/%{name}.desktop
%{_datadir}/fyre/*
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-%{name}-animation.png
%{_datadir}/mime/packages/%{name}.xml

%changelog
* Sun Aug 28 2011 Christophe Donatsch <cdonatsch@lavabit.com> 1.0.1-1
- New upstream version
- Update icon cache
- Update desktop database
- Fix license version
- Add doc
- Add BuildRequire for libglade2-devel
- Removed useless explicit require

* Fri Mar 04 2005 Mirco Mueller <macslow@bangang.de> 1.0.0-2
- stupid me, I totally forgot to enable gnet2 and OpenEXR support

* Thu Mar 03 2005 Mirco Mueller <macslow@bangang.de> 1.0.0-1
- initial .spec file written for fyre-1.0.0.tar.gz

