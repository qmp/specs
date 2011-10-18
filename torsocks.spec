Name:           torsocks
Version:        1.1
Release:        4%{?dist}
Summary:        A transparent socks proxy for use with tor

License:        GPLv2
URL:            http://code.google.com/p/torsocks/
Source0:        http://torsocks.googlecode.com/files/%{name}-1.1.tar.gz
Patch0:         torsocks.libdir.patch

%description
Torsocks allows you to use most socks-friendly applications in a safe way with
Tor. It ensures that DNS requests are handled safely and explicitly rejects UDP
traffic from the application you're using. 


%prep
%setup -q
%patch0 -p1


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc ChangeLog FAQ COPYING INSTALL README README.TORDNS TODO
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_bindir}/usewithtor
%{_libdir}/%{name}/
%{_datadir}/man/man1/%{name}.1.gz
%{_datadir}/man/man1/usewithtor.1.gz
%{_datadir}/man/man5/%{name}.conf.5.gz
%{_datadir}/man/man8/%{name}.8.gz



%changelog
*Tue Oct 18 2011 qmp <glang@lavabit.com> - 1.1-4
- Removed ifarch

*Mon Oct 17 2011 qmp <glang@lavabit.com> - 1.1-3
- Correct libdir

*Mon Oct 17 2011 qmp <glang@lavabit.com> - 1.1-2
- Correct libdir

*Mon Oct 17 2011 qmp <glang@lavabit.com> - 1.1-1
- Initial packaging
