Name:           ros-hydro-hostapd-access-point
Version:        1.0.4
Release:        0%{?dist}
Summary:        ROS hostapd_access_point package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/hostapd_access_point
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-access-point-control
Requires:       ros-hydro-dynamic-reconfigure
Requires:       ros-hydro-ieee80211-channels
Requires:       ros-hydro-rospy
BuildRequires:  ros-hydro-access-point-control
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-dynamic-reconfigure
BuildRequires:  ros-hydro-ieee80211-channels
BuildRequires:  ros-hydro-rospy

%description
A ROS node that controls a hostapd-based access point. It is mainly intended for
use with a wireless network adapter running in master mode. It implements the
dynamic_reconfigure interface defined in the [[access_point_control]] package.

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
* Fri Oct 03 2014 Dash <dash@clearpathrobotics.com> - 1.0.4-0
- Autogenerated by Bloom

