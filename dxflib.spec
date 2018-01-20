Summary:	Open source C++ library mainly for parsing DXFTM files
Summary(pl.UTF-8):	Otwarta biblioteka w C++ do obsługi plików DXF
Name:		dxflib
Version:	3.17.0
Release:	0.1
License:	GPL v2+
Group:		Libraries
Source0:	https://qcad.org/archives/dxflib/%{name}-%{version}-src.tar.gz
# Source0-md5:	b4b3bdc7ed678952b5a81c01d1faaac2
URL:		https://qcad.org/en/what-is-dxflib
BuildRequires:	qt5-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open source C++ library mainly for parsing DXFTM files

%description -l pl.UTF-8
Otwarta biblioteka w C++ do obsługi plików DXF

%prep
%setup -q -n %{name}-%{version}-src

%build

qmake-qt5 -r \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_LINK="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}" \
	QMAKE_RPATH=

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/dxflib}
cp -p libdxflib.a $RPM_BUILD_ROOT%{_libdir}/
cp -p src/*.h $RPM_BUILD_ROOT%{_includedir}/dxflib/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/libdxflib.a
%{_includedir}/dxflib/*.h
