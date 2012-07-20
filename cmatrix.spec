#Note : we don't package embedded fonts for now
Name:           cmatrix
Version:        1.2a
Release:        1%{?dist}
Summary:        Let you see the matrix code in your console

License:        GPL
URL:            http://www.asty.org/cmatrix/
Source0:        http://www.asty.org/cmatrix/dist/%{name}-%{version}.tar.gz

BuildRequires:  ncurses-devel

%description
CMatrix is a program I wrote one evening because I didn't want to have to run
Wind*ws to see the cool scrolling lines from 'The Matrix', my fave movie.  If
you haven't seen this movie and you are a fan of computers or sci-fi in
general, go see this movie!!!  I have seen it twice, and I'm pondering seeing
it again before it comes out on VHS.

Cmatrix is written in ncurses under Linux, and should compile on other OSes
with few modifications.  I  am always interested to hear from people who use
this program and any modifications they make to it! 


%prep
%setup -q -n %{name}-%{version}


%build
%configure
make %{?_smp_mflags}


%install
#warning : assume install goes cleanly, without installing
#X server side fonts
make install DESTDIR=%{buildroot} || :

%files
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz



%changelog
*Tue Jul 17 2012 qmp <glang@lavabit.com> - 1.2a-1
 - Initial packaging
