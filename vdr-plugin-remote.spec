%define plugin	remote

Summary:	VDR plugin: Remote control
Name:		vdr-plugin-%plugin
Version:	0.4.0
Release:	8
Group:		Video
License:	GPL
URL:		https://www.escape-edv.de/endriss/vdr/
Source:		http://www.escape-edv.de/endriss/vdr/vdr-%plugin-%{version}.tgz
Patch0:		90_remote-0.4.0-1.5.7.dpatch
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
%setup -q -n %plugin-%{version}
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
%vdr_plugin_install

%files -f %plugin.vdr
%doc README HISTORY CONTRIBUTORS FAQ 


