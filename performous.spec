#package for rpmfusion-free
#inspired by http://aur.archlinux.org/packages/pe/performous-git/PKGBUILD
%define gitrev 53cac51
Name:           performous
Version:        0.6.1
Release:        1.git%{gitrev}%{?dist}
Summary:        The All-in-One Music Game

License:        GPLv2+
URL:            http://performous.org
Source0:        %{name}-%{version}-%{gitrev}.tar.xz
Patch0:         %{name}.fix-glib2-headers.patch

BuildRequires:  cmake
BuildRequires:  glibmm24-devel
BuildRequires:  gettext
BuildRequires:  boost-devel
BuildRequires:  SDL-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  cairo-devel
BuildRequires:  librsvg2-devel
BuildRequires:  glew-devel
BuildRequires:  libxml++-devel
BuildRequires:  portaudio-devel
BuildRequires:  portmidi-devel
BuildRequires:  ImageMagick-c++-devel
BuildRequires:  opencv-devel
BuildRequires:  pango-devel
BuildRequires:  desktop-file-utils
BuildRequires:  help2man

%description
Everybody loves music and while one might be too shy to dance or sing, there is
always some part for everyone. Performous is about improving your skills and
having fun at the same time. No special hardware required, you may play guitar
on your PC keyboard, sing on your laptop microphone and so on. If you do have
SingStar microphones, Guitar Hero or Rock Band instruments, or dance pads, just
plug them into your USB ports and start rocking!


%prep
%setup -q -n %{name}-%{version}-%{gitrev}
%patch0 -p1


%build
mkdir build
pushd build
%cmake ..
make %{?_smp_mflags}
popd


%install
pushd build
make install DESTDIR=%{buildroot} INSTALL="install -p"
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
pushd ../docs/man
mkdir -pm 755 %{buildroot}/%{_mandir}/man1
install -pm 644 *1 %{buildroot}/%{_mandir}/man1/
popd
%find_lang Performous
popd

%post
update-desktop-database &>/dev/null || :

%postun
update-desktop-database &>/dev/null || :


%files -f build/Performous.lang
%doc
%{_bindir}/%{name}
%{_bindir}/gh_fsb_decrypt
%{_bindir}/gh_xen_decrypt
%{_bindir}/itg_pck
%{_bindir}/ss_adpcm_decode
%{_bindir}/ss_archive_extract
%{_bindir}/ss_chc_decode
%{_bindir}/ss_cover_conv
%{_bindir}/ss_extract
%{_bindir}/ss_ipu_conv
%{_bindir}/ss_ipu_decode
%{_bindir}/ss_pak_extract
%{_datadir}/applications/%{name}.desktop
%{_datadir}/games/%{name}
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man1/gh_fsb_decrypt.1*
%{_mandir}/man1/gh_xen_decrypt.1*
%{_mandir}/man1/ss_adpcm_decode.1*
%{_mandir}/man1/ss_chc_decode.1*
%{_mandir}/man1/ss_cover_conv.1*
%{_mandir}/man1/ss_extract.1*
%{_mandir}/man1/ss_ipu_conv.1*
%{_mandir}/man1/ss_ipu_decode.1*
%{_mandir}/man1/ss_pak_extract.1*
%{_mandir}/man6/%{name}.6*



%changelog
*Mon Jun 18 2012 qmp <glang@lavabit.com> - 0.6.1-1.git53cac51
- Initial packaging
