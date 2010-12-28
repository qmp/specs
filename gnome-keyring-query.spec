%global alphatag 20101228
Name:           gnome-keyring-query
Version:        0
Release:        %{alphatag}.1%{?dist}
Summary:        Cli utility for the gnome-keyring

Group:          Applications/Text
License:        Public Domain
URL:            http://www.gentoo-wiki.info/HOWTO_Use_gnome-keyring_to_store_SSH_passphrases
Source0:        %{name}.c

BuildRequires:  libgnome-keyring-devel

%description
Cli utility for the gnome-keyring

%prep
%setup -q -T -c %{name}
cp %{_sourcedir}/%{name}.c .


%build
gcc `pkg-config --cflags --libs gnome-keyring-1 glib-2.0` -o %{name} %{name}.c

%install
install -D -m 755 %{name} %{buildroot}/%{_bindir}/%{name}

%clean


%files
%defattr(-,root,root,-)
%{_bindir}/%{name}


%changelog
* Tue Dec 28 2010 - build@rnd - 0-20101228.1
- Initial packaging
