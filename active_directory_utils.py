from ldap3 import Server, Connection, MODIFY_REPLACE, ALL
from ldap3.core.exceptions import LDAPException
from copy import copy, deepcopy
from django.conf import settings

def create_ad_user(person):
    error_message = ""
    first = person.preferred_name if person.preferred_name else person.first_name
    first_last = '{0} {1}'.format(first, person.last_name)
    username = '{}.{}'.format(first, person.last_name)
    username.replace('-', '')
    username.replace(' ', '')
    username.replace("'", '')
    email = '{}@companyX.com'.format(username)
    server = Server(settings.LDAP_SERVER), use_ssl=True)
    dn = 'CN={0},{1}{2},OU=Company Users,DC=myDomain,DC=local'.format(first_last, details[2], details[0])
    
    try:
        conn = Connection(
            server,
            user=settings.LDAP_USER,
            password=settings.LDAP_PASS,
        )
        conn.bind()
        conn.add(
            dn=dn,
            object_class=[
                'top',
                'person',
                'organizationalPerson',
                'user'
            ],
            attributes={
                'employeeID': person.employeeId,
                'sAMAccountName': username,
                'userPrincipalName': email,
                'physicalDeliveryOfficeName': 'Office 1',
                'company': 'Company X',
                'manager': get_ad_user_object(person.managerId).entry_dn,
                'employeeType': person.role,
                'mail': email,
                'proxyAddresses': ['SMTP:' + email],
                'title': person.title,
                'sn': person.last_name,
                'cn': first_last,
                'givenName': person.last_name,
                'distinguishedName': dn,
                'displayName': first_last,
                'name': first_last
            },
        )

        create_result = deepcopy(conn.result)
        conn.extend.microsoft.modify_password(dn, 'Welcome!')
        conn.modify(dn, {'userAccountControl': [('MODIFY_REPLACE', 512)]})
    except LDAPException as ldap_error:
        error_message = "LDAPException: Could not create active directory data for user. {0}.".format(ldap_error)
    except Exception as error:
        error_message = "Exception: Could not create active directory data for user. {0}.".format(error)
    finally:
        conn.unbind()

    if error_message:
        return True, error_message
    else:
        if create_result['description'] == 'operationsError':
            return True, create_result['description']
        return False, create_result['description']


def get_ad_user_object(person):
    ldap_server_ip = settings.LDAP_SERVER[8:len(settings.LDAP_SERVER)-4]
    server = Server(ldap_server_ip, get_info=ALL)
    conn = Connection(server, settings.LDAP_USER, settings.LDAP_PASS, auto_bind=True)
    search_base = 'ou=Company Users,dc=mydomain,dc=local'
    search_filter = "(&({0})({1}={2}))".format(
        'objectClass=*',
        'employeeID',
        person.employeeId
    )
    conn.search(
        search_base,
        search_filter,
        attributes='*'
    )

    if len(conn.entries) > 0:
        return conn.entries[0]
    else:
        return None


def modify_ad_username(person, username):
    error_message = ""
    dn = get_ad_user_object(person.employeeId).entry_dn
    server = Server(settings.LDAP_SERVER)
    userPrincipalName = '{}@companyX.com'.format(username)
    try:
        conn = Connection(
            server,
            user=settings.LDAP_USER,
            password=settings.LDAP_PASS,
        )
        conn.bind()
        conn.modify(
            dn=dn,
            changes={
                'userPrincipalName': [(MODIFY_REPLACE, [userPrincipalName])],
                'sAMAccountName': [(MODIFY_REPLACE, [username])]
            },
        )
    except LDAPException as ldap_error:
        error_message = "LDAPException: Could not modify active directory data for user. {0}.".format(ldap_error)
    except Exception as error:
        error_message = "Exception: Could not modify active directory data for user. {0}.".format(error)
    finally:
        conn.unbind()

    if error_message:
        return True, error_message
    else:
        return False, conn.result['message']

