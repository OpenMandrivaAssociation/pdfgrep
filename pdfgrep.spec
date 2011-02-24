%define name    pdfgrep
%define version 1.1
%define release %{mkrel 0}

Name:           %{name}
Summary:	search in pdf files for strings matching a regular expression
Version:        %{version}
Release:        %{release}
Source0:        http://sourceforge.net/projects/%{name}/files/%{version}/%{name}-%{version}.tar.gz
URL:            http://pdfgrep.sourceforge.net/
Group:          Text tools
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv3
BuildRequires:	libstdc++-devel
BuildRequires:	libpoppler-cpp-devel

%description
Pdfgrep is a tool to search text in PDF files. It works similar to grep.
Features:
 * search for regular expressions.
 * support for some important grep options, including:
	- filename output.
	- page number output.
	- optional case insensitivity.
	- count occurrences.
 * and the most important feature: color output!

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755,root,root)
%doc README NEWS COPYING AUTHORS
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}

%changelog
