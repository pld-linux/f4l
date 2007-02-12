Summary:	SWF designer and generator
Summary(pl.UTF-8):	Program do projektowania i generowania SWF-ów
Name:		f4l
Version:	0.2.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Publishing
Source0:	http://dl.sourceforge.net/f4l/%{name}-%{version}.tar.bz2
# Source0-md5:	dcc2ef251814008e753becb933afb266
URL:		http://f4l.sourceforge.net/
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRequires:	rpmbuild(macros) >= 1.167
BuildRequires:	sed >= 4.0
Obsoletes:	f4lm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SWF designer and generator.

%description -l pl.UTF-8
Program do projektowania i generowania SWF-ów.

%prep
%setup -q

%build
%{__sed} -i 's,/usr/share/qt3,%{_datadir}/qt,' Makefile
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
