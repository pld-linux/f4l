%define		_src_name	F4L-BETA
Summary:	SWF designer and generator
Summary(pl):	Program do projektowania i generowania SWF-ów
Name:		f4lm
Version:	0.2
Release:	0.beta.1
License:	GPL
Group:		X11/Applications/Publishing
#Source0:	http://dl.sourceforge.net/f4l/%{name}-%{version}.tar.gz
Source0:	http://dl.sourceforge.net/f4l/%{_src_name}-%{version}.tar.bz2
# Source0-md5:	6eaea1d9863518c663545ccb0cdf958f
URL:		http://f4l.sourceforge.net/
BuildRequires:	automake
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SWF designer and generator.

%description -l pl
Program do projektowania i generowania SWF-ów.

%prep
%setup -q -n %{_src_name}

%build
cp -f /usr/share/automake/config.sub admin
rm config.cache

%configure2_13 \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
