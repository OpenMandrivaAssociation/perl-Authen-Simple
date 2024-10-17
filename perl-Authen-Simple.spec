%define upstream_name    Authen-Simple
%define upstream_version 0.5
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.5
Release:	3

Summary:	Simple Authentication
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Authen/Authen-Simple-0.5.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(Crypt::PasswdMD5)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)

BuildArch:	noarch

%description
Simple and consistent framework for authentication.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.400.0-2mdv2011.0
+ Revision: 654877
- rebuild for updated spec-helper

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.400.0-1mdv2011.0
+ Revision: 504579
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.4-2mdv2010.0
+ Revision: 430263
- rebuild

* Fri Oct 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.4-1mdv2009.0
+ Revision: 291357
- import perl-Authen-Simple


* Thu Oct 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.4-1mdv2009.1
- initial mdv release, generated with cpan2dist


