Name:           flashplayer
Version:        10.2
Release:        p3.1%{?dist}
Summary:        Adobe Flash player plugin

Group:          Applications/Internet
License:        Proprietary
URL:            http://labs.adobe.com/downloads/flashplayer10_square.html
Source0:        http://download.macromedia.com/pub/labs/flashplayer10/flashplayer10_2_p3_64bit_linux_111710.tar.gz

Requires:       firefox

%description
Adobe flash player plugin, 64 bit version


%prep
%setup -q -c %{name}-%{version}


%build
#nothing to do

%install
install -D -m 644 libflashplayer.so %{buildroot}/%{_libdir}/mozilla/plugins/libflashplayer.so

%clean


%files
%defattr(-,root,root,-)
%{_libdir}/mozilla/plugins/libflashplayer.so


%changelog
* Thu Dec 23 2010 build@rnd - 10.2-p3.1
- Initial packaging
