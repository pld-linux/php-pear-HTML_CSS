%include	/usr/lib/rpm/macros.php
%define         _class          HTML
%define         _subclass       CSS
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - class for generating CSS declarations
Summary(pl):	%{_pearname} - klasa do generowania deklaracji CSS
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4a459102e6b81ff268ad22f345deed13
URL:		http://pear.php.net/package/HTML_CSS/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

This class has in PEAR status: %{_status}.

%description -l pl
%{_pearname} dostarcza prostego interfejsu do generowania deklaracji
arkusza stylów. Jest ca³kowicie zgodny ze standardami, i ma kilka
¶wietnych cech:
- prosty obiektowo zorientowany interfejs do definicji CSS
- wyj¶cie do:
  - deklaracji arkusza stylów w miejscu
  - wewnêtrznych deklaracji arkusza stylów w dokumencie
  - samodzielnego pliku z definicjami
  - tablicy definicji

Ponadto wspó³dzieli nastêpuj±ce cechy z klasami opartymi na
HTML_Common:
- ró¿ne style wciêæ
- ró¿ne rodzaje znaków koñca linii

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{examples,tests}
%{php_pear_dir}/%{_class}/*.php
