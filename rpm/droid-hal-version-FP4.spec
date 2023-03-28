# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device FP4
%define vendor fairphone

# Manufacturer and device name to be shown in UI
%define vendor_pretty Fairphone
%define device_pretty FP4

# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator_native 1
%define have_led 1
# Device-specific ofono configuration
Provides: ofono-configs
Obsoletes: ofono-configs-mer
Obsoletes: ofono-configs-binder
Obsoletes: bluez5-configs-mer

# No device reset
Provides: jolla-settings-system-reset

# Device-specific usb-moded configuration
Provides: usb-moded-configs
Obsoletes: usb-moded-defaults

Obsoletes: audioflingerglue



Requires: libgbinder-tools

%define ofono_enable_plugins bluez5,hfp_ag_bluez5
%define ofono_disable_plugins bluez4,dun_gw_bluez4,hfp_ag_bluez4,hfp_bluez4,dun_gw_bluez5,hfp_bluez5

%include droid-hal-version/droid-hal-version.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

