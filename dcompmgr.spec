Name:           dcompmgr
Version:        0.20110527
Release:        1%{?dist}
Summary:        Alternative to xcompmgr

License:        Unknown
URL:            http://git.openbox.org/?p=dana/dcompmgr.git;a=summary
Source0:        dcompmgr-0.20110527.tar.bz2


%description
Alternative to xcompmgr. Used to have transparency and fade effect.


%prep
%setup -q

%build
make 


%install
%{__install} -D -m0755 %{name} %{buildroot}/%{_bindir}/%{name}


%files
%{_bindir}/%{name}


%changelog
* Fri May 27 2011 qmp <glang@lavabit.com> - 0.20110527
- Initial packaging
