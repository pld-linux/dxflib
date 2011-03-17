Summary:	Open source C++ library mainly for parsing DXFTM files
Summary(pl.UTF-8):	Otwarta biblioteka w C++ do obslugi plikow DXF
Name:		dxflib
Version:	2.2.0.0
Release:	0.3
License:	GPL
Group:		Libraries
Source0:	ftp://anonymous:anonymous@ribbonsoft.com/archives/dxflib/%{name}-%{version}-1.src.tar.gz
# Source0-md5:	0eb6bef3b3a702012eeb4e99ef1aa3f1
Patch0:		%{name}_include_string.patch
URL:		http://www.qcad.org/dxflib.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open source C++ library mainly for parsing DXFTM files

%description -l pl.UTF-8
Otwarta biblioteka w C++ do obslugi plikow DXF

%prep
%setup -q -n %{name}-%{version}-1.src
%patch0

%build
%{__aclocal}
%{__autoconf}
%configure

%{__make}
%{__make} -C test

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	INCDIR=$RPM_BUILD_ROOT%{_includedir}/dxflib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/libdxflib.a
%{_includedir}/dxflib/*.h
