# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

%define package_name gaphas

Name:           python-gaphas
Version:        0.7.2
Release:        2%{?dist}
Summary:        Gaphas is a GTK+ based diagramming widget

License:        GPLv2
URL:            http://pypi.python.org/pypi/gaphas/0.7.2
#Source0:        http://pypi.python.org/packages/source/g/gaphas/gaphas-0.7.2.tar.gz#md5=8a18fa17a7f4df29d9e7762eb430816e
Source0:        %{package_name}-%{version}.tar.gz

Patch0:         python-gaphas.no_source_download.patch

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools

Requires:       pygtk2

%description
Gaphas is a MVC canvas that uses Cairo for rendering. One of the nicer things
of this widget is that the user (model) is not bothered with bounding box
calculations: this is all done through Cairo.

Some more features:

 Each item has it's own separate coordinate space (easy when items are
 rotated).
 Items on the canvas can be connected to each other. Connections are
 maintained by a linear constraint solver.
 Multiple views on one Canvas.
 What is drawn is determined by Painters. Multiple painters can be used and
 painters can be chained.
 User interaction is handled by Tools. Tools can be chained.
 Versatile undo/redo system



%prep
%setup -q -n %{package_name}-%{version}
%patch0 -p0


%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

 
%files
%doc COPYING README.rst NEWS
%{python_sitelib}/*


%changelog
*Sun Dec 18 2011 qmp <glang@lavabit.com> - 0.7.2-2
- Adds requirements on pygtk2
- Don't download sources while running setup.py (ez_setup) : add requirement
python-setuptools instead

*Sat Dec 17 2011 qmp <glang@lavabit.com> - 0.7.2-1
- Initial packaging
