Name: openamp
Version: 2021.10.0
Release: 1
Summary: Open asymmetric multiprocessing framework

License: BSD
URL: http://github.com/OpenAMP
Source0: https://github.com/OpenAMP/open-amp/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	libmetal-devel
BuildRequires:	libsysfs-devel

%description
The OpenAMP framework provides software components that enable development of
software applications for Asymmetric Multiprocessing (AMP) systems.

%package devel
Summary:	Development files for OpenAMP
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development file for OpenAMP
baremetal, and RTOS environments.

%prep
%autosetup -p1

%build
mkdir build
cd build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
	-DCMAKE_INCLUDE_PATH=%{_includedir}/libmetal/ \
	-DCMAKE_LIBRARY_PATH=%{_libdir} \
	-DWITH_STATIC_LIB=OFF \
	-DWITH_APPS=OFF ..


%install
cd build
%make_install

%ldconfig_scriptlets

%files
%license LICENSE.md
%doc README.md
%{_libdir}/libopen_amp.so.1
%{_libdir}/libopen_amp.so.1.1.0

%files devel
%{_includedir}/openamp/
%{_libdir}/libopen_amp.so

%changelog

* Fri Feb 11 2022 Wayne Ren <renwei41@huawei.com> - 2022.10.0-1
- Package init
