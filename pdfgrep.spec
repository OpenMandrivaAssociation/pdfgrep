Name:           pdfgrep
Summary:	search in pdf files for strings matching a regular expression
Version:        2.2.0
Release:        1
Source0:        https://pdfgrep.org/download/pdfgrep-%{version}.tar.gz
#Patch0:		pdfgrep-1.3.2-compile.patch
Url:		https://pdfgrep.org/
#Also:		http://pdfgrep.sourceforge.net/
#		https://gitlab.com/pdfgrep/pdfgrep.git
Group:          Text tools
License:	GPLv3
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(poppler-cpp)

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
%autosetup -p1
%configure

%build
%make_build

%install
%make_install

%files
%defattr(0755,root,root)
%doc COPYING AUTHORS
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/pdfgrep
%{_datadir}/zsh/site-functions/_pdfgrep
