Name:           ix
Version:        0.4
Release:        1%{?dist}
Summary:        Client for the ix.io pastebin

Group:          Applications/Internet
License:        Unknown
URL:            http://ix.io
Source0:        http://ix.io/client
BuildArch:      noarch
Requires:       python

%description
Client for the ix.io pastebin


%prep
#nothing to do

%build
#nothing to do

%install
install -D -m 755 %{_sourcedir}/client %{buildroot}/%{_bindir}/%{name}

%clean


%files
%defattr(-,root,root,-)
%{_bindir}/%{name}


%changelog
* Sun Dec 26 2010 build@rnd - 0.4-1
- Initial packaging
