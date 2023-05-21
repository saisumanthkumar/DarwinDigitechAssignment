import json
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import User

def home(request):
    if request.method == 'GET':
        return JsonResponse({'data': 'Welcome!'})

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        mobile = data.get('mobile')
        name = data.get('name')
        address = data.get('address')
        email = data.get('email')

        # Validate
        # Regex validation are in models
        if not (username and password and mobile and name and address and email):
            return HttpResponseBadRequest(json.dumps({'error': 'Missing required fields.'}), content_type='application/json')

        # Save user
        user = User(username=username, password=password, mobile=mobile, name=name, address=address, email=email)
        user.save()

        #Email to user
        email_subject = 'Registration Successful'
        email_message = f'Your account has been created. Username: {username}, Password: {password}'
        send_mail(email_subject, email_message, 'noreply@example.com', [email], fail_silently=True)

        return JsonResponse({'user_id': user.id})
    
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        if not (username and password):
            return HttpResponseBadRequest(json.dumps({'error': 'Missing username or password.'}), content_type='application/json')

        # Check whether credentials are incorrect
        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Invalid credentials.'}, status=401)

        return JsonResponse({'message': 'Login successful.'})

def select_all_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        user_list = []

        for user in users:
            user_data = {
                'username': user.username,
                'mobile': user.mobile,
                'name': user.name,
                'address': user.address,
                'email': user.email,
            }
            user_list.append(user_data)

        return JsonResponse(user_list, safe=False)

