Name:           parallel
Version:        20101222
Release:        1%{?dist}
Summary:        GNU parallel is a shell tool for executing jobs in parallel

Group:          Applications/System
License:        GPLv3+
URL:            http://www.gnu.org/software/parallel/
Source0:        ftp://ftp.gnu.org/gnu/parallel/parallel-20101222.tar.bz2

Requires:       perl
#name clash : /usr/bin/parallel
Conflicts:      moreutils
BuildArch:      noarch

%description
GNU parallel is a shell tool for executing jobs in parallel locally or using
remote computers. A job is typically a single command or a small script that
has to be run for each of the lines in the input. The typical input is a list
of files, a list of hosts, a list of users, a list of URLs, or a list of
tables.

If you use xargs today you will find GNU parallel very easy to use as GNU
parallel is written to have the same options as xargs. If you write loops in
shell, you will find GNU parallel may be able to replace most of the loops and
make them run faster by running several jobs in parallel. If you use ppss or
pexec you will find GNU parallel will often make the command easier to read.

GNU parallel makes sure output from the commands is the same output as you
would get had you run the commands sequentially. This makes it possible to use
output from GNU parallel as input for other programs.

For each line of input GNU parallel will execute command with the line as
arguments. If no command is given, the line of input is executed. Several lines
will be run in parallel. GNU parallel can often be used as a substitute for
xargs or cat | sh.


%prep
%setup -q


%build
%configure --docdir=%{_defaultdocdir}/%{name}-%{version}
make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} INSTALL="install -p" CP="cp -p" install 
install -D -m 644 COPYING %{buildroot}/%{_defaultdocdir}/%{name}-%{version}/COPYING
install -D -m 644 NEWS %{buildroot}/%{_defaultdocdir}/%{name}-%{version}/NEWS
install -D -m 644 README %{buildroot}/%{_defaultdocdir}/%{name}-%{version}/README


%clean
#nothing to do

%files
%defattr(-,root,root,-)
%{_defaultdocdir}/%{name}-%{version}
%{_defaultdocdir}/%{name}-%{version}/COPYING
%{_defaultdocdir}/%{name}-%{version}/NEWS
%{_defaultdocdir}/%{name}-%{version}/README
%{_defaultdocdir}/%{name}-%{version}/parallel.html
%{_defaultdocdir}/%{name}-%{version}/niceload.html
%{_defaultdocdir}/%{name}-%{version}/sem.html
%{_defaultdocdir}/%{name}-%{version}/sql.html
%{_bindir}/parallel
%{_bindir}/niceload
%{_bindir}/sem
%{_bindir}/sql
%{_mandir}/man1/parallel.1*
%{_mandir}/man1/niceload.1*
%{_mandir}/man1/sem.1*
%{_mandir}/man1/sql.1*



%changelog
* Wed Dec 29 2010 build@rnd - 20101222-1
- Initial packaging
