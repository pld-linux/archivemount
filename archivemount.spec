Summary:	FUSE based filesystem for mounting archives
Name:		archivemount
Version:	0.9.1
Release:	2
License:	LGPL v2+
Group:		Applications/System
Source0:	https://www.cybernoia.de/software/archivemount/%{name}-%{version}.tar.gz
# Source0-md5:	954c096230ab1e1f7153555c0221b37d
URL:		https://www.cybernoia.de/software/archivemount.html
BuildRequires:	libarchive-devel
BuildRequires:	libfuse-devel >= 2.6
BuildRequires:	pkgconfig
Requires:	libfuse >= 2.6
Requires:	libfuse-tools >= 2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
archivemount is a piece of glue code between libarchive and FUSE. It
can be used to mount a (possibly compressed) archive (as in .tar.gz or
.tar.bz2) and use it like an ordinary filesystem.

%prep
%setup -q

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_bindir}/archivemount
%{_mandir}/man1/archivemount.1*
