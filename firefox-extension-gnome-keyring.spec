#Based on http://aur.archlinux.org/packages/firefox-extension-gnome-keyring-git/firefox-extension-gnome-keyring-git/PKGBUILD
#Source created with :
#git clone https://github.com/mdlavin/firefox-gnome-keyring.git
#git archive --prefix=firefox-gnome-keyring/ master | gzip >firefox-extension-gnome-keyring-20110307.tar.gz
%global alphatag 20110307
%global gitname firefox-gnome-keyring
Name:           firefox-extension-gnome-keyring
Version:        0.5
Release:        %{alphatag}git.1%{?dist}
Summary:        Gnome keyring integration for firefox

Group:          Applications/Internet
License:        MPLv1.1
URL:            https://github.com/mdlavin/firefox-gnome-keyring
Source0:        %{name}-%{alphatag}.tar.gz
Patch0:         %{name}-x86_64.patch

BuildRequires:  libgnome-keyring-devel
BuildRequires:  xulrunner-devel
#Todo : Requires: mozilla-filesystem
Requires:       firefox >= 4
ExclusiveArch:  x86_64

%description
This extension replaces the default password manager in both Firefox and
Thunderbird with an implementation which stores the passwords in Gnome keyring.

This allows for safe storage of passwords without prompting for password after
Firefox or Thunderbird has been started.



%prep
%setup -q -n %{gitname}
pushd %{_builddir}/%{gitname}/
rm -rf lib
popd
%patch0

%build
%ifarch x86_64
make build-library-x86_64 %{?_smp_mflags}
%endif


%install
#Todo : install to mozilla filesystem
install -D -m 644 xpi/chrome.manifest \
 %{buildroot}/%{_libdir}/firefox-4/extensions/{6f9d85e0-794d-11dd-ad8b-0800200c9a66}/chrome.manifest
install -D -m 644 xpi/install.rdf \
 %{buildroot}/%{_libdir}/firefox-4/extensions/{6f9d85e0-794d-11dd-ad8b-0800200c9a66}/install.rdf
install -D -m 755 xpi/platform/Linux_x86_64-gcc3/components/libgnomekeyring.so \
 %{buildroot}/%{_libdir}/firefox-4/extensions/{6f9d85e0-794d-11dd-ad8b-0800200c9a66}/platform/Linux_x86_64-gcc3/components/libgnomekeyring.so

%clean


%files
%defattr(-,root,root,-)
%doc README COPYING
#Todo : Use mozilla filesystem
%{_libdir}/firefox-4/extensions/{6f9d85e0-794d-11dd-ad8b-0800200c9a66}
%{_libdir}/firefox-4/extensions/{6f9d85e0-794d-11dd-ad8b-0800200c9a66}/chrome.manifest
%{_libdir}/firefox-4/extensions/{6f9d85e0-794d-11dd-ad8b-0800200c9a66}/install.rdf
%{_libdir}/firefox-4/extensions/{6f9d85e0-794d-11dd-ad8b-0800200c9a66}/platform
%{_libdir}/firefox-4/extensions/{6f9d85e0-794d-11dd-ad8b-0800200c9a66}/platform/Linux_x86_64-gcc3
%{_libdir}/firefox-4/extensions/{6f9d85e0-794d-11dd-ad8b-0800200c9a66}/platform/Linux_x86_64-gcc3/components
%{_libdir}/firefox-4/extensions/{6f9d85e0-794d-11dd-ad8b-0800200c9a66}/platform/Linux_x86_64-gcc3/components/libgnomekeyring.so


%changelog
* Wed Mar 09 2011 qmp <glang@lavabit.com> - 0.5-20110307git.1
- Include chrome manifest
- Do not build for the i386 platform
* Mon Mar 07 2011 qmp <glang@lavabit.com> - 0.4-2.20110307git
- New git snapshot
* Mon Jan 17 2011 build@rnd - 0.4-2.20101223git
- Add ownership of the extension's directory
* Wed Dec 23 2010 build@rnd - 0.4-1.20101223git
- Initial packaging
