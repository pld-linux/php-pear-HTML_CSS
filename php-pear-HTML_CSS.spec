%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	CSS
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - class for generating CSS declarations
Summary(pl.UTF-8):	%{_pearname} - klasa do generowania deklaracji CSS
Name:		php-pear-%{_pearname}
Version:	1.5.3
Release:	1
Epoch:		0
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	65826e7039eecb0884c146d478e795bf
URL:		http://pear.php.net/package/HTML_CSS/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-HTML_Common >= 1.2.4
Requires:	php-pear-PEAR-core >= 1:1.5.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# included in tests
%define		_noautoreq 'pear(HTML_TestListener.php)' 'pear(TestUnit.php)' 'pear(PEAR.*)' 'pear(Services/W3C/CSSValidator.*)' 'pear(PHPUnit.*)'

%description
%{_pearname} provides a simple interface for generating a stylesheet
declaration. It is completely standards compliant, and has some great
features:
- simple OO interface to CSS definitions
- output to:
  - inline stylesheet declarations
  - document internal stylesheet declarations
  - standalone stylesheet declarations
  - array of definitions

In addition, it shares the following with HTML_Common based classes:
- indent style support
- line ending style

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
%{_pearname} dostarcza prostego interfejsu do generowania deklaracji
arkusza stylów. Jest całkowicie zgodny ze standardami, i ma kilka
świetnych cech:
- prosty obiektowo zorientowany interfejs do definicji CSS
- wyjście do:
  - deklaracji arkusza stylów w miejscu
  - wewnętrznych deklaracji arkusza stylów w dokumencie
  - samodzielnego pliku z definicjami
  - tablicy definicji

Ponadto współdzieli następujące cechy z klasami opartymi na
HTML_Common:
- różne style wcięć
- różne rodzaje znaków końca linii

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
