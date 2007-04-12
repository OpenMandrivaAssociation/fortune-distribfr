%define name fortune-distribfr
%define version 20060806
%define release %mkrel 1

Summary: The best IRC moments by the French Mandr* team
Summary(fr): Les meilleurs moments IRC par les mandr* français
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Toys
URL: http://nanardon.zarb.org/cgi-bin/viewcvs.cgi/?root=fortune
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: fortune-mod
BuildRequires: fortune-mod

%define thanks Milka, Ennael, Zborg, Zorro, Dolly, Erinmargault, Virginie, Hina,
%define thanks2 Paysage, Bibi, Cvjetic, Othalia, Mandi, leeloo, Little_Tux_Girl,
%define thanks3 poipoi, Scara

%description
The best moments of IRC chatting from channels #mandriva-fr ( ex #mandrakefr ), 
#gentoofr, #lea-linux, on the IRC server irc.freenode.net (in French), and from the
Mandriva Linux Cooker mailing list.

This package includes octoz fortunes.

Special thanks to:
%{thanks}
%{thanks2}
%{thanks3}.

%description -l fr
Les meilleurs moments trouvés sur IRC sur les canaux #mandrivafr 
( ex #mandrakefr ), #gentoofr, #lea-linux, serveur IRC irc.freenode.net, et sur 
la mailing-list Mandriva Linux Cooker.

Ce paquet inclut les fortunes octoz.

Spéciale dédicace à:
%{thanks}
%{thanks2}
%{thanks3}.

%prep
%setup -q -c %name

%build
%make clean
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_datadir/games/fortunes/*


