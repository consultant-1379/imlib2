Summary: Powerful image loading and rendering library
Name: imlib2
Version: 1.4.5
Release: 0.%(date '+%Y%m%d')
License: BSD
Group: System Environment/Libraries
URL: http://www.enlightenment.org
Source: %{name}-%{version}.tar.gz
Packager: %{?_packager:%{_packager}}%{!?_packager:Michael Jennings <mej@eterm.org>}
Vendor: %{?_vendorinfo:%{_vendorinfo}}%{!?_vendorinfo:The Enlightenment Project (http://www.enlightenment.org/)}
Distribution: %{?_distribution:%{_distribution}}%{!?_distribution:%{_vendor}}
#BuildSuggests: XFree86-devel xorg-x11-devel freetype-devel freetype2-devel libungif-devel
BuildRequires: /usr/bin/freetype-config /usr/include/gif_lib.h
BuildRequires: libid3tag-devel
Requires: %{name}-loader_jpeg = %{version}
Requires: %{name}-loader_png = %{version}
Requires: %{name}-loader_argb = %{version}
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Imlib2 is an advanced replacement library for libraries like libXpm that
provides many more features with much greater flexibility and speed than
standard libraries, including font rasterization, rotation, RGBA space
rendering and blending, dynamic binary filters, scripting, and more.

%package devel
Summary: Imlib2 headers, static libraries and documentation
Group: System Environment/Libraries
Requires: %{name} = %{version}
Requires: /usr/bin/freetype-config

%description devel
Headers, static libraries and documentation for Imlib2.

%package filters
Summary: Imlib2 basic plugin filters set
Group: System Environment/Libraries
Requires: %{name} = %{version}
%description filters
Basic set of plugin filters that come with Imlib2

%package loader_lbm
Summary: Imlib2 LBM loader
Group: System Environment/Libraries
%description loader_lbm
LBM image loader/saver for Imlib2

%package loader_jpeg
Summary: Imlib2 JPEG loader
Group: System Environment/Libraries
BuildRequires: libjpeg-devel
%description loader_jpeg
JPEG image loader/saver for Imlib2

%package loader_png
Summary: Imlib2 PNG loader
Group: System Environment/Libraries
BuildRequires: libpng-devel
BuildRequires: zlib-devel
%description loader_png
PNG image loader/saver for Imlib2

%package loader_argb
Summary: Imlib2 ARGB loader
Group: System Environment/Libraries
%description loader_argb
ARGB image loader/saver for Imlib2

%package loader_bmp
Summary: Imlib2 BMP loader
Group: System Environment/Libraries
%description loader_bmp
BMP image loader/saver for Imlib2

%package loader_gif
Summary: Imlib2 GIF loader
Group: System Environment/Libraries
%description loader_gif
GIF image loader for Imlib2

%package loader_pnm
Summary: Imlib2 PNM loader
Group: System Environment/Libraries
%description loader_pnm
PNM image loader/saver for Imlib2

%package loader_tga
Summary: Imlib2 TGA loader
Group: System Environment/Libraries
%description loader_tga
TGA image loader/saver for Imlib2

%package loader_tiff
Summary: Imlib2 TIFF loader
Group: System Environment/Libraries
BuildRequires: libtiff-devel
%description loader_tiff
TIFF image loader/saver for Imlib2

%package loader_xpm
Summary: Imlib2 XPM loader
Group: System Environment/Libraries
%description loader_xpm
XPM image loader/saver for Imlib2

%package loader_bz2
Summary: Imlib2 .bz2 loader
Group: System Environment/Libraries
%description loader_bz2
Bzip2 compressed image loader/saver for Imlib2

%package loader_gz
Summary: Imlib2 .gz loader
Group: System Environment/Libraries
%description loader_gz
gz compressed image loader/saver for Imlib2

%package loader_id3 
Summary: Imlib2 .id3 loader
Group: System Environment/Libraries
%description loader_id3
id3 tag image loader/saver for Imlib2

%prep
%setup -q

%build
%{configure} --prefix=%{_prefix} \
%ifarch x86_64
       --disable-mmx \
%endif
%ifarch i386 i486 i586 i686
       --enable-mmx \
%endif
       $RPM_CONFIGURE_OPTS
%{__make} %{?_smp_mflags} %{?mflags}

%install
%{__make} %{?mflags_install} DESTDIR=$RPM_BUILD_ROOT install
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/%{name}/filters/*.a
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/%{name}/loaders/*.a

%clean
test "x$RPM_BUILD_ROOT" != "x/" && rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING COPYING-PLAIN README
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/loaders
%{_libdir}/lib*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/imlib2/*/*.la
%{_bindir}/imlib2-config
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/%{name}
%{_bindir}/imlib2_*

%files filters
%dir %{_libdir}/%{name}/filters
%attr(755,root,root) %{_libdir}/imlib2/filters/*.so

%files loader_lbm
%attr(755,root,root) %{_libdir}/imlib2/loaders/lbm.so

%files loader_jpeg
%attr(755,root,root) %{_libdir}/imlib2/loaders/jpeg.so

%files loader_png
%attr(755,root,root) %{_libdir}/imlib2/loaders/png.so

%files loader_argb
%attr(755,root,root) %{_libdir}/imlib2/loaders/argb.so

%files loader_bmp
%attr(755,root,root) %{_libdir}/imlib2/loaders/bmp.so

%files loader_gif
%attr(755,root,root) %{_libdir}/imlib2/loaders/gif.so

%files loader_pnm
%attr(755,root,root) %{_libdir}/imlib2/loaders/pnm.so

%files loader_tga
%attr(755,root,root) %{_libdir}/imlib2/loaders/tga.so

%files loader_tiff
%attr(755,root,root) %{_libdir}/imlib2/loaders/tiff.so

%files loader_xpm
%attr(755,root,root) %{_libdir}/imlib2/loaders/xpm.so

%files loader_bz2
%attr(755,root,root) %{_libdir}/imlib2/loaders/bz2.so

%files loader_gz
%attr(755,root,root) %{_libdir}/imlib2/loaders/zlib.so

%files loader_id3
%attr(755,root,root) %{_libdir}/imlib2/loaders/id3.so

%changelog
