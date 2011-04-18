%define upstream_name    Authen-Simple
%define upstream_version 0.4

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Simple Authentication
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Authen/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(Class::Data::Inheritable)
BuildRequires: perl(Crypt::PasswdMD5)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Digest::SHA)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Simple and consistent framework for authentication.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
