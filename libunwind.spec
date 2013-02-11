Summary:	libunwind - a (mostly) platform-independent unwind API
Name:		libunwind
Version:	1.1
Release:	1
License:	MIT
Group:		Libraries
#Source0:	http://download.savannah.gnu.org/releases/libunwind/%{name}-%{version}.tar.gz
# use git snapshot for now, can't be downloaded from savannah currently
# git clone git://git.sv.gnu.org/libunwind.git
# git archive --format=tar --prefix=libunwind-1.1/ HEAD | xz -c > libunwind-1.1.tar.xz
# 679b65cd221efa7df42b6a369c7b1ebe9d8b5c3e
Source0:	%{name}-%{version}.tar.xz
# Source0-md5:	62f418da972f9d685f9de2acf16ae39f
Patch0:		%{name}-link.patch
URL:		http://www.nongnu.org/libunwind/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-U_FORTIFY_SOURCE

%description
The goal of the libunwind project is to define a portable and
efficient C programming interface (API) to determine the call-chain
of a program.

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

