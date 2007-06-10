%define name gimp-dbp
%define version 1.1.5
%define fversion %(echo %version|sed s/\\\\\./-/g)
%define release %mkrel 2
%define gimpdir %(gimptool-2.0 --gimpplugindir)
%define oname dbp

Summary: David's Batch Processor for The GIMP
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.ozemail.com.au/~hodsond/%{oname}Src-%{fversion}.tar.bz2
Patch: dbp-1.1.5-include.patch
License: GPL
Group: Graphics
Url: http://members.ozemail.com.au/~hodsond/dbp.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gimp-devel
Requires: gimp

%description

DBP (David's Batch Processor) is a simple batch processing plugin for
the Gimp - it allows the user to automatically perform operations
(such as resize) on a collection of image files. Its main advantage is
that the user does not have to learn a scripting language. Like the
Gimp itself, DBP relies on a graphical interface. The user creates a
list of images, and sets up the processing required for each
image. The results of the current settings can be displayed. Once the
required sequence of operations has been set up, DBP performs the same
processing on each image in turn. The images can be colour corrected,
resized, cropped, and sharpened, then renamed and saved to a different
file in a specified image format. All the steps (except loading and
saving the image!) are optional; so the simplest use of DBP is just to
convert a number of image files from one format to another.

Note that DBP is intended for RGB, not indexed images. Trying to
process an indexed image will probably just cause an error, and DBP
will halt. Also, DBP will not overwrite the original image (in fact,
it should not overwrite any file) - images must at least be either
renamed (possibly by changing the image format) or moved to a
different directory.

%prep
%setup -q -n %oname-%version
%patch -p1

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 755 %oname %buildroot%gimpdir/plug-ins/%oname


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc %oname.html *.png
%_libdir/gimp/2.0/plug-ins/%oname


