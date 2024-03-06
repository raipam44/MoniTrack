# # middleware.py
# from django.shortcuts import redirect
# from django.utils import timezone
# from django.contrib.sessions.models import Session
# from django.conf import settings
# import datetime
# from django.contrib.auth import logout
# from django.dispatch import receiver
# from django.contrib.auth.signals import user_logged_out 

# from main.models import update_session

# class SessionTimeoutMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if request.user.is_authenticated:
#             current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#             last_activity = request.session.get('last_activity', None)
#             if last_activity:
#                 last_activity = datetime.datetime.strptime(last_activity, '%Y-%m-%d %H:%M:%S')
#                 if (datetime.datetime.now() - last_activity).seconds > 10: # 30 seconds = timeout duration
                  
#                    return self.process_logout(request, timezone.now())
#             request.session['last_activity'] = current_time
#         response = self.get_response(request)
#         return response
    
#     def process_logout(self, request, time):
#         # Your custom logic before logout (optional)
#         update_session(request.user,time)
#         logout(request)
#         return redirect('home')
    
  