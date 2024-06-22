from flask import abort, request
from .models import db, RioUser, UserGroupUser, UserGroup, ApiKey, UserIpAddress
from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps
from .user_util import *
import time, os

'''
Accepts an array of UserGroups who have permission to use this endpoint
'''
def api_key_check(acceptable_user_groups, unacceptable_user_groups=[]):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            
            admin_key_provided = request.is_json and 'ADMIN_KEY' in request.json
            if (admin_key_provided):
                admin_key = request.json.get('ADMIN_KEY')
                if (admin_key != os.getenv('ADMIN_KEY')):
                    return abort(462, description="No API Key, Rio Key or JWT Provided")
                return func(*args, **kwargs)

            # Declare user var
            rio_user = None
            # Check if api_key is provided
            rio_user = get_user(request)
            if not rio_user:
                return abort(463, 'No matching user')

            # Check if RioUser has correct group privledge
            user_groups = db.session.query(
                UserGroup.name
            ).join(
                UserGroupUser
            ).join(
                RioUser
            ).filter(
                RioUser.id == rio_user.id
            )

            user_in_acceptable_group = False
            user_in_unacceptable_group = False
            for group in user_groups:
                if group.name in acceptable_user_groups:
                  user_in_acceptable_group = True
                if group.name in unacceptable_user_groups:
                  user_in_unacceptable_group = True
            if user_in_acceptable_group and not user_in_unacceptable_group:    
                return func(*args, **kwargs)
            #TODO maintain counts for validation methods

            # api_key = ApiKey.query.filter_by(api_key=in_api_key).first()
            # if not api_key:
            #     abort(462, "Invalid api_key")
            #     for group in user_groups:
            #         if group.name in acceptable_user_groups:
            #             api_key.total_pings += 1
            #             api_key.pings_daily += 1
            #             api_key.pings_weekly += 1
            #             api_key.last_ping_date = int(time.time())
            #             db.session.add(api_key)
            #             db.session.commit()

                        # func(*args, **kwargs)
                        # return
            return abort(464, 'You do not have valid permissions to use this endpoint.')
        return decorated_function
    return decorator

def record_ip_address(func):
    @wraps(func)
    def decorated_function():
        # Declare user var
        rio_user = None
        # Check if api_key is provided
        rio_user = get_user(request)
        if not rio_user:
            return abort(465, 'No matching user')
        
        update_ip_address_entry(rio_user, request)

        return func()
    return decorated_function
