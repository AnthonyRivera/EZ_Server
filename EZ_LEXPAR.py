from client import *
from server import *
import time
import ply.lex as lex
from ply import yacc

tokens = [
    'IP',
    'INT',
    'STRING',
    'COLON',
    'COMMA',
    'PAR1',
    'PAR2'
]

reserved = {
    'address'       : 'ADDRESS',
    'port'          : 'PORT',
    'connection'    : 'CONNECTION',
    'connecting'       : 'CONNECTING',
    'to'           :'TO',
    'create'      : 'CREATE',
    'info'          : 'INFO',
    'close'         : 'CLOSE',
    'message'       : 'MESSAGE',
    'send'          : 'SEND',
    'show'          : 'SHOW',
    'server'        : 'SERVER',
    'clients'       : 'CLIENTS',
    'name'          : 'NAME',
    'in'            :  'IN',
    'more'          :  'MORE'
}

tokens += reserved.values()

t_COMMA = ','
t_COLON = r':'
t_PAR2 = '\)'
t_PAR1 = '\('

t_ignore = ' \t'



def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_BOOL(t):
    r'true|false'
    if  t.value == 'true':
        t.value = True
    elif t.value == 'false':
        t.value = False
    return t

def t_IP(t):
    r'\b((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\.)){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))\b'
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'\d*\.\d+'
    t.value = float(t.value)
    return t
def t_STRING(t):
    r'"(?:\\"|.)*?"'
    t.value = bytes(t.value.lstrip('"').rstrip('"'), "utf-8").decode("unicode_escape")
    return t

def t_KEYWORD(t):
    r'\w+'
    value = t.value.lower()
    if(reserved.get(value)):
        t.value = str(t.value)
        t.type = reserved.get(value, t.type)
    else:
        t.type = 'STRING'
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

global_vars = {}
connType = None
currentCon = None


def p_run_command(p):
    '''
    run_command : createServer
                | allowConnection
                | closeConnection
                | showClients
                | closeClient
                | createClient
                | sendMessage
                | showServer
    '''
    p[0] = p[1]


def p_creatServer(p):
    '''
    createServer : CREATE SERVER PAR1 ADDRESS IP COMMA PORT INT COMMA NAME STRING PAR2
    '''
    p[0] = Server(p[5], p[8])
    global_vars[p[11]] = p[0]
    global_vars['conType'] = "s"


def p_createClient(p):
    '''
    createClient : CONNECTING TO SERVER PAR1 ADDRESS IP COMMA PORT INT PAR2
    '''
    p[0] = Client(p[6], p[9])
    connType = "c"
    time.sleep(.500)
    username = p[0].getUsername()
    global_vars[username] = p[0]
    global_vars['conType'] = "c"
    global_vars['activeUser'] = username

def p_allowConnection(p):
    '''
    allowConnection : MORE CONNECTION IN STRING COLON INT
    '''
    server = global_vars[p[4]]
    if (server):
        server.changeClientLimit(p[6])
    else:
        print("server is not yet created")
def p_showClients(p):
    '''
    showClients : SHOW CLIENTS INFO IN STRING
    '''
    server = global_vars[p[5]]
    if (server):
        server.showClientsList()
    else:
        print("server is not yet created")

def p_showServer(p):
    '''
    showServer : SHOW STRING INFO
    '''
    server = global_vars[p[2]]
    if (server):
        server.showServerInfo()
    else:
        print("server is not yet created")

def p_closeConnection(p):
    '''
    closeConnection : CLOSE CONNECTION PAR1 STRING PAR2
    '''
    try:
        conn = global_vars[p[4]]
        conn.closeCon()
        sys.exit()
    except KeyError:
        print("object to close not found")
    except AttributeError:
        print("object to close is not of a connection type")

def p_closeClient(p):
    '''
    closeClient : CLOSE CONNECTION PAR1 STRING IN STRING PAR2
    '''
    server = global_vars[p[6]]
    if (server):
        try:
            if (server.lookUpClient(p[4])):
                server.closeClientCon(p[4])
        except KeyError:
            print("client not connected to server")


def p_sendMessage(p):
    '''
    sendMessage : SEND MESSAGE PAR1 STRING PAR2
    '''
    if (global_vars['conType'] == "c"):
        username = global_vars['activeUser']
        global_vars[username].send_msg(p[4])
    elif (global_vars['conType'] == "s"):
        currentCon.msg_to_all_from_server(p[4])
    else:
        print("message was not sent")

def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
        parser.errok()
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
print('Bienvenido a EZ_Server 0.01')
while True:
    try:
        msg = input('EZS->>')
        if msg == 'exit':
            sys.exit()
    except EOFError:
        break
    result = parser.parse(msg)