Summary:	SWF designer and generator
Summary(pl):	Program do projektowania i generowania SWF-ów
Name:		f4l
Version:	0.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Publishing
Source0:	http://dl.sourceforge.net/f4l/%{name}-%{version}.tar.bz2
# Source0-md5:	d123d5108b1e434de7d1195d7046a4e9
URL:		http://f4l.sourceforge.net/
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRequires:	rpmbuild(macros) >= 1.167
BuildRequires:	sed >= 4.0
Obsoletes:	f4lm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SWF designer and generator.

%description -l pl
Program do projektowania i generowania SWF-ów.

%prep
%setup -q

%build
%{__sed} -i 's,mkspecs.*,share/qt/mkspecs/default/qmake.conf,' Makefile
%{__make} \
	CXXFLAGS="%{rpmcxxflags} -Wno-deprecated" \
	QTDIR="%{_prefix}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bin/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
