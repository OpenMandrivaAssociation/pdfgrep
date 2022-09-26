Name:           pdfgrep
Summary:	search in pdf files for strings matching a regular expression
Version:        1.3.2
Release:        1
Source0:        http://sourceforge.net/projects/%{name}/files/%{version}/%{name}-%{version}.tar.gz
Patch0:		pdfgrep-1.3.2-compile.patch
URL:            http://pdfgrep.sourceforge.net/
Group:          Text tools
License:	GPLv3
BuildRequires:	libpoppler-devel
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
%doc README NEWS COPYING AUTHORS
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/pdfgrep
%{_datadir}/zsh/site-functions/_pdfgrep
