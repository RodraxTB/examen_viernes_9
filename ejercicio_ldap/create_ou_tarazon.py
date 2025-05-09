ous = [
	"alumnos",
	"3esoA", "3esoB", "3esoC", "3esoD", "3esoE", "3esoF", "3esoG",
	"1bachA", "1bachB", "1bachC", "1bachD", "1bachE",
	"GSasir1", "GSasir2",
	"GSdaw1", "GSdaw2"
]

base_dn = "dc=examentarazon,dc=org"

with open("ou_tarazon.ldif", "w") as f:
	for ou in ous:
		f.write(f"""dn: ou={ou},{base_dn}
objectClass: organizationalUnit
ou: {ou}

""")
