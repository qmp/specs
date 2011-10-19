#snapshot of lp:granite
%define revision 90
%define short_name granite
Name:           libgranite
Version:        0
Release:        r%{revision}.1%{?dist}
Summary:        An extension of GTK

License:        GPLv3
URL:            http://elementaryos.org/
Source0:        %{short_name}-r%{revision}.tar.bz2
Patch0:         libgranite.libdir.patch

BuildRequires:  vala-devel
BuildRequires:  gtk3-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  glib2-devel

%description
Granite is an extension of GTK. Among other things, it provides the
commonly-used widgets such as modeswitchers, welcome screens, AppMenus, search
bars, and more found in elementary apps.


%prep
%setup -q -n %{short_name}-r%{revision}
%patch0 -p1


%build
mkdir build
pushd build
%cmake ..
make %{?_smp_mflags}
popd


%install
pushd build
make install DESTDIR=%{buildroot}
popd

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING COPYRIGHT
%{_libdir}/lib*.so.*
%{_libdir}/girepository-1.0/Granite-0.1.typelib
%{_datadir}/%{short_name}/
%{_datadir}/locale/*/LC_MESSAGES/granite.mo
%{_datadir}/vala/vapi/%{short_name}*

%package devel
Summary:        Header files for libgranite
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
Granite is an extension of GTK. Among other things, it provides the
commonly-used widgets such as modeswitchers, welcome screens, AppMenus, search
bars, and more found in elementary apps.

This package contains the header files

%files devel
%{_includedir}/%{short_name}/
%{_libdir}/pkgconfig/%{short_name}.pc
%{_libdir}/*.so
%{_datadir}/gir-1.0/Granite-0.1.gir


%changelog
* Wed Oct 19 2011 qmp <glang@lavabit.com> - 0-r90.1
- Initial packaging
