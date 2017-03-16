import dbus

def get_devices():
    bus = dbus.SystemBus()
    wifi = bus.get_object('org.freedesktop.NetworkManager',
                        '/org/freedesktop/NetworkManager')

    iface = dbus.Interface(wifi, dbus_interface='org.freedesktop.NetworkManager')

    # getting all devices
    m = iface.get_dbus_method("GetAllDevices", dbus_interface=None)
    devs = []
    for dev in m():
        devs.append("%s" % dev)
    return devs

def get_wifi_access_points_by_dev(device_path):
    print "Checking:", device_path
    bus = dbus.SystemBus()
    obj = bus.get_object('org.freedesktop.NetworkManager', device_path)

    iface = dbus.Interface(obj, dbus_interface='org.freedesktop.NetworkManager.Device.Wireless')

    # getting all wireless access points
    m = iface.get_dbus_method("GetAccessPoints", dbus_interface=None)

    aps = []
    for ap in m():
        aps.append("%s" % ap)
    print aps
    return aps

def get_wifi_access_points():
    aps = None
    for dev in get_devices():
        try:
            aps = get_wifi_access_points_by_dev(dev)
            #break
        except:
            pass
    return aps



if __name__ == "__main__":
    print get_devices()
    print get_wifi_access_points()
