Summary:	Generic Userspace Asyncronous Syscall Interface
Name:		guasi
Version:	0.17
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://www.xmailserver.org/%{name}-%{version}.tar.gz
# Source0-md5:	9f0a0eee7a3688925d10e0f35fad6d67
URL:		http://www.xmailserver.org/guasi-lib.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GUASI library implements a thread based generic asyncronous
execution engine, to be used to give otherwise synchronous calls an
asynchronous behavior. It can be used to wrap any synchronous call so
that it can be scheduled for execution and whose result can be fetched
at a later time (hence not blocking the submitter thread). The GUASI
library can be used as a complement to standard event retrieval
interfaces like poll(2), select(2), or epoll(4).

%package devel
Summary:	Header files for GUASI library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for GUASI library.

%package static
Summary:	Static GUASI library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GUASI library.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libguasi.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib/libguasi.so
%{_libdir}/lib/libguasi.la
%{_includedir}/guasi.h
%{_includedir}/guasi_syscalls.h
%{_mandir}/man3/guasi.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib/libguasi.a