Summary:	SWF designer and generator
Summary(pl):	Program do projektowania i generowania SWF-ów
Name:		f4lm
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications/Publishing
Source0:	http://dl.sourceforge.net/f4l/%{name}-%{version}.tar.gz
# Source0-md5:	63e9f24c9eed94d01e721dc9075817ac
URL:		http://f4l.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SWF designer and generator.

%description -l pl
Program do projektowania i generowania SWF-ów.

%prep
%setup -q

%build
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
%configure
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
