%global pkg_name xmonad-utils
%global common_summary A small collection of X utilities
%global common_description \
A small collection of X utilities useful when running XMonad. It includes: \
* hxsel, which returns the text currently in the X selection; \
* hslock, a simple X screen lock; \
* hmanage: an utility to toggle the override-redirect property of any window; \
* and hhp, a simple utility to hide the pointer, similar to unclutter. \
%global debug_package %{nil}
Name:           %{pkg_name}
Version:        0.1.2
Release:        2%{?dist}
Summary:        %{common_summary}

Group:          User Interface/X
License:        BSD
URL:            http://hackage.haskell.org/cgi-bin/hackage-scripts/package/%{name}
Source0:        http://hackage.haskell.org/packages/archive/%{name}/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ghc
BuildRequires:  ghc-ghc-devel
BuildRequires:  ghc-X11-devel
BuildRequires:  ghc-rpm-macros

%description
%{common_description}


%prep
%setup -q


%build
%ghc_bin_build

%install
%ghc_bin_install

%clean


%files
%defattr(-,root,root,-)
%doc LICENSE
%{_bindir}/hhp
%{_bindir}/hmanage
%{_bindir}/hslock
%{_bindir}/hxput
%{_bindir}/hxsel

%changelog
* Fri Dec 24 2010 build@rnd - 0.1.2-2
- Typo

* Fri Dec 24 2010 build@rnd - 0.1.2-1
- Initial packaging
