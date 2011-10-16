Name:           qmp-release
Version:        16
Release:        1
Summary:        Configuration files for qmp's repo

License:        BSD
URL:            http://qmp.net46.net
Source0:        qmp.repo
Source1:        RPM-GPG-KEY-qmp

Requires:       system-release >= %{version}
BuildArch:      noarch

%description
Configuration file for qmp's repo. Contains a few packages with patches not
suitable for fedora's repos.


%prep
#nothing to do


%build
#nothing to do


%install
%{__install} -d -m755 %{buildroot}%{_sysconfdir}/yum.repos.d
%{__install} -d -m755 %{buildroot}%{_sysconfdir}/pki/rpm-gpg
%{__install} -D -m644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/
%{__install} -D -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/

%files
#no %config : we want to overwrite each time
%{_sysconfdir}/yum.repos.d/qmp.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-qmp


%changelog
* Sat Oct 15 2011 qmp <glang@lavabit.com> - 16-1
- Bump to version 16

* Sun May 15 2011 qmp <glang@lavabit.com> - 15-1
- Initial packaging
