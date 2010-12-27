#fix-flash.sh source : https://bugzilla.redhat.com/attachment.cgi?id=460254&action=edit
Name:           flashplayer
Version:        10.2
Release:        p3.3%{?dist}
Summary:        Adobe Flash player plugin

Group:          Applications/Internet
License:        Proprietary
URL:            http://labs.adobe.com/downloads/flashplayer10_square.html
Source0:        http://download.macromedia.com/pub/labs/flashplayer10/flashplayer10_2_p3_64bit_linux_111710.tar.gz
Patch0:         fix-flash.sh
ExclusiveArch:  x86_64
Requires:       mozilla-filesystem

%description
Adobe flash player plugin, 64 bit version


%prep
%setup -q -c %{name}-%{version}
%{_sourcedir}/fix-flash.sh %{_builddir}/%{name}-%{version}/libflashplayer.so


%build
#nothing to do

%install
install -D -m 644 libflashplayer.so %{buildroot}/%{_libdir}/mozilla/plugins/libflashplayer.so

%clean


%files
%defattr(-,root,root,-)
%{_libdir}/mozilla/plugins/libflashplayer.so


%changelog
* Mon Dec 27 2010 build@rnd - 10.2-p3.3
- ExclusiveArch: x86_64

* Fri Dec 24 2010 build@rnd - 10.2-p3.2
- Replace all memcpy calls with memmove calls in libflashplayer.so (#638477)

* Thu Dec 23 2010 build@rnd - 10.2-p3.1
- Initial packaging
