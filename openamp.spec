Name: openamp
Version: 2022.10.1
Release: 4
Summary: Open asymmetric multiprocessing framework

License: BSD-3-Clause
URL: http://github.com/OpenAMP
Source0: https://github.com/OpenAMP/open-amp/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

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

%package demos
Summary:	Demos for OpenAMP
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description demos
Demos for OpenAMP
baremetal, and RTOS environments.

%prep
%autosetup -p1

%build
mkdir build
cd build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
	-DCMAKE_INCLUDE_PATH=%{_includedir}/libmetal/ \
	-DCMAKE_LIBRARY_PATH=%{_libdir} \
	-DMACHINE=generic \
	-DWITH_STATIC_LIB=OFF \
	-DWITH_PROXY=ON \
	-DWITH_APPS=ON ..


%install
cd build
%make_install

%ldconfig_scriptlets

%files
%license LICENSE.md
%doc README.md
%{_libdir}/*.so*

%files devel
%{_includedir}/openamp/
%{_libdir}/libopen_amp.so

%files demos
%{_bindir}/*-shared

%changelog
* Wed March 15 2023 hanzongcheng <hanzongcheng@huawei.com> - 2022.10.1-4
- rename to openamp

* Mon Feb 27 2023 hanzongcheng <hanzongcheng@huawei.com> - 2022.10.1-3
- update to 2022.10.1

* Tue Aug 9 2022 zhangziyang <zhangziyang1@huawei.com> - 2022.04.0-2
- synchronous embedded compilation and packaging options

* Thu Jun 30 2022 luojects <luoyonglun@huawei.com> - 2022.04.0-1
- update to 2022.04.0

* Fri Jun 17 2022 liukuo <liukuo@kylinos.cn> - 2021.10.0-2
- License compliance rectification

* Fri Feb 11 2022 Wayne Ren <renwei41@huawei.com> - 2021.10.0-1
- Package init
