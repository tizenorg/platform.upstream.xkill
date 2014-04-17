Summary: kill a client by its X resource
Name: xkill
Version: 1.0.4
Release: 1
License: MIT
Group: User Interface/X
URL: http://www.x.org
Source0: %{name}-%{version}.tar.gz

# NOTE: Each upstream tarball has its own "PatchN" section, taken from
# multiplying the "SourceN" line times 100.  Please keep them in this
# order.  Also, please keep each patch specific to a single upstream tarball,
# so that they don't have to be split in half when submitting upstream.
#
# iceauth section
#Patch0:

#BuildRequires: xorg-x11-xutils-dev
#BuildRequires: pkgconfig(xorg-macros)
BuildRequires: pkgconfig(xmu) pkgconfig(xext) pkgconfig(xrandr)
BuildRequires: pkgconfig(xxf86vm) pkgconfig(xrender) pkgconfig(xi)
BuildRequires: pkgconfig(xt) pkgconfig(xpm)
# xsetroot requires xbitmaps-devel (which was renamed now)
#BuildRequires: xorg-x11-xbitmaps
# xsetroot
BuildRequires: libXcursor-devel
# xinput
BuildRequires: libXinerama-devel

# xrdb, sigh
#Requires: mcpp
# older -apps had xinput and xkill, moved them here because they're
# a) universally useful and b) don't require Xaw
#Conflicts: xorg-x11-apps < 7.6-4

%define DEF_SUBDIRS xkill
Provides: %{DEF_SUBDIRS}
#Provides: x11-xserver-utils = %{version}

%description
Xkill  is  a utility for forcing the X server to close connections to clients.
This program is very dangerous, but is useful for aborting programs that  have
displayed  undesired windows on a user's screen.  If no resource identifier is
given with -id, xkill will display a special cursor as a prompt for  the  user
to  select  a window to be killed.  If a pointer button is pressed over a non-
root window, the server will close its connection to the client  that  created
the window.

%prep
%setup -q

%build
%autogen
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}
{
      make install DESTDIR=$RPM_BUILD_ROOT
}

mkdir -p %{buildroot}%{_libdir}/systemd/user/core-efl.target.wants

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/share/license/%{name}
%doc
%{_bindir}/xkill
