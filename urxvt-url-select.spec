#Based on http://aur.archlinux.org/packages/urxvt-url-select/urxvt-url-select/PKGBUILD
Name:           urxvt-url-select
Version:        1.5
Release:        1%{?dist}
Summary:        Copy and open URLs in rxvt-unicode using the keyboard

Group:          User Interface/X
License:        GPLv2
URL:            http://www.github.com/muennich/urxvt-perls
Source0:        https://github.com/downloads/muennich/urxvt-perls/url-select-%{version}.tar.gz
patch0:         url-select-interpreter.patch

Requires:       rxvt-unicode
BuildArch:	noarch

%define extension url-select

%description
This perl script for rxvt-unicode adds the ability to underline urls, select
them with the keyboard and open them in a browser.

%prep
%setup -q -n %{extension}-%{version}
%patch0


%build


%install
install -D -m 755 url-select %{buildroot}/%{_libdir}/urxvt/perl/url-select

%clean


%files
%defattr(-,root,root,-)
%{_libdir}/urxvt/perl/url-select


%changelog
* Fri Jun 08 2012 qmp <glang@lavbit.com> - 1.5-1
- New upstream version
- The extension variable is now local
- Set the executable bit

* Thu Dec 23 2010 build@rnd - 1.4-2
- Set buildarch to noarch

* Wed Dec 22 2010 build@rnd - 1.4-1
- Initial packaging
