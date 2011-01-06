#TODO: themes
Summary: A real time network traffic statistic tool
Name: slurm
Version: 0.3.3
Release: 1%{?dist}
URL: http://web.archive.org/web/20080304085911/http://www.wormulon.net/slurm
Source0: http://downloads.openwrt.org/sources/%{name}-%{version}.tar.gz
License: GPLv2+
Group: Applications/System
BuildRequires: ncurses-devel

%description
slurm started as a pppstatus port to FreeBSD. Features:

* real time traffic statistics divided into incoming and outgoing
* optional combined view
* can monitor any kind of network interface (testers welcome!)
* shows detailed statistics about the interface.
* contact me if you need anything else. 

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}
gzip %{name}.1

%install
make DESTDIR=%{buildroot} INSTALL="install -p" CP="cp -p" install
install -p -D -m 644 %{name}.1.gz %{buildroot}/%{_mandir}/man1/%{name}.1.gz

%clean
#nothing to do

%files
%defattr(-,root,root)
%doc ChangeLog README KEYS TODO THANKS COPYRIGHT AUTHORS THEMES.txt
%doc COPYING FAQ INSTALL
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
* Wed Dec 29 2010 build@rnd - 0.3.3-1
- New upstream release
- spec cleanup

* Thu May 15 2003 Ralf Ertzinger <ertzinger@skytale.net>
- Initial RPM build

# end of file
