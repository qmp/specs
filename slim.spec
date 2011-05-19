Name:           slim
Version:        1.3.2
Release:        4.rnd.4%{?dist}
Summary:        Simple Login Manager

Group:          User Interface/X
License:        GPLv2+
URL:            http://slim.berlios.de/
Source0:        http://download.berlios.de/slim/%{name}-%{version}.tar.gz
# stolen from lxdm
Source5:        %{name}-lxdm.pam
# adapted from debian to use freedesktop
Source2:        slim-update_slim_wmlist
Source3:        slim-fedora.txt
# logrotate entry (see bz#573743)
Source4:        slim.logrotate.d
Source6:        slim-dotxinitrc.example
Source7:        slim.tmpfiles.d
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Fedora-specific patches
Patch0: 01-slim-1.3.2-make.patch
Patch1: 02-slim-1.3.2-fedora.patch
Patch3: 03-slim-1.3.2-var-run_transition.patch

BuildRequires:  libXmu-devel libXft-devel libXrender-devel
BuildRequires:  libpng-devel libjpeg-devel freetype-devel fontconfig-devel
BuildRequires:  pkgconfig gettext libselinux-devel pam-devel
BuildRequires:  xwd xterm /sbin/shutdown
Requires:       xwd xterm /sbin/shutdown
Requires:       %{_sysconfdir}/pam.d
# we use 'include' in the pam file, so
Requires:       pam >= 0.80
# reuse the images
Requires:       desktop-backgrounds-basic
# for anaconda yum
Provides:       service(graphical-login)

%description
SLiM (Simple Login Manager) is a graphical login manager for X11.
It aims to be simple, fast and independent from the various
desktop environments.
SLiM is based on latest stable release of Login.app by Per Lidén.

In the distribution, slim may be called through a wrapper, slim-dynwm,
which determines the available window managers using the freedesktop
information and modifies the slim configuration file accordingly,
before launching slim.

%prep
%setup -q
%patch0 -p1 -b .make
%patch1 -p1 -b .fedora
%patch3 -p0 -b .var-run
cp -p %{SOURCE3} README.Fedora
cp -p %{SOURCE6} xinitrc.example

%build
make %{?_smp_mflags} OPTFLAGS="$RPM_OPT_FLAGS" USE_PAM=1

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p' MANDIR=%{_mandir}

install -p -m755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/update_slim_wmlist

# do a slim wrapper which updates the window manager list before
# launching slim
cat > $RPM_BUILD_ROOT%{_bindir}/slim-dynwm << EOF
#!/bin/sh
update_slim_wmlist
if [ "x\$1" = "x-nodaemon" ]; then
  shift
  exec slim "\$@"
else
  slim -d "\$@"
fi
EOF

chmod 0755 $RPM_BUILD_ROOT%{_bindir}/slim-dynwm
chmod 0644 $RPM_BUILD_ROOT%{_sysconfdir}/slim.conf

install -d -m755 $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
install -p -m644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/slim

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/run/slim

# replace the background image
rm -f $RPM_BUILD_ROOT%{_datadir}/slim/themes/default/background.jpg
ln -s ../../../backgrounds/tiles/default_blue.jpg $RPM_BUILD_ROOT%{_datadir}/slim/themes/default/background.jpg

# install logrotate entry
install -m0644 -D %{SOURCE4} $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d/slim

install -m0644 -D %{SOURCE7} %{buildroot}%{_libdir}/../lib/tmpfiles.d/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog README* THEMES TODO xinitrc.example
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/pam.d/slim
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/slim.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/logrotate.d/slim
%{_libdir}/../lib/tmpfiles.d/slim.conf
%ghost %dir %{_var}/run/slim
%{_bindir}/slim*
%{_bindir}/update_slim_wmlist
%{_mandir}/man1/slim*.1*
%dir %{_datadir}/slim
%{_datadir}/slim/themes/


%changelog
* Thu May 19 2011 qmp <glang@lavabit.com> - 1.3.2-4.rnd.4
- Move tmpfiles.d config to /usr/lib/tmpfiles.d

* Thu May 19 2011 qmp <glang@lavabit.com> - 1.3.2-4.rnd.3
- Write to a xdm_var_run_t labeled directory : /run/slim

* Thu May 19 2011 qmp <glang@lavabit.com> - 1.3.2-4.rnd.2
- Add example file for .xinitrc

* Thu May 19 2011 qmp <glang@lavabit.com> - 1.3.2-4.rnd.1
- Removed /etc/tmpfiles.d/slim.conf
- Transition from /var/run to /run
- Don't listen on tcp socket
- Stoled pam configuration from lxdm :
  - Add pam_selinux_permit for auth
  - Add pam_gnome_keyring
  - Prevent root login
  - Add pam_selinux
  - Add pam_namepace

* Fri May 13 2011 qmp <glang@lavabit.com> - 1.3.2-4.rnd
- Add /etc/tmpfiles.d/slim.conf

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 24 2010 Petr Sabata <psabata@redhat.com> - 1.3.2-3
- /var/run/slim is now ghost'd, rhbz#656689

* Tue Aug 31 2010 Petr Sabata <psabata@redhat.com> - 1.3.2-2
- slim-update_wm_list script modification, rhbz#581518

* Sun Aug 22 2010 Lorenzo Villani <lvillani@binaryhelix.net> - 1.3.2-1
- New upstream version 1.3.2
- Drop slim-1.3.1-usexwd.patch (folded into 02-slim-1.3.2-fedora.patch)
- Drop slim-1.3.1-curdir.patch (folded into 02-slim-1.3.2-fedora.patch)
- Drop slim-1.3.1-strtol.patch (merged upstream)
- Drop slim-1.3.1-remove.patch (merged upstream)
- Drop slim-1.3.1-gcc44.patch (merged upstream)
- Drop slim-1.3.1-CVE-2009-1756.patch (merged upstream)
- Drop slim-1.3.1-fix-insecure-mcookie-generation.patch (merged upstream)

* Tue Mar 30 2010 Lorenzo Villani <lvillani@binaryhelix.net> - 1.3.1-13
- Missing /var/run/slim (Fix bz#573284)

* Mon Mar 29 2010 Lorenzo Villani <lvillani@binaryhelix.net> - 1.3.1-12
- Add logrotate.d file to work-around bz#573743

* Fri Feb 19 2010 Lorenzo Villani <lvillani@binaryhelix.net> - 1.3.1-11
- Refresh slim-1.3.1-selinux.patch to include fix for bz#561095

* Tue Dec 22 2009 Lorenzo Villani <lvillani@binaryhelix.net> - 1.3.1-9
- Fix CVE-2009-1756 (bugzilla: 544024)
- Fix MIT insecure cookie generation (patch from Debian)
- Fix build with GCC 4.4

* Sat Oct 10 2009 Lorenzo Villani <lvillani@binaryhelix.net> - 1.3.1-8
- Fix BZ #518068

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 21 2009 Anders F Bjorklund <afb@users.sourceforge.net> 1.3.1-6
- exclude current directory from default_path in slim.conf (#505359)

* Sat Feb 28 2009 Anders F Bjorklund <afb@users.sourceforge.net> 1.3.1-5
- provide service(graphical-login) for anaconda yuminstall (#485789)

* Sun Feb 22 2009 Anders F Bjorklund <afb@users.sourceforge.net> 1.3.1-4
- Add header for remove(3)

* Wed Feb 04 2009 Anders F Bjorklund <afb@users.sourceforge.net> 1.3.1-3
- use small "default_blue" background, instead of large compat "default"

* Wed Oct 15 2008 Marco Pesenti Gritti <mpg@redhat.com>  1.3.1-2
- Enable pam_selinux

* Thu Oct 09 2008 Marco Pesenti Gritti <mpg@redhat.com>  1.3.1-1
- Update to 1.3.1

* Sun Oct 05 2008 Anders F Bjorklund <afb@users.sourceforge.net> 1.3.0-7
- add compat req (#465631)

* Wed Sep 24 2008 Anders F Bjorklund <afb@users.sourceforge.net> 1.3.0-6
- fix patch fuzz

* Fri May 16 2008 Anders F Bjorklund <afb@users.sourceforge.net> 1.3.0-5
- all the images are now in desktop-backgrounds-basic

* Fri Feb 22 2008 Anders F Bjorklund <afb@users.sourceforge.net> 1.3.0-4
- add header for strtol(3)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3.0-3
- Autorebuild for GCC 4.3

* Sat Jan 19 2008 Anders F Bjorklund <afb@users.sourceforge.net> 1.3.0-2
- rebuild

* Mon Aug  6 2007 Anders F Bjorklund <afb@users.sourceforge.net> 1.3.0-1
- version upgrade

* Mon Aug  6 2007 Anders F Bjorklund <afb@users.sourceforge.net> 1.2.6-6
- require system-logos instead of fedora-logos (#250365)

* Tue May 22 2007 Anders F Bjorklund <afb@users.sourceforge.net> 1.2.6-5
- make sure to own datadir slim parent too

* Mon May 21 2007 Anders F Bjorklund <afb@users.sourceforge.net> 1.2.6-4
- use desktop background, instead of slim
- leave (unused) pam files in the package

* Mon May 14 2007 Anders F Bjorklund <afb@users.sourceforge.net>
- clean up spec file
- correct README user

* Sun May 13 2007 Anders F Bjorklund <afb@users.sourceforge.net> 1.2.6-3
- use slim background instead of default
- added more build dependencies / -devel
- add "README.Fedora"
- patch issue display

* Wed May 09 2007 Anders F Bjorklund <afb@users.sourceforge.net>
- clean up spec file
- noreplace slim.conf

* Tue May 08 2007 Anders F Bjorklund <afb@users.sourceforge.net> 1.2.6-2
- fixed source URL
- added libXft-devel
- removed xrdb dependency (left from wdm)
- added xwd dependency (for screenshots)

* Sun May 06 2007 Anders F Bjorklund <afb@users.sourceforge.net> 1.2.6-1
- initial package
- adopted wdm spec
