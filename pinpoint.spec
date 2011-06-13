Name:           pinpoint
Version:        0.1.2
Release:        2%{?dist}
Summary:        Simple presentation tool

License:        LGPLv2
URL:            http://live.gnome.org/Pinpoint
Source0:        http://ftp.gnome.org/pub/GNOME/sources/pinpoint/0.1/%{name}-%{version}.tar.bz2

BuildRequires:  clutter-devel
BuildRequires:  cairo-devel
BuildRequires:  clutter-gst-devel
BuildRequires:  librsvg2-devel

%description
Pinpoint a simple presentation tool that hopes to avoid audience death by bullet
point and instead encourage presentations containing beautiful images and small
amounts of concise text in slides.

Features :

    Text position
    Styling of font, text-color, contrast background and text positioning for
    global default and per slide overrides.
    Image backgrounds
    Video backgrounds
    Pango markup inside slides
    Transitions, extendable through json
    PDF export
    Embedding commands to run for demos in slides, with editable commandline
    during presentation.
    Monitoring of source file with live updates of changed slide for authoring 


%prep
%setup -q


%build
%configure --enable-pdf=yes\
        --enable-cluttergst=yes\
        --enable-rsvg=yes\
        --enable-dax=no
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
%{__install} -d -m0755 %{buildroot}/%{_defaultdocdir}/%{name}-%{version}/example
%{__install} -m0644 -p -t %{buildroot}/%{_defaultdocdir}/%{name}-%{version}/example introduction.pin bg.jpg bowls.jpg linus.jpg

%{__install} -m0644 -p -t %{buildroot}/%{_defaultdocdir}/%{name}-%{version} AUTHORS COPYING NEWS README


%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/%{name}/*.json
%{_defaultdocdir}/%{name}-%{version}
%{_defaultdocdir}/%{name}-%{version}/example
%{_defaultdocdir}/%{name}-%{version}/example/introduction.pin
%{_defaultdocdir}/%{name}-%{version}/example/bg.jpg
%{_defaultdocdir}/%{name}-%{version}/example/bowls.jpg
%{_defaultdocdir}/%{name}-%{version}/example/linus.jpg
%{_defaultdocdir}/%{name}-%{version}/AUTHORS
%{_defaultdocdir}/%{name}-%{version}/COPYING
%{_defaultdocdir}/%{name}-%{version}/NEWS
%{_defaultdocdir}/%{name}-%{version}/README



%changelog
* Mon Jun 13 2011 qmp <glang@lavabit.com> - 0.1.2-2
- enable rsvg (svg support)

* Sun Jun 12 2011 qmp <glang@lavabit.com> - 0.1.2-1
- Initial packaging
