Name:           binwalk
Version:        0.4
Release:        1%{?dist}
Summary:        Firmware analysis tool

License:        MIT
URL:            https://code.google.com/p/%{name}/
Source0:        https://%{name}.googlecode.com/files/%{name}-0.4.0.tar.gz

BuildRequires:  libcurl-devel
BuildRequires:  zlib-devel

%description
Binwalk is a tool for searching a given binary image for embedded files and
executable code. Specifically, it is designed for identifying files and code
embedded inside of firmware images. Binwalk uses the libmagic library, so it is
compatible with magic signatures created for the Unix file utility.

Binwalk also includes a custom magic signature file which contains improved
signatures for files that are commonly found in firmware images such as
compressed/archived files, firmware headers, Linux kernels, bootloaders,
filesystems, etc. 


%prep
%setup -q -n %{name}-%{version}.0


%build
pushd src
%configure \
 --disable-updates \
# --enable-libmagic
make %{?_smp_mflags}
popd


%install
pushd src
make install DESTDIR=%{buildroot}
popd


%files
%{_bindir}/%{name}
%{_sysconfdir}/%{name}
%doc docs/README



%changelog
* Sat Nov 26 2011 qmp <glang@lavabit.com> - 0.4-1
- Initial packaging
