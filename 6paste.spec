Name:           6paste
Version:        0
Release:        1%{?dist}
Summary:        Client for p.6core.net pastebin

License:        Unknown
URL:            https://p.6core.net/about.html
Source0:        6paste

Requires:       curl
BuildArch:      noarch

%description
Client for p.6core.net pastebin

%prep
#nothing to do


%build
#nothing to do


%install
install -D -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}


%files
%{_bindir}/%{name}



%changelog
* Sat Jun 09 2012 qmp <glang@lavabit.com> - 0-1
- Initial packaging
