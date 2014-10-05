# based on PLD Linux spec git://git.pld-linux.org/packages/.git
Summary:	(mostly) Platform-independent unwind API
Name:		libunwind
Version:	1.1
Release:	4
License:	MIT
Group:		Libraries
Source0:	http://download.savannah.gnu.org/releases/libunwind/%{name}-%{version}.tar.gz
Patch0:		%{name}-link.patch
URL:		http://www.nongnu.org/libunwind/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-U_FORTIFY_SOURCE

%description
Portable and efficient C programming interface (API) to determine the
call-chain of a program.

%package devel
Summary:	Header files for libunwind library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libunwind library.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %ghost %{_libdir}/libunwind-coredump.so.0
%attr(755,root,root) %ghost %{_libdir}/libunwind-ptrace.so.0
%attr(755,root,root) %ghost %{_libdir}/libunwind-setjmp.so.0
%attr(755,root,root) %ghost %{_libdir}/libunwind-x86*.so.8
%attr(755,root,root) %ghost %{_libdir}/libunwind.so.8
%attr(755,root,root) %{_libdir}/libunwind-coredump.so.*.*.*
%attr(755,root,root) %{_libdir}/libunwind-ptrace.so.*.*.*
%attr(755,root,root) %{_libdir}/libunwind-setjmp.so.*.*.*
%attr(755,root,root) %{_libdir}/libunwind-x86*.so.*.*.*
%attr(755,root,root) %{_libdir}/libunwind.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libunwind*.so
%{_libdir}/libunwind-generic.a
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/*.3*

