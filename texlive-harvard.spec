%global tl_name harvard
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0.5
Release:	%{tl_revision}.1
Summary:	Harvard citation package for use with LaTeX2e
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/harvard
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/harvard.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/harvard.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/harvard.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a re-implementation, for LaTeX2e, of the original Harvard
package. The bundle contains the LaTeX package, several BibTeX styles,
and a 'Perl package' for use with LaTeX2HTML. Harvard is an author-year
citation style (all but the first author are suppressed in second and
subsequent citations of the same entry); the package defines several
variant styles: apsr.bst for the American Political Science Review;
agsm.bst for Australian Government publications; dcu.bst from the Design
Computing Unit of the University of Sydney; kluwer.bstwhich aims at the
format preferred in Kluwer publications; nederlands.bst which deals with
sorting Dutch names with prefixes (such as van) according to Dutch
rules, together with several styles whose authors offer no description
of their behaviour.

