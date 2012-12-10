%define name fortune-distribfr
%define version 20090926
%define release %mkrel 2

Summary: The best IRC moments by the French Mandr* team
Summary(fr): Les meilleurs moments IRC par les mandr* français
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPLv2+
Group: Toys
URL: http://nanardon.zarb.org/cgi-bin/viewcvs.cgi/?root=fortune
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: fortune-mod
BuildRequires: fortune-mod
BuildRequires: recode

%define thanks Milka, Ennael, Zborg, Zorro, Dolly, Erinmargault, Virginie, Hina,
%define thanks2 Paysage, Bibi, Cvjetic, Othalia, Mandi, leeloo, Little_Tux_Girl,
%define thanks3 poipoi, Scara, lafeebleue, Cinaee, eponae, annma, elephantine,
%define thanks4 melodie, Amaz, Jehane, Djezael

%description
The best moments of IRC chatting from channels #mandriva-fr ( ex #mandrakefr ),
#gentoofr, #lea-linux, on the IRC server irc.freenode.net (in French), and from
the Mandriva Linux Cooker mailing list.

This package includes octoz fortunes.

Special thanks to:
%{thanks}
%{thanks2}
%{thanks3}
%{thanks4}.

%description -l fr
Les meilleurs moments trouvés sur IRC sur les canaux #mandrivafr 
( ex #mandrakefr ), #gentoofr, #lea-linux, serveur IRC irc.freenode.net, et sur
la mailing-list Mandriva Linux Cooker.

Ce paquet inclut les fortunes octoz.

Spéciale dédicace à:
%{thanks}
%{thanks2}
%{thanks3}
%{thanks4}.

%prep
%setup -q -c %name
rm -f fr/*.dat
for fortune in fr/*;do recode l1..u8 $fortune; done

%build
%make clean
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
cd %buildroot%_datadir/games/fortunes/fr
for x in *.dat; do 
  ln -s $(echo $x|sed s/.dat//) $(echo $x|sed s/.dat/.u8/) 
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
 %_datadir/games/fortunes/mandrake*
%lang(fr) %_datadir/games/fortunes/fr/*




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 20090926-2mdv2011.0
+ Revision: 618333
- the mass rebuild of 2010.0 packages

* Sat Sep 26 2009 Michael Scherer <misc@mandriva.org> 20090926-1mdv2010.0
+ Revision: 449404
- update to new snapshot
- update thanks list
- update license

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 20080829-5mdv2010.0
+ Revision: 437574
- rebuild

* Sun Feb 15 2009 Olivier Thauvin <nanardon@mandriva.org> 20080829-4mdv2009.1
+ Revision: 340522
- add Jehane

* Sun Sep 28 2008 Olivier Thauvin <nanardon@mandriva.org> 20080829-3mdv2009.0
+ Revision: 289095
- complete thanks

* Fri Sep 26 2008 Olivier Thauvin <nanardon@mandriva.org> 20080829-2mdv2009.0
+ Revision: 288722
- update thanks

* Fri Aug 29 2008 Olivier Thauvin <nanardon@mandriva.org> 20080829-1mdv2009.0
+ Revision: 277291
- 20080829

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 20070905-4mdv2009.0
+ Revision: 266816
- rebuild early 2009.0 package (before pixel changes)

  + Olivier Thauvin <nanardon@mandriva.org>
    - new miss
    - complete thanks 3 again

  + Michael Scherer <misc@mandriva.org>
    - complete thanks3

* Mon May 05 2008 Götz Waschk <waschk@mandriva.org> 20070905-3mdv2009.0
+ Revision: 201383
- add u8 symlinks
- language tag the French quotes

* Mon May 05 2008 Götz Waschk <waschk@mandriva.org> 20070905-2mdv2009.0
+ Revision: 201373
- convert fortunes to UTF-8 (bug #23716)

  + Thierry Vignaud <tv@mandriva.org>
    - fix description-line-too-long
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 05 2007 Michael Scherer <misc@mandriva.org> 20070905-1mdv2008.0
+ Revision: 80162
- new version, with improved fortunes and quotes


* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 12:11:52 (53421)
- 20060806

* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 11:43:03 (53414)
Import fortune-distribfr

* Sat Mar 25 2006 Olivier Thauvin <nanardon@mandriva.org> 20060325-3mdk
- fix url (again, typo)

* Sat Mar 25 2006 Olivier Thauvin <nanardon@mandriva.org> 20060325-2mdk
- fix url

* Sat Mar 25 2006 Olivier Thauvin <nanardon@mandriva.org> 20060325-1mdk
- 20060325
- add Scara to thanks list

* Tue Dec 20 2005 Michael Scherer <misc@mandriva.org> 20051220-1mdk
- 20051220

* Thu Oct 27 2005 Michael Scherer <misc@mandriva.org> 20051027-1mdk
- 20051027

* Sun Aug 28 2005 Michael Scherer <misc@mandriva.org> 20050828-1mdk
- 20050828

* Thu Jul 28 2005 Olivier Thauvin <nanardon@mandriva.org> 20050728-1mdk
- 20050728 (helldragon included)
- add leeloo and Little_Tux_Girl as girl

* Wed Jun 08 2005 Michael Scherer <misc@mandriva.org> 20050608-1mdk
- 20050608
- update credit and description
- use mkrel

* Sat Feb 12 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr> 20050212-1mdk
- 20050212

* Mon Oct 18 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 20041018-1mdk
- 20041018
- Description is now UTF-8 encoded (and has better spelling :p)

* Mon Aug 30 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 20040830-1mdk
- 20040830

* Tue Aug 03 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 20040803-1mdk
- 20040803 (more octoz and cooker fortunes)

* Sat Jul 31 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 20040731-1mdk
- 20040731
- integrate missing fabulous octoz fortunes !

* Sat Jul 24 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 20040724-1mdk
- 20040724
- fix nick in desc

* Tue Dec 23 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 20031223-1mdk
- 20031223

* Sun Aug 31 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 20030831-1mdk
- 20030831
- BuildRequires fortune-mod

* Thu Aug 21 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 20030821-1mdk
- update

