%define git_release 20111016
Name:           cairo-compmgr
Version:        0.3.0git%{git_release}
Release:        1%{?dist}
Summary:        A versatile and extensible composite manager

License:        GPLv2
URL:            http://cairo-compmgr.tuxfamily.org/
Source0:        %{name}-%{git_release}.tar.bz2

BuildRequires:  libXdamage-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libSM-devel
BuildRequires:  cairo-devel
BuildRequires:  pixman-devel
BuildRequires:  gtk2-devel
BuildRequires:  GConf2-devel
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  vala-devel


%description
Cairo Composite Manager is a versatile and extensible composite manager which
use cairo for rendering. Plugins can be used to add some cool effects to your
desktop.


%prep
%setup -q -n %{name}-%{git_release}


%build
./autogen.sh
%configure
make


%install
make install DESTDIR=%{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/\
%{name}.desktop


%files
%doc AUTHORS COPYING
%{_bindir}/%{name}
%{_bindir}/ccm-schema-key-to-gconf
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/man/man1/%{name}.1.gz
%{_datadir}/pixmaps/%{name}
%{_datadir}/vala/vapi/%{name}*
%{_libdir}/%{name}
%{_libdir}/libcairo_compmgr*

%post
/sbin/ldconfig
update-desktop-database &> /dev/null || :

%postun
/sbin/ldconfig
update-desktop-database &> /dev/null || :

%package devel
Summary:        Cairo-compmgr development files
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
Cairo Composite Manager is a versatile and extensible composite manager which
use cairo for rendering. Rendering can be done in 2D or 3D, using Xrender and
Glitz back-ends. Plug-ins can be used to add some cool effects to your desktop.

This package contains the development files.

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Sun Oct 16 2011 qmp <glang@lavabit.com> - 0.3.0git20111016-1
- Initial packaging
