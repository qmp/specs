Name:           python3-docs
Version:        3.2.2
Release:        1%{?dist}
Summary:        Documentation for Python 3 programming language

License:        Python
URL:            http://docs.python.org/py3k/index.html
Source0:        http://docs.python.org/py3k/archives/python-%{version}-docs-html.tar.bz2

BuildArch:      noarch

%description
The python3-docs package contains documentation on the Python 3
programming language and interpreter.

Install the python3-docs package if you'd like to use the documentation
for the Python 3 language.


%prep
%setup -q -n python-%{version}-docs-html


%build
#nothing to do

%install
mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}
cp -pr * %{buildroot}/%{_docdir}/%{name}-%{version}/

 
%files
%{_docdir}/%{name}-%{version}

%changelog
* Thu Dec 08 2011 qmp <glang@lavabit.com> - 3.2.2-1
- Initial packaging
