Summary:	C++ library to read and write XISF files produced by PixInsight
Summary(pl.UTF-8):	Bibliotek C++ do odczytu i zapisu plików XISF tworzonych przez PixInsight
Name:		libxisf
Version:	0.2.13
Release:	1
License:	GPL v3+
Group:		Libraries
#Source0Download: https://gitea.nouspiro.space/nou/libXISF/tags
Source0:	https://gitea.nouspiro.space/nou/libXISF/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Source0-md5:	ff7dd5251bf630d14b28770604ecde3b
URL:		https://nouspiro.space/?page_id=306
BuildRequires:	cmake >= 3.14
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	lz4-devel
BuildRequires:	pkgconfig
BuildRequires:	pugixml-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	zlib-devel
BuildRequires:	zstd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibXISF is C++ library that can read and write XISF files produced by
PixInsight.

%description -l pl.UTF-8
LibXISF to biblioteka C++ potrafiąca czytać i zapisywać pliki XISF,
tworzone przez PixInsight.

%package devel
Summary:	Header files for XISF library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki XISF
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:7
Requires:	lz4-devel
Requires:	pugixml-devel
Requires:	zlib-devel
Requires:	zstd-devel

%description devel
Header files for XISF library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki XISF.

%prep
%setup -q -n %{name}

%build
%cmake -B build \
	-DCMAKE_INSTALL_INCLUDEDIR=include \
	-DCMAKE_INSTALL_LIBDIR=%{_lib} \
	-DUSE_BUNDLED_LIBS=OFF

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libXISF.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXISF.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXISF.so
%{_includedir}/libXISF_global.h
%{_includedir}/libxisf.h
%{_pkgconfigdir}/libxisf.pc
