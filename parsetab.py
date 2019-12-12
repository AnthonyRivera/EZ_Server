
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADDRESS CLIENTS CLOSE COLON COMMA CONNECTING CONNECTION CREATE IN INFO INT IP MESSAGE MORE NAME PAR1 PAR2 PORT SEND SERVER SHOW STRING TO\n    run_command : createServer\n                | allowConnection\n                | closeConnection\n                | showClients\n                | closeClient\n                | createClient\n                | sendMessage\n                | showServer\n    \n    createServer : CREATE SERVER PAR1 ADDRESS IP COMMA PORT INT COMMA NAME STRING PAR2\n    \n    createClient : CONNECTING TO SERVER PAR1 ADDRESS IP COMMA PORT INT PAR2\n    \n    allowConnection : MORE CONNECTION IN STRING COLON INT\n    \n    showClients : SHOW CLIENTS INFO IN STRING\n    \n    showServer : SHOW STRING INFO\n    \n    closeConnection : CLOSE CONNECTION PAR1 STRING PAR2\n    \n    closeClient : CLOSE CONNECTION PAR1 STRING IN STRING PAR2\n    \n    sendMessage : SEND MESSAGE PAR1 STRING PAR2\n    '
    
_lr_action_items = {'CREATE':([0,],[10,]),'MORE':([0,],[11,]),'CLOSE':([0,],[12,]),'SHOW':([0,],[13,]),'CONNECTING':([0,],[14,]),'SEND':([0,],[15,]),'$end':([1,2,3,4,5,6,7,8,9,27,38,40,42,44,48,55,57,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-13,-14,-12,-16,-11,-15,-10,-9,]),'SERVER':([10,21,],[16,28,]),'CONNECTION':([11,12,],[17,18,]),'CLIENTS':([13,],[19,]),'STRING':([13,24,25,29,33,39,54,],[20,31,32,35,40,45,56,]),'TO':([14,],[21,]),'MESSAGE':([15,],[22,]),'PAR1':([16,18,22,28,],[23,25,29,34,]),'IN':([17,26,32,],[24,33,39,]),'INFO':([19,20,],[26,27,]),'ADDRESS':([23,34,],[30,41,]),'IP':([30,41,],[36,46,]),'COLON':([31,],[37,]),'PAR2':([32,35,45,53,56,],[38,42,48,55,57,]),'COMMA':([36,46,50,],[43,49,52,]),'INT':([37,47,51,],[44,50,53,]),'PORT':([43,49,],[47,51,]),'NAME':([52,],[54,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'run_command':([0,],[1,]),'createServer':([0,],[2,]),'allowConnection':([0,],[3,]),'closeConnection':([0,],[4,]),'showClients':([0,],[5,]),'closeClient':([0,],[6,]),'createClient':([0,],[7,]),'sendMessage':([0,],[8,]),'showServer':([0,],[9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> run_command","S'",1,None,None,None),
  ('run_command -> createServer','run_command',1,'p_run_command','EZ_LEXPAR.py',101),
  ('run_command -> allowConnection','run_command',1,'p_run_command','EZ_LEXPAR.py',102),
  ('run_command -> closeConnection','run_command',1,'p_run_command','EZ_LEXPAR.py',103),
  ('run_command -> showClients','run_command',1,'p_run_command','EZ_LEXPAR.py',104),
  ('run_command -> closeClient','run_command',1,'p_run_command','EZ_LEXPAR.py',105),
  ('run_command -> createClient','run_command',1,'p_run_command','EZ_LEXPAR.py',106),
  ('run_command -> sendMessage','run_command',1,'p_run_command','EZ_LEXPAR.py',107),
  ('run_command -> showServer','run_command',1,'p_run_command','EZ_LEXPAR.py',108),
  ('createServer -> CREATE SERVER PAR1 ADDRESS IP COMMA PORT INT COMMA NAME STRING PAR2','createServer',12,'p_creatServer','EZ_LEXPAR.py',115),
  ('createClient -> CONNECTING TO SERVER PAR1 ADDRESS IP COMMA PORT INT PAR2','createClient',10,'p_createClient','EZ_LEXPAR.py',124),
  ('allowConnection -> MORE CONNECTION IN STRING COLON INT','allowConnection',6,'p_allowConnection','EZ_LEXPAR.py',136),
  ('showClients -> SHOW CLIENTS INFO IN STRING','showClients',5,'p_showClients','EZ_LEXPAR.py',145),
  ('showServer -> SHOW STRING INFO','showServer',3,'p_showServer','EZ_LEXPAR.py',155),
  ('closeConnection -> CLOSE CONNECTION PAR1 STRING PAR2','closeConnection',5,'p_closeConnection','EZ_LEXPAR.py',165),
  ('closeClient -> CLOSE CONNECTION PAR1 STRING IN STRING PAR2','closeClient',7,'p_closeClient','EZ_LEXPAR.py',178),
  ('sendMessage -> SEND MESSAGE PAR1 STRING PAR2','sendMessage',5,'p_sendMessage','EZ_LEXPAR.py',191),
]
