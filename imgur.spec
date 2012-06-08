Name:           imgur
Version:        2
Release:        2%{?dist}
Summary:        Bash script to upload to imgur.com

Group:          Applications/Internet
License:        Public Domain
URL:            http://imgur.com/tools
Source0:        http://imgur.com/tools/imgurbash.sh
BuildArch:      noarch
Requires:       curl

%description
Bash script to upload images to imgur.com

%prep
#nothing to do

%build
#nothing to do

%install
install -D -m 755 %{_sourcedir}/imgurbash.sh %{buildroot}/%{_bindir}/%{name}

%clean
#nothind to do

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}


%changelog
* Fri Jun 08 2012 qmp <glang@lavabit.com> - 2-2
- Rebuild for f17

* Sun Dec 26 2010 build@rnd - 2-1
- Initial packaging
