#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Log
%define	pnam	Trace
Summary:	Log::Trace - provides a unified approach to tracing
Summary(pl.UTF-8):	Log::Trace - dostarcza jednolite podejście do śledzenia
Name:		perl-Log-Trace
Version:	1.070
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/B/BB/BBC/Log-Trace-%{version}.tar.gz
# Source0-md5:	773aefa7539b1857edb3e225cfbc4a22
URL:		http://search.cpan.org/dist/Log-Trace/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A module to provide a unified approach to tracing. A script can use
Log::Trace qw( < mode > ) to set the behaviour of the TRACE function.

By default, the trace functions are exported to the calling package
only. You can export the trace functions to other packages with the
Deep option. See "OPTIONS" for more information.

All exports are in uppercase (to minimise collisions with "real"
functions).

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Log/*.pm
%{perl_vendorlib}/Log/Trace
%{_mandir}/man3/*
