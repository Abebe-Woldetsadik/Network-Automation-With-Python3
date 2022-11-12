from netmiko import connectHandler
cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '173.16.0.1',
    'username': 'wihl',
    'password': 'cisco',
    'port': 22,
    'secret': 'cisco'
}
connection = connectHandler(**cisco_device)
connection.enable()
connection.send_config_set('vlan 2')
connection.send_config_set('Name python 2')
connection.send_config_set('vlan 3')
connection.send_config_set('Name python 3')
connection.send_config_set('vlan 4')
connection.send_config_set('Name python 4')
connection.send_config_set('vlan 5')
connection.send_config_set('Name python 5')

print(connection.send_command('show vlan'))

connection.disconnect()
