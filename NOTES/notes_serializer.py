from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
s = Serializer('secret',50)
token = s.dumps({'user_id': 2}).decode('utf-8')
token
s.loads(token)

