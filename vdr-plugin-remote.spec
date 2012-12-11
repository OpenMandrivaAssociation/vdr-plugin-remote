
%define plugin	remote
%define name	vdr-plugin-%plugin
%define version	0.4.0
%define rel	5

Summary:	VDR plugin: Remote control
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.escape-edv.de/endriss/vdr/
Source:		http://www.escape-edv.de/endriss/vdr/vdr-%plugin-%version.tgz
Patch0:		90_remote-0.4.0-1.5.7.dpatch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin extends the remote control capabilities of vdr.
The following remote control devices are supported:

(a) linux input device driver ('/dev/input/eventX', X=0,1,2,...)
    - built-in remote control port of the av711x-based DVB cards
      (aka full-featured cards), e.g. DVB-S Nexus [1]
    - remote control port of some budget cards, e.g. Nova-CI [2]
    - other input devices (not tested, please report success!)
    See file FAQ for a list of cards which have been reported to work.

(b) keyboard (tty driver): /dev/console, /dev/ttyX

(c) TCP connection (telnet)

(d) LIRC

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# Select an input device using evdev protocol
var=EVDEV_DEVICE
param="-i EVDEV_DEVICE"
# Select an input device using LIRC protocol
var=LIRC_DEVICE
param="-l LIRC_DEVICE"
# Select a terminal device for input
var=TTY_DEVICE
param="-t TTY_DEVICE"
# Select a terminal device for input with OSD
var=TTY_OSD_DEVICE
param="-T TTY_OSD_DEVICE"
# Select a connection on tcp port
var=TCP_PORT
param="-p tcp:TCP_PORT"
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY CONTRIBUTORS FAQ 


%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.4.0-5mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.4.0-4mdv2009.1
+ Revision: 359359
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.4.0-3mdv2009.0
+ Revision: 197971
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.4.0-2mdv2009.0
+ Revision: 197716
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt for api changes of VDR 1.5.7 (P0 from e-tobi)

* Fri Feb 29 2008 Anssi Hannula <anssi@mandriva.org> 0.4.0-1mdv2008.1
+ Revision: 176581
- new version

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.3.9-5mdv2008.1
+ Revision: 145195
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.3.9-4mdv2008.1
+ Revision: 103193
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.3.9-3mdv2008.0
+ Revision: 50039
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.3.9-2mdv2008.0
+ Revision: 42125
- rebuild for new vdr

* Sat May 19 2007 Anssi Hannula <anssi@mandriva.org> 0.3.9-1mdv2008.0
+ Revision: 28473
- 0.3.9

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.3.8-4mdv2008.0
+ Revision: 22677
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.3.8-3mdv2007.0
+ Revision: 90967
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.3.8-2mdv2007.1
+ Revision: 74078
- rebuild for new vdr
- Import vdr-plugin-remote

* Thu Aug 03 2006 Anssi Hannula <anssi@mandriva.org> 0.3.8-1mdv2007.0
- initial Mandriva release

