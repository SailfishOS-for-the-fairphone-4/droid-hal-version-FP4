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

Obsoletes: ofono-configs-binder
Obsoletes: bluez5-configs-mer


%include droid-hal-version/droid-hal-version.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

