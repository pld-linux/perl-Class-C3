#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define	pdir	Class
%define	pnam	C3
Summary:	Class::C3 - A pragma to use the C3 method resolution order algorithm
Summary(pl.UTF-8):	Class::C3 - pragma do używania algorytmu C3 kolejności rozwiązywania metod
Name:		perl-Class-C3
Version:	0.35
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	db5450767d46ddb8ff31a99fbef7f3e0
URL:		https://metacpan.org/dist/Class-C3
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.52
BuildRequires:	perl-ExtUtils-CBuilder >= 0.27
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Algorithm-C3 >= 0.07
BuildRequires:	perl-Scalar-List-Utils >= 1.10
BuildRequires:	perl-Test-Simple >= 0.47
%endif
Suggests:	perl-Class-C3-XS >= 0.13
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

%description -l pl.UTF-8
Jest to aktualnie eksperymentalna pragma do zmiany standardowej
kolejności rozwiązywania metod w Perlu 5 z pierwszej co do głębokości,
od lewej do prawej (czyli pre-order) na bardziej przemyślaną kolejność
rozwiązywania metod C3.

C3 to nazwa algorytmu, którego celem jest dostarczenie rozsądnej
kolejności rozwiązywania metod przy wielokrotnym dziedziczeniu. Po raz
pierwszy został wprowadzony w języku Dylan (odnośniki w sekcji SEE
ALSO manuala), a następnie zaadoptowany jako preferowana MRO (Method
Resolution Order - kolejność rozwiązywania metod) dla nowego stylu
klas w Pythonie 2.3. Ostatnio został zaadoptowany jako "kanoniczna"
MRO dla klas Perla 6 i domyślna MRO dla obiektów Parrota.

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
%doc Changes
%{perl_vendorlib}/Class/C3.pm
%{perl_vendorlib}/Class/C3
%{_mandir}/man3/Class::C3*.3pm*
