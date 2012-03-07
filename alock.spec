%define svn_rev 94
Name:           alock
Version:        0.%{svn_rev}
Release:        1%{?dist}
Summary:        A simple screen locker

License:        MIT
URL:            http://code.google.com/p/alock/
Source0:        http://alock.googlecode.com/files/alock-svn-%{svn_rev}.tar.bz2

BuildRequires:  pam-devel
BuildRequires:  imlib2-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXpm-devel
BuildRequires:  xmlto
BuildRequires:  xorg-x11-proto-devel

%description
alock locks the X server until the user enters a password via the keyboard. If
the authentification was successful the X server is unlocked and the user can
continue to work. 


%prep
%setup -q -n %{name}-svn-%{svn_rev}


%build
%configure --prefix %{_prefix}\
           --with-xrender --with-xcursor --with-imlib2 --with-xpm --with-pam\
           --with-hash
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/%{name}



%changelog
* Wed Mar 07 2012 qmp <glang@lavabit.com> 0.94-1
- Initial packaging for fedora
