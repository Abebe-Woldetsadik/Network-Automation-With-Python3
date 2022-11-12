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
print(connection.send_command('show ip interface br'))
connection.disconnect()
