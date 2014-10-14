Name:           ros-hydro-network-control-tests
Version:        1.0.9
Release:        0%{?dist}
Summary:        ROS network_control_tests package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/network_control_tests
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-access-point-control
Requires:       ros-hydro-ddwrt-access-point
Requires:       ros-hydro-dynamic-reconfigure
Requires:       ros-hydro-hostapd-access-point
Requires:       ros-hydro-linksys-access-point
Requires:       ros-hydro-network-monitor-udp
Requires:       ros-hydro-network-traffic-control
Requires:       ros-hydro-rostest
BuildRequires:  ros-hydro-access-point-control
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-ddwrt-access-point
BuildRequires:  ros-hydro-dynamic-reconfigure
BuildRequires:  ros-hydro-hostapd-access-point
BuildRequires:  ros-hydro-linksys-access-point
BuildRequires:  ros-hydro-network-monitor-udp
BuildRequires:  ros-hydro-network-traffic-control
BuildRequires:  ros-hydro-rostest

%description
Test suite for the packages that are part of the &quot;WiFi Test Setup&quot;
project: network_monitor_udp, network_traffic_control, hostapd_access_point,
linksys_access_point, ddwrt_access_point.

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
* Tue Oct 14 2014 Dash <dash@clearpathrobotics.com> - 1.0.9-0
- Autogenerated by Bloom

* Fri Oct 10 2014 Dash <dash@clearpathrobotics.com> - 1.0.7-0
- Autogenerated by Bloom

* Fri Oct 10 2014 Dash <dash@clearpathrobotics.com> - 1.0.6-0
- Autogenerated by Bloom

* Mon Oct 06 2014 Dash <dash@clearpathrobotics.com> - 1.0.5-0
- Autogenerated by Bloom

* Fri Oct 03 2014 Dash <dash@clearpathrobotics.com> - 1.0.4-0
- Autogenerated by Bloom

