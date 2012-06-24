%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	CSS
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - class for generating CSS declarations
Summary(pl):	%{_pearname} - klasa do generowania deklaracji CSS
Name:		php-pear-%{_pearname}
Version:	0.3.4
Release:	3
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8f3d1eecd60e998da40f53c7e6306841
URL:		http://pear.php.net/package/HTML_CSS/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-HTML_Common >= 1.2
Requires:	php-pear-PEAR >= 1:1.3.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# included in tests
%define		_noautoreq 'pear(HTML_TestListener.php)' 'pear(TestUnit.php)'

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

%description -l pl
%{_pearname} dostarcza prostego interfejsu do generowania deklaracji
arkusza styl�w. Jest ca�kowicie zgodny ze standardami, i ma kilka
�wietnych cech:
- prosty obiektowo zorientowany interfejs do definicji CSS
- wyj�cie do:
  - deklaracji arkusza styl�w w miejscu
  - wewn�trznych deklaracji arkusza styl�w w dokumencie
  - samodzielnego pliku z definicjami
  - tablicy definicji

Ponadto wsp�dzieli nast�puj�ce cechy z klasami opartymi na
HTML_Common:
- r�ne style wci��
- r�ne rodzaje znak�w ko�ca linii

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
