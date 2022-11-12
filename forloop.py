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

for i in range(2, 11):
    connection.send_config_set('vlan' + str(n))
    connection.send_config_set('Name python' + str(n))

print(connection.send_command('show vlan'))

connection.disconnect()
