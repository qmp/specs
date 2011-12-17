# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

%define package_name etk.docking

Name:           python-etk-docking
Version:        0.2
Release:        1%{?dist}
Summary:        Simple docking module

License:        GPLv2
URL:            http://pypi.python.org/pypi/etk.docking
#Source0:        http://pypi.python.org/packages/source/e/etk.docking/etk.docking-0.2.tar.gz#md5=ec6249aee6cd210bbdffd7bbe839e0a1
Source0:        %{package_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel

%description
Simple docking module


%prep
%setup -q -n %{package_name}-%{version}


%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
rm -rf %{buildroot}/usr/doc

 
%files
%doc AUTHORS COPYING COPYING.LESSER README TODO
# For noarch packages: sitelib
%{python_sitelib}/*


%changelog
* Sat Dec 17 2011 qmp <glang@lavabit.com> - 0.2-1
- Initial packaging
