Summary:	WebP image codec library and tools
Name:		libwebp
Version:	0.2.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://webp.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	dc9b26f16bd5221414dbab95f13d4453
URL:		https://developers.google.com/speed/webp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WebP image codec library and tools.

%package devel
Summary:	Header files for WebP library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for WebP library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS PATENTS README
%attr(755,root,root) %{_bindir}/cwebp
%attr(755,root,root) %{_bindir}/dwebp
%attr(755,root,root) %ghost %{_libdir}/libwebp.so.4
%attr(755,root,root) %{_libdir}/libwebp.so.*.*.*
%{_mandir}/man1/cwebp.1*
%{_mandir}/man1/dwebp.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwebp.so
%{_includedir}/webp
%{_pkgconfigdir}/libwebp.pc
