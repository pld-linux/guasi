Summary:	Generic Userspace Asyncronous Syscall Interface
Summary(pl.UTF-8):	Ogólny interfejs asynchronicznych wywołań systemowych
Name:		guasi
Version:	0.25
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.xmailserver.org/%{name}-%{version}.tar.gz
# Source0-md5:	ebbd96073b2ce7c7f0be16ebf01b758c
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

%description -l pl.UTF-8
Biblioteka GUASI implementuje oparty na wątkach ogólny silnik wywołań
asynchronicznych, mający nadać asynchroniczne zachowanie zwykle
synchronicznym wywołaniom. Może być używany do obudowania dowolnych
synchronicznych wywołań tak, że wywołanie może być zaszeregowane do
wykonania, a jego wynik pobrany później (tym samym nie blokując wątku
zlecającego). Biblioteka GUASI może być używana jako dopełnienie
standardowych interfejsów pobierania zdarzeń, takich jak poll(2),
select(2) czy epoll(4).

%package devel
Summary:	Header files for GUASI library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GUASI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for GUASI library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki GUASI.

%package static
Summary:	Static GUASI library
Summary(pl.UTF-8):	Statyczna biblioteka GUASI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GUASI library.

%description static -l pl.UTF-8
Statyczna biblioteka GUASI.

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
%attr(755,root,root) %ghost %{_libdir}/libguasi.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libguasi.so
%{_libdir}/libguasi.la
%{_includedir}/guasi.h
%{_includedir}/guasi_syscalls.h
%{_mandir}/man3/guasi.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libguasi.a
