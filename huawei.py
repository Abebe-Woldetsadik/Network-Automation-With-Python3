from netmiko import ConnectHandler


device = {

    'device_type': 'huawei',

    'host': '192.168.2.150',

    'username': 'admin',

    'password': 'admin',

    'global_delay_factor': 0.1,

}


netmiko_connect = ConnectHandler(**device)

netmiko_connect.find_prompt()

print("Connecting to Device:")

config_commands = ["display memory", "display arp"]

output = netmiko_connect.send_config_set(config_commands, delay_factor=0.2)

netmiko_connect.disconnect()

print(output)
