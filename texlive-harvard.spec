Name:		texlive-harvard
Version:	2.0.5
Release:	1
Summary:	Harvard citation package for use with LaTeX 2e
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/harvard
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harvard.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harvard.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/harvard.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This is a re-implementation, for LaTeX 2e, of the original
Harvard package. The bundle contains the LaTeX package, several
BibTeX styles, and a 'Perl package' for use with LaTeX2HTML.
Harvard is an author-year citation style (all but the first
author are suppressed in second and subsequent citations of the
same entry); the package defines several variant styles: -
apsr.bst for the American Political Science Review; - agsm.bst
for Australian Government publications; - dcu.bst from the
Design Computing Unit of the University of Sydney; -
kluwer.bstwhich aims at the format preferred in Kluwer
publications; - nederlands.bst which deals with sorting Dutch
names with prefixes (such as van) according to Dutch rules;
together with several styles whose authors offer no description
of their behaviour.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/harvard/harvard.bib
%{_texmfdistdir}/bibtex/bst/harvard/agsm.bst
%{_texmfdistdir}/bibtex/bst/harvard/apsr.bst
%{_texmfdistdir}/bibtex/bst/harvard/dcu.bst
%{_texmfdistdir}/bibtex/bst/harvard/jmr.bst
%{_texmfdistdir}/bibtex/bst/harvard/jphysicsB.bst
%{_texmfdistdir}/bibtex/bst/harvard/kluwer.bst
%{_texmfdistdir}/bibtex/bst/harvard/nederlands.bst
%{_texmfdistdir}/tex/latex/harvard/harvard.sty
%doc %{_texmfdistdir}/doc/latex/harvard/INSTALL
%doc %{_texmfdistdir}/doc/latex/harvard/README
%doc %{_texmfdistdir}/doc/latex/harvard/harvard.pdf
%doc %{_texmfdistdir}/doc/latex/harvard/harvard.perl
%doc %{_texmfdistdir}/doc/latex/harvard/harvard.tex
%doc %{_texmfdistdir}/doc/latex/harvard/manifest.txt
#- source
%doc %{_texmfdistdir}/source/latex/harvard/Makefile
%doc %{_texmfdistdir}/source/latex/harvard/doc_Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
