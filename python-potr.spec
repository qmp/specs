#TODO : how to activate the plugin???
# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

%define gajim_plugin_dir %{_datadir}/gajim/plugins

Name:           python-potr
Version:        1.0.0b5
Release:        1%{?dist}
Summary:        A pure python OTR implementation

License:        GPLv3
URL:            https://github.com/afflux/pure-python-otr
Source0:        %{name}-%{version}.tar.xz
Patch0:         %{name}.build_gajim_plugin.patch

BuildArch:      noarch
BuildRequires:  python-devel

Requires:       python-crypto

%description
This is a pure Python OTR implementation; it does not bind to libotr

%package gajim-plugin-gotr
Summary:        gajim plugin for otr encryption
Requires:       gajim
Requires:       python-potr

%description gajim-plugin-gotr
gajim plugin for otr encryption


%prep
%setup -q
%patch0 -p1


%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot} 
mkdir -p %{buildroot}/%{gajim_plugin_dir}
mv %{buildroot}/%{python_sitelib}/gotr %{buildroot}/%{gajim_plugin_dir}/

 
%files
%doc
# For noarch packages: sitelib
%{python_sitelib}/potr
%{python_sitelib}/*egg-info

%files gajim-plugin-gotr
%{gajim_plugin_dir}/gotr

%changelog
* Mon Jul 02 2012 qmp <glang@lavabit.com> 1.0.0b5-1
- Initial packaging
