#checked out from svn
%global alphatag 20110512

Name:           aircrack-ng
Version:        1.1
Release:        %{alphatag}svn.1%{?dist}
Summary:        802.11 (wireless) sniffer and WEP/WPA-PSK key cracker

Group:          Applications/System

License:        GPLv2+
URL:            http://www.aircrack-ng.org/
Source0:        aircrack-ng-%{version}-%{alphatag}.tar.gz
Patch0:         aircrack-ng-parallel_make.patch
Patch1:         aircrack-ng.oui_path.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  sqlite-devel openssl-devel


%description
aircrack-ng is a set of tools for auditing wireless networks. It's an
enhanced/reborn version of aircrack. It consists of airodump-ng (an 802.11
packet capture program), aireplay-ng (an 802.11 packet injection program),
aircrack (static WEP and WPA-PSK cracking), airdecap-ng (decrypts WEP/WPA
capture files), and some tools to handle capture files (merge, convert, etc.).


%prep
%setup -q -n aircrack-ng-%{version}-%{alphatag}
%patch0 -p1 -b .parallel_make
%patch1 -p1 -b .oui-path


%build
#grep '(hex') %{SOURCE4} > airodump-ng-oui.txt
# License unclear
touch airodump-ng-oui.txt
#touch --reference %{SOURCE4} airodump-ng-oui.txt

export CFLAGS=$RPM_OPT_FLAGS
# unstable=true needed for wesside-ng, easside-ng, buddy-ng and tkiptun-ng
# (also needed in make install)
make %{?_smp_mflags} sqlite=true unstable=true


%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} mandir=%{_mandir}/man1 sqlite=true unstable=true
install -p -m 644 -D airodump-ng-oui.txt  $RPM_BUILD_ROOT%{_sysconfdir}/aircrack-ng/airodump-ng-oui.txt


#%check
#make check

# WEP checks, that are not wanted by upstream:
# http://trac.aircrack-ng.org/ticket/533
#cp %{SOURCE2} test/ptw.cap
#cp %{SOURCE3} test/test.ivs
#src/aircrack-ng -K -b 00:11:95:91:78:8C -q test/test.ivs | grep 'KEY FOUND! \[ AE:5B:7F:3A:03:D0:AF:9B:F6:8D:A5:E2:C7 \]'
#src/aircrack-ng -q -e Appart -z test/ptw.cap | grep 'KEY FOUND! \[ 1F:1F:1F:1F:1F \]'


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog LICENSE README VERSION test/ patches/
%{_bindir}/aircrack-ng
%{_bindir}/airdecap-ng
%{_bindir}/airdecloak-ng
%{_bindir}/airolib-ng
%{_bindir}/buddy-ng
%{_bindir}/ivstools
%{_bindir}/kstats
%{_bindir}/makeivs-ng
%{_bindir}/packetforge-ng
%{_sbindir}/airbase-ng
%{_sbindir}/airdriver-ng
%{_sbindir}/aireplay-ng
%{_sbindir}/airmon-ng
%{_sbindir}/airmon-zc
%{_sbindir}/airodump-ng
%{_sbindir}/airodump-ng-oui-update
%{_sbindir}/airserv-ng
%{_sbindir}/airtun-ng
%{_sbindir}/easside-ng
%{_sbindir}/tkiptun-ng
%{_sbindir}/besside-ng
%{_sbindir}/wesside-ng
%{_mandir}/man1/airbase-ng.1*
%{_mandir}/man1/aircrack-ng.1*
%{_mandir}/man1/airdecap-ng.1*
%{_mandir}/man1/airdecloak-ng.1*
%{_mandir}/man1/airdriver-ng.1*
%{_mandir}/man1/aireplay-ng.1*
%{_mandir}/man1/airmon-ng.1*
%{_mandir}/man1/airodump-ng.1*
%{_mandir}/man1/airolib-ng.1*
%{_mandir}/man1/airserv-ng.1*
%{_mandir}/man1/airtun-ng.1*
%{_mandir}/man1/buddy-ng.1*
%{_mandir}/man1/easside-ng.1*
%{_mandir}/man1/ivstools.1*
%{_mandir}/man1/kstats.1*
%{_mandir}/man1/makeivs-ng.1*
%{_mandir}/man1/packetforge-ng.1*
%{_mandir}/man1/tkiptun-ng.1*
%{_mandir}/man1/wesside-ng.1*
%dir %{_sysconfdir}/aircrack-ng
%config(noreplace) %{_sysconfdir}/aircrack-ng/airodump-ng-oui.txt


%changelog
* Thu May 12 2011 qmp <glang@lavabit.com> - 1.1-20110512svn.1
- svn snapshot

* Sat Jun 26 2010 Till Maas <opensource@till.name> - 1.1-1
- Update to new release
- remove upstream patches and patches from upstream

* Sat May 29 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 1.0-3
- CVE-2010-1159 aircrack-ng: remote denial of service, RH Bug #582416

* Sun Mar 28 2010 Till Maas <opensource@till.name> - 1.0-2
- Include patch against eapol overflow from upstream, RH Bug #577654

* Wed Sep 16 2009 Till Maas <opensource@till.name> - 1.0-1
- Update to stable release
- Include airodump-ng-oui-update
- prepare shipping of oui database
- fix paths for oui database in airodump-ng-oui-update and airodump-ng
- add missing #include <types.h>

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.0-0.10.rc3
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.9.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 13 2009 Till Maas <opensource@till.name> - 1.0-0.8.rc3
- Update to new release
- Enable patch to make parallel make work on x86_64

* Tue Feb 24 2009 Till Maas <opensource@till.name> - 1.0-0.7.20090224svn
- Update to new svn snapshot to make it compile again

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.20081109svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 09 2008 Till Maas <opensource@till.name> - 1.0-0.5.20081109svn
- Update to new svn snapshot

* Sun Nov 09 2008 Till Maas <opensource@till.name> - 1.0-0.4.20081109svn
- Update to new svn snapshot

* Sat Nov 08 2008 Till Maas <opensource@till.name> - 1.0-0.3.20081108svn
- Update to new svn snapshot that fixes some issues with tkiptun-ng

* Fri Nov 07 2008 Till Maas <opensource@till.name> - 1.0-0.2.20081107svn
- Update to current svn snapshot
- remove gz suffix from manpages
- add new airdecloack-ng tool
- remove partly upstreamed patch

* Fri Oct 31 2008 Till Maas <opensource@till.name> - 1.0-0.1.20081031svn
- Update to current svn snapshot
- Add sqlite-devel BR and add airolib-ng
- Add patch to do some testing of aircrack-ng
- Add openssl-devel BR

* Sat Mar 01 2008 Till Maas <opensource till name> - 0.9.3-1
- update to latest version
- remove patch that was merged upstream

* Wed Feb 13 2008 Till Maas <opensource till name> - 0.9.2-1
- update to latest version
- remove patch that was merged upstream
- add aircrack-ng-0.9.2-include_limits.patch

* Thu Aug 23 2007 Till Maas <opensource till name> - 0.9.1-2
- rebuild because of broken ppc32 package
- update License Tag
- fix some bugs in aireplay-ng.c

* Thu Jun 28 2007 Till Maas <opensource till name> - 0.9.1-1
- update to latest version

* Sun May 14 2007 Till Maas <opensource till name> - 0.9-1
- update to latest version

* Sun May 06 2007 Till Maas <opensource till name> - 0.8-2
- fix disttag

* Sun May 06 2007 Till Maas <opensource till name> - 0.8-1
- update to latest version

* Thu Apr 12 2007 Till Maas <opensource till name> - 0.8-0.2.20070417svn
- some more bugfixes

* Thu Apr 12 2007 Till Maas <opensource till name> - 0.8-0.1.20070413svn
- update to 0.8
- fixes http://archives.neohapsis.com/archives/fulldisclosure/2007-04/0408.html
  (remote code execution)
- fix race condition in %%install

* Wed Feb 21 2007 Till Maas <opensource till name> - 0.7-1
- initial spec for fedora
