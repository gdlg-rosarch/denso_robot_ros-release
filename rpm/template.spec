Name:           ros-hydro-denso-robot-core
Version:        3.0.1
Release:        0%{?dist}
Summary:        ROS denso_robot_core package

Group:          Development/Libraries
License:        MIT
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-actionlib
Requires:       ros-hydro-actionlib-msgs
Requires:       ros-hydro-bcap-core
Requires:       ros-hydro-bcap-service
Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-std-msgs
BuildRequires:  ros-hydro-actionlib
BuildRequires:  ros-hydro-actionlib-msgs
BuildRequires:  ros-hydro-bcap-core
BuildRequires:  ros-hydro-bcap-service
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-std-msgs

%description
DENSO robot control core package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Thu Dec 07 2017 DENSO WAVE INCORPORATED <denso_robot_soft@denso-wave.co.jp> - 3.0.1-0
- Autogenerated by Bloom

