from marshmallow import Schema,fields

class PlainUserSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    company_name = fields.Str()
    password = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str(required=True)
    image = fields.Str()
    usertype = fields.Str(required=True)

class LocationSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)

class UserSchema(PlainUserSchema):
    location = fields.Int(required=True)
    location_name = fields.Nested(PlainUserSchema(), dump_only=True)

class LoginSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True,load_only=True)