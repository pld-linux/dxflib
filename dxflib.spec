Summary:	XX
Summary(pl):	Biblioteka do obslugi plikow DXF (AutoCAD)
Name:		dxflib
Version:	2.2.0.0
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	ftp://anonymous:anonymous@ribbonsoft.com/archives/dxflib/dxflib-%{version}-1.src.tar.gz
# Source0-md5:	0eb6bef3b3a702012eeb4e99ef1aa3f1
Patch0:		%{name}_include_string.patch
URL:		http://www.qcad.org/dxflib.html
#BuildRequires:
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description

%description(pl)

%prep
%setup -q -n %{name}-%{version}-1.src
%patch0

%build
%{__aclocal}
%{__autoconf}
%configure 
%{__make}
%install
%files
