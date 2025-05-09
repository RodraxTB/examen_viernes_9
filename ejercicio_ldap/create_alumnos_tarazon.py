base_dn = "dc=examentarazon,dc=org"
ou = "alumnos"
grupo = "alumnos"

with open("alumnos_tarazon.ldif", "w") as f:
	f.write(f"""dn: ou={ou},{base_dn}
objectClass: organizationalUnit
ou: {ou}

""")

	for i in range(1, 2001):
		uid = f"alumno{i}"
		f.write(f"""dn: uid={uid},ou={ou},{base_dn}
objectClass: inetOrgPerson
objectClass: posixAccount
objectClass: top
objectClass: shadowAccount
cn: {uid}
sn: tarazon{i}
uid: {uid}
uidNumber: {10000 + i}
gidNumber: 5000
homeDirectory: /home/{uid}
loginShell: /bin/bash
userPassword: alumno123

""")
