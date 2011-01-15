#Based on http://aur.archlinux.org/packages/firefox-extension-gnome-keyring-git/firefox-extension-gnome-keyring-git/PKGBUILD
#Source created with :
#git clone https://github.com/mdlavin/firefox-gnome-keyring.git
#git archive --prefix=firefox-gnome-keyring/ master | gzip >firefox-extension-gnome-keyring-20101223.tar.gz
%global alphatag 20110115
%global gitname firefox-gnome-keyring
Name:           mozilla-extension-gnome-keyring
Version:        0.4
Release:        %{alphatag}git.1%{?dist}
Summary:        Gnome keyring integration for firefox and thunderbird

Group:          Applications/Internet
License:        MPLv1.1
URL:            https://github.com/mdlavin/firefox-gnome-keyring
Source0:        firefox-extension-gnome-keyring-%{alphatag}.tar.gz

BuildRequires:  libgnome-keyring-devel
BuildRequires:  xulrunner-devel
Requires:       mozilla-filesystem
Conflicts:      firefox-extension-gnome-keyring

%description
This extension replaces the default password manager in both Firefox and
Thunderbird with an implementation which stores the passwords in Gnome keyring.

This allows for safe storage of passwords without prompting for password after
Firefox or Thunderbird has been started.



%prep
%setup -q -n %{gitname}


%build
make build %{?_smp_mflags}


%install
#Todo : install to mozilla filesystem
install -D -m 644 xpi/install.rdf \
 %{buildroot}/%{_libdir}/mozilla/extensions/{6f9d85e0-794d-11dd-ad8b-0800200c9a66}/install.rdf
install -D -m 755 libgnomekeyring.so \
 %{buildroot}/%{_libdir}/mozilla/extensions/{6f9d85e0-794d-11dd-ad8b-0800200c9a66}/platform/Linux_x86_64-gcc3/components/libgnomekeyring.so

%clean


%files
%defattr(-,root,root,-)
%doc README COPYING
%{_libdir}/mozilla/extensions/{6f9d85e0-794d-11dd-ad8b-0800200c9a66}
%{_libdir}/mozilla/extensions/{6f9d85e0-794d-11dd-ad8b-0800200c9a66}/install.rdf
%{_libdir}/mozilla/extensions/{6f9d85e0-794d-11dd-ad8b-0800200c9a66}/platform
%{_libdir}/mozilla/extensions/{6f9d85e0-794d-11dd-ad8b-0800200c9a66}/platform/Linux_x86_64-gcc3
%{_libdir}/mozilla/extensions/{6f9d85e0-794d-11dd-ad8b-0800200c9a66}/platform/Linux_x86_64-gcc3/components
%{_libdir}/mozilla/extensions/{6f9d85e0-794d-11dd-ad8b-0800200c9a66}/platform/Linux_x86_64-gcc3/components/libgnomekeyring.so


%changelog
* Sat Jan 15 2011 build@rnd - 0.4.20110115git.1
- Change name to mozilla-extension-gnome-keyring
- Use mozilla-filesystem

* Wed Dec 23 2010 build@rnd - 0.4-1.20101223git
- Initial packaging
