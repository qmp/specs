Name:           gaphor
Version:        0.17.1
Release:        1%{?dist}
Summary:        A UML modelling tool.

License:        GPLv2
URL:            http://gaphor.sourceforge.net/index.php
#Source0:        http://pypi.python.org/packages/source/g/%{name}/%{name}-%{version}.tar.gz#md5=cf7b6e1f752913f19a69c7addcfe00d5
Source0:        %{name}-%{version}.tar.gz

Patch0:         %{name}.desktopfile.patch

BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  python2-devel

%description
Gaphor is a UML modelling tool, written in Python. This makes
it very easy to use (and very easy to extend -- and to write
;-) ).


%prep
%setup -q
%patch0 -p0


%build
%{__python} setup.py build
desktop-file-validate %{name}.desktop


%install
%{__python} setup.py install --root %{buildroot}
install -D %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%doc AUTHORS COPYING FAQ HACKING NEWS README
%{_bindir}/%{name}
%{_bindir}/%{name}convert
%{_datadir}/applications/%{name}.desktop
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}-py2.7.egg-info

%post
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || 


%changelog
* Sat Dec 17 2011 qmp <glang@lavabit.com> - 0.17.1-1
- Initial packaging
