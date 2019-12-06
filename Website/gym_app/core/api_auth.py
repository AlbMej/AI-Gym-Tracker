import json
import base64

from django.http import HttpResponse
from django.contrib.auth import models
from django.core.exceptions import ObjectDoesNotExist

from gym_app.core.models import User


class ApiAuth:

    def __init__(self, call_method):
        self.call_method = call_method

    def unauthorized(self):
        data = {'error': 'Invalid authorization token provided'}
        data_json = json.dumps(data)
        return HttpResponse(data_json, content_type='application/json', status=403)

    def __call__(self, request):
        is_valid = False
        username = None
        try:
            print(models.User.objects.filter(username='test_gabe'))
            # auth = request.META['HTTP_AUTHORIZATION'].split(' ', 1)
            # username, api_key = base64.b64decode(auth[1]).decode('utf-8').split(':', 1)
            # user = models.User.objects.get(username=username)
            # api_client = APIClient.get_by_user(user)
            # if api_client.api_key == api_key:
            #     is_valid = True
        except Exception as e:
            raise e
        # except KeyError:
        #     is_valid = False
        # except ObjectDoesNotExist:
        #     is_valid = False

        if is_valid and username is not None:
            try:
                _return = self.call_method(request, username)
            except Exception as e:
                data_json = json.dumps({'status': 'error', 'msg': 'Internal Error'})
                _return = HttpResponse(data_json, content_type='application/json')
            return _return
        else:
            return self.unauthorized()
