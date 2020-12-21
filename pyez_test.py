from jnpr.junos import Device

dev = Device(host='dcr1', user="nornir", ssh_private_key_file="id_rsa", ssh_config="custom_ssh/config")

dev.open()
print(f"{dev.connected}")

print(f"{dev.facts['hostname']}\n{dev.facts['junos_info']}")

dev.close()
print(f"{dev.connected}")
