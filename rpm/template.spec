Name:           ros-hydro-asmach-tutorials
Version:        1.0.7
Release:        0%{?dist}
Summary:        ROS asmach_tutorials package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/smach_tutorials
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-actionlib
Requires:       ros-hydro-actionlib-msgs
Requires:       ros-hydro-asmach
Requires:       ros-hydro-rospy
Requires:       ros-hydro-smach-ros
Requires:       ros-hydro-turtlesim
BuildRequires:  ros-hydro-actionlib
BuildRequires:  ros-hydro-actionlib-msgs
BuildRequires:  ros-hydro-asmach
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-smach-ros
BuildRequires:  ros-hydro-turtlesim

%description
This package containes numerous examples of how to use SMACH. See the examples
directory.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Fri Oct 10 2014 Dash <dash@clearpathrobotics.com> - 1.0.7-0
- Autogenerated by Bloom

* Fri Oct 10 2014 Dash <dash@clearpathrobotics.com> - 1.0.6-0
- Autogenerated by Bloom

* Mon Oct 06 2014 Dash <dash@clearpathrobotics.com> - 1.0.5-0
- Autogenerated by Bloom

* Fri Oct 03 2014 Dash <dash@clearpathrobotics.com> - 1.0.4-0
- Autogenerated by Bloom

