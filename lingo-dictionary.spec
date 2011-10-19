#snapshot from lp:lingo-dictionary
%define revision 94
Name:           lingo-dictionary
Version:        0
Release:        r%{revision}.2%{?dist}
Summary:        The sexiest dictionary on Earth and Jupiter.

License:        GPLv3
URL:            http://elementaryos.org/
Source0:        lingo-dictionary-r%{revision}.tar.bz2

BuildRequires:  vala-devel
BuildRequires:  cmake
BuildRequires:  libgee-devel
BuildRequires:  gtk3-devel
BuildRequires:  json-glib-devel
BuildRequires:  sqlite-devel
BuildRequires:  libsoup-devel
BuildRequires:  libgranite-devel
BuildRequires:  desktop-file-utils

%description
Lingo is a dictionary application using the web to provides accurate
definitions.


%prep
%setup -q -n %{name}-r%{revision}
#TODO : patch desktop file ...
#desktop-file-validate data/lingo.desktop


%build
%cmake .
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc AUTHORS COPYING
%{_bindir}/lingo
%{_datadir}/applications/lingo.desktop
%{_datadir}/glib-2.0/schemas/apps.lingo.gschema.xml

%post
update-desktop-database &> /dev/null || :
if [ $1 -eq 1 ]; then
	glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%postun
update-desktop-database &> /dev/null || :
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%changelog
* Wed Oct 19 2011 qmp <glang@lavabit.com> - 0-r94.2
- Compile glib schemas

* Wed Oct 19 2011 qmp <glang@lavabit.com> - 0-r94.1
- Initial packaging
