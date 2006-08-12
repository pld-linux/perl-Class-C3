#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	C3
Summary:	Class::C3 - A pragma to use the C3 method resolution order algortihm
Summary(pl):	Class::C3 - pragma do u¿ywania algorytmu C3 kolejno¶ci rozwi±zywania metod
Name:		perl-Class-C3
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	eb8f390f8d4497c23e5437048869c809
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Exception >= 0.15
BuildRequires:	perl-Algorithm-C3
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is currently an experimental pragma to change Perl 5's standard
method resolution order from depth-first left-to-right (a.k.a -
pre-order) to the more sophisticated C3 method resolution order.

C3 is the name of an algorithm which aims to provide a sane method
resolution order under multiple inheritance. It was first introduced
in the Dylan language (see links in the manual SEE ALSO section), and
then later adopted as the preferred MRO (Method Resolution Order) for
the new-style classes in Python 2.3. Most recently it has been adopted
as the 'canonical' MRO for Perl 6 classes, and the default MRO for
Parrot objects as well.

%description -l pl
Jest to aktualnie eksperymentalna pragma do zmiany standardowej
kolejno¶ci rozwi±zywania metod w Perlu 5 z pierwszej co do g³êboko¶ci,
od lewej do prawej (czyli pre-order) na bardziej przemy¶lan± kolejno¶æ
rozwi±zywania metod C3.

C3 to nazwa algorytmu, którego celem jest dostarczenie rozs±dnej
kolejno¶ci rozwi±zywania metod przy wielokrotnym dziedziczeniu. Po raz
pierwszy zosta³ wprowadzony w jêzyku Dylan (odno¶niki w sekcji SEE
ALSO manuala), a nastêpnie zaadoptowany jako preferowana MRO (Method
Resolution Order - kolejno¶æ rozwi±zywania metod) dla nowego stylu
klas w Pythonie 2.3. Ostatnio zosta³ zaadoptowany jako "kanoniczna"
MRO dla klas Perla 6 i domy¶lna MRO dla obiektów Parrota.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Class/*.pm
%{_mandir}/man3/*
